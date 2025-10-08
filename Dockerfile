#RUN curl -fsSL https://get.docker.com -o get-docker.sh
#RUN chmod +x get-docker.sh
#RUN sh get-docker.sh

# Build the image based on the official Python version 3.9 image
FROM python:3.14-slim@sha256:9dc4ef3e628432af2237d1418908f5c6d4528e9f776aaa6e7c95c18854c86e48

# Use RUN to install Python packages (numpy and scipy) via pip, Python's package manager
RUN pip install --no-cache-dir UQpy
