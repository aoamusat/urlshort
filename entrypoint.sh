#!/bin/bash

alembic upgrade head

# Run the main application command
exec "$@"
