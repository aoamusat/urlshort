#!/usr/bin/env bash
# exit on error
set -o errexit

# Install project dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Run the application
uvicorn main:app --host 0.0.0.0 --port 10000