#!/bin/bash

# Wait for database to be ready
echo "Waiting for database to be ready..."
./wait-for-db.sh db

# Initialize database
echo "Initializing database..."
python3 exploitx/init_db.py

# Start Flask application
echo "Starting Flask application..."
python3 -m flask --app exploitx/app.py run --host=0.0.0.0 