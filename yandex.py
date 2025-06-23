import requests
from logger import logger

def yandex_spell_check(text: str) -> str:
    try:
        response = requests.get(
            "https://speller.yandex.net/services/spellservice.json/checkText",params={"text": text})
        response.raise_for_status()
        data = response.json()

        corrected_text = text
        offset = 0
        for error in reversed(data):
            start = error['pos'] + offset
            end = start + error['len']
            if error['s']:
                replacement = error['s'][0]
                corrected_text = corrected_text[:start] + replacement + corrected_text[end:]
                offset += len(replacement) - error['len']
                incorrect_word = text[start:end]
                logger.info(f"Исправлено слово '{incorrect_word}': заменено на '{replacement}'")
        return corrected_text
    except Exception as e:
        logger.error("Ошибка проверки правописания:", e)
        return text