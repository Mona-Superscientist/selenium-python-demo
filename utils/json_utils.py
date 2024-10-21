import json
import os


def load_json_data(file_name):
    """Load data from a JSON file in the testData directory."""
    # Define the absolute path to the testData directory
    test_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testData'))

    # Construct the full path to the JSON file
    file_path = os.path.join(test_data_dir, file_name)

    with open(file_path, 'r') as json_file:
        return json.load(json_file)
