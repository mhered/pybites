import os
from pathlib import Path
from typing import List
import unicodedata
from urllib.request import urlretrieve


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


def get_accentuated_sentence(
    text: str, words: List[str] = SPANISH_WORDS
) -> str:
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf8')
    
"""
strings = [
    (
        "Cuando era pequeno me gustaba jugar en la via",
        "Cuando era pequeño me gustaba jugar en la vía",
    ),
    ("un dos tres ... accion", "un dos tres ... acción"),
    ("anadir otra aficion", "añadir otra afición"),
    (
        "bajo el arbol descansando vi un avion",
        "bajo el árbol descansando vi un avión",
    ),
    (
        "no tomes mucho azucar o hay que evitar la bascula",
        "no tomes mucho azúcar o hay que evitar la báscula",
    ),
    (
        "vehiculo volando, utopia o realidad pronto ...?",
        "vehículo volando, utopía o realidad pronto ...?",
    ),
    (
        "telefono publico ... apenas ya no se ve en esta epoca",
        "teléfono público ... apenas ya no se ve en esta época",
    ),
    ("me falta jamon y jabon", "me falta jamón y jabón"),
    (
        "leyendo un libro en el jardin ... tarde de exito",
        "leyendo un libro en el jardín ... tarde de éxito",
    ),
    (
        "sesion de escribir, primera pagina de mi poesia hecha",
        "sesión de escribir, primera página de mi poesía hecha",
    ),
]

for tup in strings:
    string = tup[1]
    print(string)
    print(get_accentuated_sentence(string))
    
"""