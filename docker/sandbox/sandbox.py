import sys

def execute_code(code):
    """Executes a given Python code string safely."""
    try:
        exec(code, {"__builtins__": {}})  # Restrict builtins for safety
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    sample_code = "print('Hello from sandbox!')"
    result = execute_code(sample_code)
    print(result)
