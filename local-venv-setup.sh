# Set up the python virtual environment

# Delete the venv directory if it exists
if [ -d "venv" ]; then
    rm -rf venv
fi

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r src/requirements.txt
pip install -r notebook/requirements.txt
