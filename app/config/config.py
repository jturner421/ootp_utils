import os
from pathlib import Path
import json

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASEDIR = Path().resolve()


class DBConfig:
    """
    Environment variables for backend infrastructure

    """
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    postgres_host = os.getenv('POSTGRES_HOST')
    postgres_port = os.getenv('POSTGRES_PORT')
    postgres_db = os.getenv('POSTGRES_DB')
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    POSTGRES_DATABASE_URI = f"postgresql+asyncpg://{postgres_user}:{postgres_password}@{postgres_host}:" \
                            f"{postgres_port}/{postgres_db}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    # DB_METADATA_PATH = os.getenv('DB_METADATA_PATH')
