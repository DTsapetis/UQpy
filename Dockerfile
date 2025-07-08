#RUN curl -fsSL https://get.docker.com -o get-docker.sh
#RUN chmod +x get-docker.sh
#RUN sh get-docker.sh

# Build the image based on the official Python version 3.9 image
FROM python:3.13-slim@sha256:6544e0e002b40ae0f59bc3618b07c1e48064c4faed3a15ae2fbd2e8f663e8283

# Use RUN to install Python packages (numpy and scipy) via pip, Python's package manager
RUN pip install --no-cache-dir UQpy
