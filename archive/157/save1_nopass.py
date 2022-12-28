import unicodedata 
import string

def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    all_accented_chars= [c for c in text if unicodedata.category(c)=='Ll' and c.lower() not in string.ascii_lowercase]
    return sorted(list(set(all_accented_chars)))
txt=("Sevilla es la capital de Andalucía, y para muchos, "
    "la ciudad más bonita de España. Pasear por sus calles, "
    "contemplar la Giralda, la Catedral o la Torre del Oro "
    "es una auténtica gozada. En primavera el olor a azahar "
    "lo envuelve todo. Al igual que Granada, toda la ciudad "
    "es una auténtica delicia. Su clima hace propensa la "
    "visita en casi cualquier época del año.")


print(filter_accents(txt))

#    ['á', 'é', 'í', 'ñ'],