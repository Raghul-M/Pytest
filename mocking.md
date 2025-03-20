## ✅ **Understanding Mocking in Pytest**

In **pytest**, mocking is a way to replace parts of your code (like functions, classes, or objects) with **mock objects**. These mock objects simulate the behavior of real objects for testing purposes.

### 📌 **Why Use Mocks?**
- To **isolate** the unit of code you're testing.
- To avoid making actual **API calls**, **database queries**, or performing **file operations**.
- To simulate scenarios like **exceptions** or specific **responses**.

---

## ✅ **Using `unittest.mock` in Pytest**
Pytest uses `unittest.mock`, a powerful Python library for mocking.

You can import it using:
```python
from unittest import mock
from unittest.mock import MagicMock, patch
```

### 📖 **Key Concepts**
- **`Mock`**: A generic mock object that can be used to simulate any object.
- **`MagicMock`**: A subclass of `Mock` with extra features (e.g., magic methods like `__len__`).
- **`patch`**: A decorator or context manager to temporarily replace objects for testing.

---

## ✅ **1. Example: Mocking a Function**

Suppose you have a function that calls an external API.

### **`app.py`**
```python
import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()
```

### **Test with Mock**
You can mock the `requests.get()` call to simulate API responses without making an actual API call.

```python
from unittest.mock import patch
import app

@patch('app.requests.get')
def test_get_weather(mock_get):
    # Simulate API response
    mock_get.return_value.json.return_value = {"temperature": 25, "city": "Chennai"}

    result = app.get_weather("Chennai")

    assert result == {"temperature": 25, "city": "Chennai"}
    mock_get.assert_called_once_with("https://api.weather.com/Chennai")
```

### 🔎 **Explanation**
- `@patch('app.requests.get')` replaces `requests.get()` with a mock object.
- `mock_get.return_value.json.return_value` simulates the API response.
- `assert_called_once_with()` ensures the function was called with the correct URL.

---

## ✅ **2. Example: Mocking a Class**

If a class has external dependencies like databases or services, you can mock it.

### **`database.py`**
```python
class Database:
    def connect(self):
        print("Connecting to database")
        return True

    def fetch_data(self):
        return {"user": "Raghul", "age": 30}
```

### **Test with Mock**
```python
from unittest.mock import MagicMock
from database import Database

def test_fetch_data():
    mock_db = MagicMock()
    mock_db.fetch_data.return_value = {"user": "Raghul", "age": 30}

    assert mock_db.fetch_data() == {"user": "Raghul", "age": 30"}
```

### 🔎 **Explanation**
- `MagicMock()` creates a mock object for the `Database` class.
- `.return_value` specifies the result of the `fetch_data()` method.

---

## ✅ **3. Example: Using `side_effect` for Exceptions or Dynamic Responses**

You can simulate exceptions or dynamic behavior using `side_effect`.

```python
from unittest.mock import MagicMock

def test_side_effect():
    mock_function = MagicMock(side_effect=[1, 2, 3, ValueError("Test Error")])

    assert mock_function() == 1
    assert mock_function() == 2
    assert mock_function() == 3
    
    try:
        mock_function()
    except ValueError as e:
        assert str(e) == "Test Error"
```

### 🔎 **Explanation**
- `side_effect` provides different results for each call.
- After the third call, it raises a `ValueError`.

---

## ✅ **4. Example: Using `patch` as a Context Manager**

You can also use `patch` as a **context manager** using `with`.

```python
from unittest.mock import patch
import app

def test_with_context_manager():
    with patch('app.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"status": "success"}
        result = app.get_weather("Mumbai")

        assert result == {"status": "success"}
        mock_get.assert_called_once_with("https://api.weather.com/Mumbai")
```

### 🔎 **Explanation**
- `with patch()` ensures the mock is applied **only within the block**.

---

## ✅ **5. Example: Mocking Time or External Libraries**

If your code uses `time.sleep()` or external libraries, you can mock them.

```python
import time
from unittest.mock import patch

def test_mock_time():
    with patch('time.sleep') as mock_sleep:
        time.sleep(5)
        mock_sleep.assert_called_once_with(5)
```

### 🔎 **Explanation**
- `patch('time.sleep')` mocks `time.sleep()`, so no actual delay occurs.

---


- Use **mocking** when your code interacts with **external systems**.
- Use **patch** to replace functions, classes, or objects temporarily.
- Use **side_effect** to simulate exceptions or dynamic responses.
- Use **MagicMock** for objects with complex behavior.

