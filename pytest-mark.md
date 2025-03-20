## ✅ **Understanding `pytest.mark` in Pytest**

In **pytest**, `@pytest.mark` is a way to **tag** or **label** test functions with metadata. You can then use these marks to:
- **Filter tests** using the `-m` option.
- **Skip or xfail (expected fail)** tests.
- **Parametrize tests** for multiple input values.

---

## 🔎 **Common Marks in Pytest**
Here are the most commonly used marks:

| Mark            | Purpose                                                   | Example Usage                                |
|------------------|-----------------------------------------------------------|--------------------------------------------|
| `@pytest.mark.skip` | Skip a test unconditionally                           | `@pytest.mark.skip(reason="Not implemented yet")` |
| `@pytest.mark.xfail` | Mark a test that is expected to fail                 | `@pytest.mark.xfail(reason="Known bug")`   |
| `@pytest.mark.parametrize` | Run a test with multiple sets of data          | `@pytest.mark.parametrize("x,y,result", [(1,2,3), (2,3,5)])` |
| `@pytest.mark.slow` | Custom marker to label slow tests                     | `@pytest.mark.slow`                        |
| `@pytest.mark.skipif` | Skip a test based on a condition                    | `@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")` |

---

## ✅ **1. Using `@pytest.mark.skip`**
Use `skip` when a test is not ready, irrelevant, or temporarily disabled.

```python
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_not_ready():
    assert False
```
- **Reason**: Provides a clear explanation.
- **Output**: It will be shown as `skipped` in the test results.

---

## ✅ **2. Using `@pytest.mark.xfail`**
Use `xfail` when you expect a test to fail (e.g., because of a known bug).

```python
@pytest.mark.xfail(reason="Bug #123, Fix in progress")
def test_known_bug():
    assert 1 + 1 == 3
```
- **Expected Fail**: If it fails, it’s marked as `xfail` (expected fail).
- **Unexpected Pass**: If it passes, it’s marked as `xpass` (unexpected pass).

---

## ✅ **3. Using `@pytest.mark.parametrize`**
Use `parametrize` to run a test function with multiple sets of inputs.

```python
import pytest

@pytest.mark.parametrize("x, y, result", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10)
])
def test_addition(x, y, result):
    assert x + y == result
```
- Runs **3 tests** with different values.
- Makes your code cleaner and reduces redundancy.

---

## ✅ **4. Using `@pytest.mark.skipif`**
Use `skipif` to conditionally skip a test based on certain conditions.

```python
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10 or higher")
def test_new_feature():
    assert True
```
- **Condition**: Checks Python version.
- **Reason**: Explains why it’s skipped.

---

## ✅ **5. Using Custom Marks**
You can create your own markers using `pytest.ini`.

### Step 1: Define custom marks in `pytest.ini`
```ini
[pytest]
markers =
    slow: marks tests as slow
    api: marks tests as API tests
```

### Step 2: Apply the custom mark
```python
import pytest

@pytest.mark.slow
def test_large_data_processing():
    assert True

@pytest.mark.api
def test_api_response():
    assert True
```

### Step 3: Run tests using the mark
```bash
pytest -m slow
```
- Only the `@pytest.mark.slow` tests will run.

---
- Use **skip** when a test is irrelevant or in progress.
- Use **xfail** when a test is broken and expected to fail.
- Use **parametrize** for clean and effective multiple data testing.
- Use **skipif** for conditional skips.
- Use **custom markers** to organize large test suites.
