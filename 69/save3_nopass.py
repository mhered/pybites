import re

def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    return bool(
        re.match('.+[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.+', text)
    )

# 2014-07-03T23:27:51 

def is_integer(number):
    """Return True if number is an integer"""
    return bool(
        re.match('^-*[0-9]+$', str(number))
    )


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return bool(
        re.match('([a-zA-Z]+?-[a-zA-Z]+?)', text)
    )


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub("\s\(.\)", "", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    re.findall("^[?!.,;] \s",text)


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub("[ ]+?", " ", text)

def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return bool(
        re.match('([aeiou]){3}', word.lower())
    )


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    date_lst = re.findall("^(\d{2})/(\d{2})/(\d{4})$", date)
    return f"{date_lst[0][1]}/{date_lst[0][0]}/{date_lst[0][2]}"


print(has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.'))
print(is_integer("-29"))
print(has_word_with_dashes("hola caracola speak-up"))

print(remove_all_parenthesis_words('Good morning (afternoon)'))
print(split_string_on_punctuation("hi, how are you doing? blabla   "))
print(remove_duplicate_spacing("  hello    how are   you   "))

print(has_three_consecutive_vowels("sioux"))
print(convert_emea_date_to_amer_date("31/12/2022"))
