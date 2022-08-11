import os

# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    'postgresql://postgres:postgres@localhost:5432/notes'
)

NOTES_API_SERVER = os.environ.get('NOTES_API_SERVER', 'http://localhost:5000')
