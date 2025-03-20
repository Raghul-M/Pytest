import pytest

@pytest.fixture
def sample_data():
    print("\nSetting up sample data")
    data = {"user": "Raghul", "role": "Admin"}
    yield data
    print("Tearing down sample data")
