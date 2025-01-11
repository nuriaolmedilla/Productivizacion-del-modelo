# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files into the container
COPY src/ src/
COPY modelo/ modelo/
COPY env/requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Flask API
EXPOSE 5000

# Command to run the API
CMD ["python", "src/app.py"]
