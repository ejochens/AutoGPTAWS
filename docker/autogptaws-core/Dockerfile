# Use a minimal Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire source directory
COPY src/ /app/src/

# Copy the config.yaml file to /app/
COPY config.yaml /app/config.yaml

# Set up entrypoint to run AI engine
CMD ["python", "/app/src/ai_engine.py"]
