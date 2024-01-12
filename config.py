import os

# Database connection string
DATABASE_URL=f"{os.environ.get('DATABASE_URL', 'sqlite:///:memory:')}"