FROM python:3.9-slim

# Disable interactive mode
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /sandbox

# Copy sandbox script
COPY sandbox.py .

CMD ["python", "sandbox.py"]
