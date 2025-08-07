#RUN curl -fsSL https://get.docker.com -o get-docker.sh
#RUN chmod +x get-docker.sh
#RUN sh get-docker.sh

# Build the image based on the official Python version 3.9 image
FROM python:3.13.6-slim@sha256:577ca9013fe0aec84258810ff8c93ecb1636984f6e40a797217bf30c82c3ea3b

# Use RUN to install Python packages (numpy and scipy) via pip, Python's package manager
RUN pip install --no-cache-dir UQpy
