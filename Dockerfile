FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser --disabled-password --no-create-home appuser
USER appuser
ENV PORT=8080
CMD exec uvicorn backend.main:app --host 0.0.0.0 --port ${PORT} --workers 1
