FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements-dev.txt

ENV PYTHONPATH=/app/src

CMD ["python", "-m", "pytest"]
