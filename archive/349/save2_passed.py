import os
from pathlib import Path
from typing import List
import unicodedata
from urllib.request import urlretrieve
import re

def _get_spanish_dictionary_words() -> List[str]:
    filename = "spanish.txt"
    # source of file
    # https://raw.githubusercontent.com/bitcoin/bips
    # /master/bip-0039/spanish.txt
    url = f"https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
    tmp_folder = os.getenv("TMP", "/tmp")
    local_filepath = Path(tmp_folder) / filename
    if not Path(local_filepath).exists():
        urlretrieve(url, local_filepath)
    return local_filepath.read_text().splitlines()


SPANISH_WORDS = _get_spanish_dictionary_words()
_accentuate = {unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf8'): word for word in SPANISH_WORDS}

def get_accentuated_sentence(
    text: str, words: List[str] = SPANISH_WORDS
) -> str:
    replaced = []
    for word_w_signs in text.split():
        word = re.sub(r'[^a-zA-Z0-9]', '', word_w_signs)
        replaced.append(word_w_signs.replace(word, _accentuate.get(word, word)))
    return " ".join(replaced)

print(get_accentuated_sentence("sesion de escribir, primera pagina de mi poesia hecha"))