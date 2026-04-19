FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY st4lker/ /app/st4lker/
COPY setup.py /app/setup.py
COPY requirements.txt /app/requirements.txt
COPY README.md /app/README.md

RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt
RUN pip install --no-cache-dir -e .

ENTRYPOINT ["st4lker"]
CMD ["--help"]
