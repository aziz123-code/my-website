import psycopg2
from logger import logger

BOT_TOKEN = '7550874873:AAEjFAzzv7b_F6XznDVLC95v5Bodc3DxHM0'


#DB_CONFIG = {
#    "dbname": "request_bot",
#    "user": "postgres",
#    "password": "KEFTEME",
#    "host": "localhost",
#    "port": 5432
#}


DB_CONFIG = {
    "dbname": "railway",
    "user": "postgres",
    "password": "FcoPDnBBnSfpcIFnPLTkBnezTQsJcyKG",
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

