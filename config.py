"""
Configuration file for FastAPI
"""
import os

# Database connection string
DATABASE_URL=f"{os.environ.get('DATABASE_URL', 'sqlite:///:memory:')}"
BASE_URL=os.environ.get('BASE_URL', 'http://localhost/')
SENTRY_DSN=os.environ.get("SENTRY_DSN")