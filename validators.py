import spacy

from  words import negative_words, keywords
from patterns import pattern_fio, pattern_phone, pattern_cabinet
from logger import logger


nlp = spacy.load("ru_core_news_sm")

def find_tags(text: str) -> list[str]:
    text = text.lower()
    tags = []
    for tag, keyword in keywords.items():
        for word in keyword:
            if word in text and tag not in tags:
                tags.append(tag)
    return tags



def has_negative_words(text: str) -> bool:
    text = text.lower()
    for phrase in negative_words:
        if phrase in text:
            return True
    return False



def has_verb_and_noun(text: str) -> bool:
    ignored_words = {"регистратура", "отдел", "кабинет", "кабинете", "отделе", "кабинетах", "отделах"}
    nlp_doc = nlp(text)

    has_verb = False
    has_noun = False

    for word in nlp_doc:
        if word.pos_ == 'VERB':
            has_verb = True
        if word.pos_ == 'NOUN' and word.text.lower() not in ignored_words:
            has_noun = True
    logger.info(f'[SPACY] => verb={has_verb}, noun={has_noun}, text={text}')
    print(f'[SPACY] => verb={has_verb}, noun={has_noun}, text={text}')

    return has_verb and has_noun


def is_valid_request(text: str) -> bool:
    return all([
        pattern_cabinet.search(text),
        pattern_phone.search(text),
        pattern_fio.search(text),
        has_verb_and_noun(text)
    ])


def looks_like_request(text: str) -> bool:
    matches = [
        bool(pattern_cabinet.search(text)),
        bool(pattern_phone.search(text)),
        bool(pattern_fio.search(text)),
        bool(has_verb_and_noun(text))
    ]
    return sum(matches) >= 2