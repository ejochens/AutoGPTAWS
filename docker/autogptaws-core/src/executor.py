import subprocess

class CodeExecutor:
    @staticmethod
    def run_code(code: str) -> str:
        """Executes the given Python code in a safe subprocess."""
        try:
            process = subprocess.run(["python3", "-c", code], capture_output=True, text=True)
            return process.stdout if process.stdout else process.stderr
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    sample_code = "print('Hello from executor!')"
    print(CodeExecutor.run_code(sample_code))
