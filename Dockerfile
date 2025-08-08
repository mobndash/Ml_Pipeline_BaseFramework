FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for xgboost, catboost, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Use JSON array syntax for CMD to prevent signal handling issues
CMD ["python", "application.py"]
