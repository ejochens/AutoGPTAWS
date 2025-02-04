import docker

class Sandbox:
    def __init__(self):
        self.client = docker.from_env()

    def execute_code(self, code: str) -> str:
        """Runs Python code inside an isolated Docker container."""
        container = self.client.containers.run(
            "python:3.9-slim",
            command=f'python3 -c "{code}"',
            remove=True,
            stdout=True,
            stderr=True
        )
        return container.decode("utf-8")

if __name__ == "__main__":
    sandbox = Sandbox()
    sample_code = "print('Hello from sandbox!')"
    print(sandbox.execute_code(sample_code))
