# Pytest

### What is Pytest ?

- Testing framework for python
- Auto-discovy for tests
- Rich assertio introspection
- Support parameterized and fixture-based testing

### Why Pytest ?

- Simplified syntax
- Rich Assertion Introspection
- Powerful fixture System
- Compatibility
- Extensibility

### ✅ Why Use Setup and Teardown?
- Setup: To create resources (e.g., database connections, files, mock data) before running tests.

- Teardown: To clean up resources (e.g., close connections, delete files) after the test completes, ensuring no side effects.

### ✅ Explanation
- setup_function() runs before each test function.
- teardown_function() runs after each test function.
- Both functions will run for every test in the module.

