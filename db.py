import os
from dotenv import load_dotenv
import psycopg2
from logger import logger

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PASSWORD = os.getenv("DB_PASSWORD")




DB_CONFIG = {
    "dbname": "railway",
    "user": "postgres",
    "password": DB_PASSWORD,
    "host": "yamabiko.proxy.rlwy.net",
    "port": 24730,
    "sslmode": "require"
}


def save_request(tags: str, text: str):
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO requests (tag, text) VALUES (%s, %s)', (tags, text))
        connection.commit()
        cursor.close()
        connection.close()
        logger.info('Успешно!')
    except Exception as e:
        logger.error('Не удалось подключится к базе!', e)

