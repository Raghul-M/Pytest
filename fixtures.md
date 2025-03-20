✅ **What is a Fixture in Pytest?**

A **fixture** in **pytest** is a reusable function that provides setup and cleanup code for your tests. It helps manage resources like:

- Database connections
- API clients
- Temporary files
- Test data
- Environment setup

### 🔎 **Key Features of Fixtures**
- Automatically manage **setup and teardown** using `yield`.
- Reuse the same fixture across multiple tests.
- Improve test **readability** and **maintainability**.
- Can have different **scopes** (`function`, `class`, `module`, or `session`).

---

## ✅ **Why Do We Need Fixtures?**

- **Avoid Code Duplication:** Instead of repeating setup code in every test, use a fixture.
- **Ensure Proper Cleanup:** Fixtures clean up automatically using `yield`.
- **Enhance Readability:** Tests become simpler and more readable.
- **Provide Test Isolation:** Each test gets its own setup state.

---

## ✅ **Where Do We Use Fixtures?**

You can use fixtures in:
- **Unit Tests:** Mock database connections or API requests.
- **Integration Tests:** Prepare external services or resources.
- **UI Tests:** Set up a browser instance using Selenium.
- **Performance Tests:** Initialize large data sets.

---

## ✅ **Example 1: Basic Fixture**

```python
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
```

### **Explanation**  
- `@pytest.fixture`: Decorates the `sample_data()` function as a fixture.
- `yield data`: Provides the sample data to the test.
- Cleanup runs **after** the test completes (after `yield`).
- Both tests reuse the same fixture without redefining the data.

---

## ✅ **Example 2: Fixture with Different Scopes**

Fixtures can have different scopes:
- `function` (default): Runs before and after **every** test.
- `class`: Runs once for **each class** of tests.
- `module`: Runs once for **all tests in the module**.
- `session`: Runs once for the **entire test session**.

```python
@pytest.fixture(scope="class")
def db_connection():
    print("\nConnecting to database")
    yield "Database Connection"
    print("Closing database connection")

class TestDatabase:
    def test_query_1(self, db_connection):
        print("Running test_query_1 with", db_connection)

    def test_query_2(self, db_connection):
        print("Running test_query_2 with", db_connection)
```

### **Explanation**
- The fixture with `scope="class"` runs **once** before both tests and tears down after all tests in the class.

---

## ✅ **Example 3: Using Fixtures with Parameters**

You can pass parameters to fixtures to test multiple scenarios.

```python
@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def browser(request):
    print(f"\nStarting {request.param} browser")
    yield request.param
    print(f"Closing {request.param} browser")

def test_open_website(browser):
    print(f"Testing on {browser}")
    assert browser in ["Chrome", "Firefox", "Safari"]
```

### **Explanation**
- `params`: Runs the test **3 times**, once for each browser.
- `request.param`: Accesses the current parameter inside the fixture.

---

- Use **fixtures** to manage complex test setups.
- Leverage different **scopes** for efficient resource management.
- Combine **parameterized fixtures** for cross-browser or cross-environment testing.

