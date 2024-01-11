import json
import os
import tempfile
from develop.utils import load_data


def test_load_data():
    with tempfile.NamedTemporaryFile('w+', suffix='.json', delete=False) as temp_file:
        test_data = {"key": "value"}
        json.dump(test_data, temp_file)
        temp_file_path = temp_file.name

    try:
        result = load_data(temp_file_path)

        assert result == test_data
    finally:
        temp_file.close()
        os.remove(temp_file_path)
