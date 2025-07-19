FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update \
  && apt-get install -y libpq-dev gcc \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get remove -y gcc \
  && rm -rf /var/lib/apt/lists/*

COPY . .
RUN chmod +x entrypoint.sh
COPY app.py /app/
COPY templates/ /app/templates/
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "app.py"]

