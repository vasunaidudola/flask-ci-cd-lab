FROM python:3.11-slim

WORKDIR /app

COPY requirements/docker-requirements.txt /app/
RUN pip install --no-cache-dir -r docker-requirements.txt

COPY . /app

ENV PORT=8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
