# Use official Apache Airflow image
FROM apache/airflow:2.7.3-python3.9

# Switch back to airflow user before installing Python packages
USER airflow

# Set working directory
WORKDIR /opt/airflow

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Set default entrypoint
ENTRYPOINT ["/bin/bash", "-c"]
