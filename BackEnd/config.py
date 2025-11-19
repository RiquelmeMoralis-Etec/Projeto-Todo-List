import secrets
import pymongo

class Config:
    SECRET_KEY = secrets.token_hex(32)
    SESSION_TYPE = "mongodb"
    SESSION_MONGODB = pymongo.MongoClient("mongodb://localhost:27017/")
    SESSION_MONGODB_DB = "todo_db"
    SESSION_MONGODB_COLLECT = "sessions"
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = False
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "todo_db"