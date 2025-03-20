import pytest

# Setup and Teardown at Function Level
def setup_function():
    print("\nSetting up resources for the test")
    
def teardown_function():
    print("Tearing down resources after the test")

def test_example_1():
    print("Running test_example_1")
    assert True

def test_example_2():
    print("Running test_example_2")
    assert True
