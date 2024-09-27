# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file if you have one (optional)
# COPY requirements.txt .

# Install Flask (and other dependencies if required)
# Uncomment the following line if you have a requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Alternatively, install Flask directly if no requirements.txt
RUN pip install Flask

# Copy the rest of your application code to the container
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Expose the port the app runs on
EXPOSE 8080

# Set environment variables (optional)
# ENV ODOO_URL=https://your-default-odoo-url.com
# ENV PGADMIN_URL=https://your-default-pgadmin-url.com

# Command to run the application
CMD ["python", "app.py"]
