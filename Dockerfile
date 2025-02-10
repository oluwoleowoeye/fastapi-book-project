# Use an official lightweight Python image as the base
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose FastAPI's default port
EXPOSE 8000

# Set FastAPI entry point
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

