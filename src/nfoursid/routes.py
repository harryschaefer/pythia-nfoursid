from flask import Blueprint, request, jsonify
import pandas as pd
import urllib.parse

from .nfoursid import NFourSID

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API"})

@main.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@main.route('/api/identify', methods=['GET'])
def identify():
    try:

        return jsonify({"message": "Identify endpoint"})

        # Get parameters from the request
        num_block_rows = int(request.args.get('num_block_rows'))
        input_columns = request.args.getlist('input_columns')
        output_columns = request.args.getlist('output_columns')
        df_json = request.args.get('df_json')
        order_to_fit = int(request.args.get('order_to_fit'))

        # Handle the case where input_columns might be null
        if not input_columns:
            input_columns = None

        # Decode and deserialize the JSON-encoded DataFrame
        df_json = urllib.parse.unquote(df_json)
        df = pd.read_json(df_json)

        nfoursid = NFourSID(
            dataframe=df,
            output_columns=output_columns,
            input_columns=input_columns,
            num_block_rows=num_block_rows
        )

        nfoursid.subspace_identification()

        state_space_identified, _ = nfoursid.system_identification(
            rank=order_to_fit
        )

        # return the matrices
        return jsonify({
            "A": state_space_identified.a.tolist(),
            "B": state_space_identified.b.tolist(),
            "C": state_space_identified.c.tolist(),
            "D": state_space_identified.d.tolist()
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
