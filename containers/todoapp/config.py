import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DB_URL', 'mysql+pymysql://admin:admin@mysql:3306/mydb'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False