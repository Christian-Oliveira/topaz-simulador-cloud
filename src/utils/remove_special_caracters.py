# -*- coding: utf-8 -*-
import re

def remove_special_caracters(text: str) -> str:
    list_words = []
    for word in text:
        if re.search(r'([0-9]|,)', word):
            list_words.append(word)
    return "".join(list_words)