VOWELS = list("aeiou")


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""

    tuples = [
        (word, sum(c in VOWELS for c in word)) for word in text.casefold().split()
    ]

    return max(tuples, key=lambda x: x[1])


if __name__ == "__main__":

    test_text = """
    Python is an easy to learn, powerful programming language. It has efficient high-level data structures
    and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic 
    typing, together with its interpreted nature, make it an ideal language for scripting and rapid 
    application development in many areas on most platforms.
    """

    print(get_word_max_vowels(test_text))