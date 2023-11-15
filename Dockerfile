# Python FastAPI

FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy project

COPY . .

# Run app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1337"]