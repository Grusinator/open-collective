FROM python:3.9

# Install Gunicorn
RUN pip install gunicorn

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev

# Install any missing dependencies for enhanced language service
RUN apt-get update && apt-get install -y libicu-dev

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
