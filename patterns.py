import re


pattern_fio = re.compile(r"\b[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+\b")
pattern_phone = re.compile(r"(?:\+7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}|\b\d{4}\b")
pattern_cabinet = re.compile(r"\b(каб|кабинет(е|ах)?|отдел(е|ах)?|регистратур(е|а|ах)?\d{1,3}\w*|\w*\d{1,3}\b)", re.IGNORECASE)