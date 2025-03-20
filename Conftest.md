## ✅ **What is `conftest.py` in Pytest?**

In **pytest**, `conftest.py` is a special configuration file that allows you to define **fixtures** and **hooks** that can be shared across multiple test files without needing to import them.

### 🔎 **Key Features of `conftest.py`**
- No need to import the fixtures in test files — **pytest automatically discovers them**.
- Ideal for storing:
  - **Common Fixtures**
  - **Custom Hooks**
  - **Plugins**
  - **Command-line Options**
- Helps in **reducing duplication** and maintaining cleaner test files.

---

## ✅ **Why Use `conftest.py`?**
- **Reusability**: Fixtures in `conftest.py` are available to all test files in the directory and subdirectories.
- **Clean Code**: Keeps test files focused on the actual tests.
- **Centralized Management**: Easier to manage common setup and teardown logic.

---

## ✅ **Where to Place `conftest.py`?**

- Place `conftest.py` **in the same directory** as your test files or **at a higher level** to apply it to all subdirectories.
  
### Example Project Structure:
```
tests/
├── conftest.py   # Shared fixtures and configurations
├── test_login.py
├── test_dashboard.py
└── api/
    ├── conftest.py   # API-specific fixtures
    ├── test_users.py
    └── test_orders.py
```
- The fixtures in `tests/conftest.py` will be available to `test_login.py` and `test_dashboard.py`.
- The fixtures in `tests/api/conftest.py` will apply to `test_users.py` and `test_orders.py`.

---

## ✅ **Example 1: Simple Fixture in `conftest.py`**

### **`conftest.py`**
```python
import pytest

@pytest.fixture
def sample_data():
    print("\nSetting up sample data")
    data = {"user": "Raghul", "role": "Admin"}
    yield data
    print("Tearing down sample data")
```

### **Test File: `test_login.py`**
```python
def test_login(sample_data):
    print(f"Testing login for {sample_data['user']} with role {sample_data['role']}")
    assert sample_data["role"] == "Admin"
```

### 🔎 **Explanation**
- The fixture `sample_data` in `conftest.py` is automatically available to `test_login.py`.
- No import needed for `sample_data`.
- `yield` ensures cleanup after the test.

---

## ✅ **Example 2: Using Multiple Fixtures**

### **`conftest.py`**
```python
import pytest

@pytest.fixture
def db_connection():
    print("\nConnecting to the database")
    yield "DB Connection"
    print("Closing the database")

@pytest.fixture
def user_data():
    print("\nFetching user data")
    yield {"name": "Raghul", "age": 30}
    print("Releasing user data")
```

### **Test File: `test_dashboard.py`**
```python
def test_dashboard(db_connection, user_data):
    print(f"Testing dashboard with {user_data['name']} using {db_connection}")
    assert user_data['age'] > 18
```

### 🔎 **Explanation**
- Both `db_connection` and `user_data` are injected into the test function.
- Pytest handles the **setup** and **teardown** automatically.

---

## ✅ **Example 3: Custom Hooks in `conftest.py`**

You can customize test behavior using **pytest hooks** in `conftest.py`.

### **`conftest.py`**
```python
def pytest_runtest_setup(item):
    print(f"\n[Hook] Setting up for test: {item.name}")

def pytest_runtest_teardown(item):
    print(f"[Hook] Tearing down after test: {item.name}")
```

### 🔎 **Explanation**
- `pytest_runtest_setup()` runs **before** each test.
- `pytest_runtest_teardown()` runs **after** each test.
- Useful for additional logging or custom setup/teardown actions.


- Use `conftest.py` to **organize fixtures** and **avoid duplication**.
- Great for **large projects** with multiple test files.
- Customize behavior using **pytest hooks**.
- No need to import fixtures in your test files — just use them directly!

