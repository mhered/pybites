import re
def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    matches = re.findall('"(.+?)"|([\w-]+)', text)
    return ["".join(item) for item in matches]


text = 'Should give "3 elements only"'
       
print(split_words_and_quoted_text(text))