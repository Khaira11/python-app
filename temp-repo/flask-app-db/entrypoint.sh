#!/bin/sh
set -e

echo "Waiting for database..."
# optional: wait until Postgres is ready (adjust host/db accordingly)
# until nc -z "$DB_HOST" 5432; do
#   echo "Waiting for Postgres..."
#   sleep 2
# done

echo "Creating tables if not exist..."
python - <<EOF
from app import app, db
with app.app_context():
    db.create_all()
EOF

echo "Starting Flask app..."
exec python app.py

