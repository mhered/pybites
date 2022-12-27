import unicodedata 
import string

def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    all_accented_chars= [c for c in text.lower() if unicodedata.category(c)=='Ll' and c not in string.ascii_lowercase]
    return sorted(list(set(all_accented_chars)))
txt= ("The 5 French accents;"
     "The cédille (cedilla) Ç ..."
     "The accent aigu (acute accent) é ..."
     "The accent circonflexe (circumflex) â, ê, î, ô, û ..."
     "The accent grave (grave accent) à, è, ù ..."
     "The accent tréma (dieresis/umlaut) ë, ï, ü")


print(filter_accents(txt))

#    ['á', 'é', 'í', 'ñ'],
#    ['à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü'],
