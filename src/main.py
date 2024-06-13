# Run locally: functions-framework --target=nfoursid --source=src/main.py --debug

import flask
import functions_framework
import pandas as pd

from nfoursid.nfoursid import NFourSID

@functions_framework.http
def nfoursid(request: flask.Request):

    # We only accept get requests
    if request.method != 'POST':
        return 'Only POST requests are accepted', 405
    
    request_json = request.get_json()
    if request_json is None:
        return 'JSON payload is missing', 400
    
    # Get the IO data
    io_data = request_json.get('io_data')
    if io_data is None:
        return 'io_data parameter is missing', 400
    # And convert it back to a pandas dataframe
    try:
        io_data = pd.read_json(io_data, orient='split')
    except:
        return 'io_data parameter is not a valid dataframe', 400

    # Get the u and y column name
    u_column_names = request_json.get('u_column_names')
    y_column_names = request_json.get('y_column_names')
    if u_column_names is None or y_column_names is None:
        return 'u_column_names or y_column_names parameter is missing', 400

    # num_block_rows defaults to 20
    num_block_rows = 20
    try:
        num_block_rows = int(request_json.get('num_block_rows'))
    except:
        pass

    # order defaults to 4
    order = 4
    try:
        order = int(request_json.get('order'))
    except:
        pass
    
    # Log the input parameters
    print(f'io_data: {io_data}')
    print(f'u_column_names: {u_column_names}')
    print(f'y_column_names: {y_column_names}')
    print(f'num_block_rows: {num_block_rows}')
    print(f'order: {order}')

    try:
        # Create the NFourSID object
        nfoursid = NFourSID(
            io_data,
            output_columns=y_column_names,
            input_columns=u_column_names,
            num_block_rows=num_block_rows
        )

        # Estimate the state-space model
        nfoursid.subspace_identification()
        identified, _ = nfoursid.system_identification(
            rank=order
        )

    except Exception as e:
        return str(e), 400

    # Extract the A, B, C, D matrices
    try:
        a, b, c, d = identified.a, identified.b, identified.c, identified.d

        output_json = {
            'a': a.tolist(),
            'b': b.tolist(),
            'c': c.tolist(),
            'd': d.tolist(),
        }

        return flask.jsonify(output_json), 200
    
    except Exception as e:
        return str(e), 400
