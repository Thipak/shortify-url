import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = os.getenv("SERVER_NAME", "localhost:5000")