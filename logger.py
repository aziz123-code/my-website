import logging


logging.basicConfig(
    level=logging.INFO, # Уровень логов: INFO — основные события, DEBUG — подробные, ERROR — ошибки
    format='%(asctime)s - %(levelname)s - %(message)s', # Формат записи: время - уровень - сообщение
    filename='bot.log', # название файла
    filemode='a', # метод append
    encoding='utf-8' # кодировка
)

logger = logging.getLogger()


logging.getLogger('pymorphy3').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('aiogram').setLevel(logging.WARNING)