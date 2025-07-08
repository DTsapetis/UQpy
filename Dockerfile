#RUN curl -fsSL https://get.docker.com -o get-docker.sh
#RUN chmod +x get-docker.sh
#RUN sh get-docker.sh

# Build the image based on the official Python version 3.9 image
FROM python:3.9-slim@sha256:c2a0feb07dedbf91498883c2f8e1e5201e95c91d413e21c3bea780c8aad8e6a7

# Use RUN to install Python packages (numpy and scipy) via pip, Python's package manager
RUN pip install --no-cache-dir UQpy
