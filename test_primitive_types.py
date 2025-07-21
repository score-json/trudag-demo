import pytest
import json


@pytest.fixture
def json_data():
    """Fixture that provides JSON data as a dictionary"""
    json_string = '''
    {
        "name": "Alice",
        "age": 30,
        "height": 5.5,
        "is_student": false,
        "address": null
    }
    '''
    return json.loads(json_string)


def test_string_type(json_data):
    """Test to check the 'name' key is a string."""
    assert isinstance(json_data["name"], str), "Expected 'name' to be a string"


def test_integer_type(json_data):
    """Test to check the 'age' key is an integer."""
    assert isinstance(json_data["age"], int), "Expected 'age' to be an integer"


def test_float_type(json_data):
    """Test to check the 'height' key is a float."""
    assert isinstance(json_data["height"], float), "Expected 'height' to be a float"


def test_boolean_type(json_data):
    """Test to check the 'is_student' key is a boolean."""
    assert isinstance(json_data["is_student"], bool), "Expected 'is_student' to be a boolean"


def test_null_type(json_data):
    """Test to check the 'address' key is null (None in Python)."""
    assert json_data["address"] is None, "Expected 'address' to be null (None in Python)"
