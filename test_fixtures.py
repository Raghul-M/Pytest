import pytest

# Define a simple fixture
@pytest.fixture
def sample_data():
    print("\nSetting up sample data")
    data = {"name": "Alice", "age": 30}
    yield data
    print("Tearing down sample data")

def test_example_1(sample_data):
    print("Running test_example_1")
    assert sample_data["name"] == "Alice"

def test_example_2(sample_data):
    print("Running test_example_2")
    assert sample_data["age"] == 30
