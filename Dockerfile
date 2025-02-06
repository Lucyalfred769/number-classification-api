# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install flask flask-cors requests gunicorn

# Expose port
EXPOSE 5000

# Run the app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
