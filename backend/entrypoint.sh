#!/bin/sh

until nc -z -v -w30 db 5433
do
  echo "Waiting for database connection..."
  sleep 1
done

echo "Database is up!"

if [ ! -d "migrations" ]; then
  flask db init && flask db migrate -m "Initial migration"
fi

flask db upgrade
flask run --host=0.0.0.0 --port=5000
