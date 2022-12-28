from typing import List, NamedTuple

from textblob import Word

from collections import namedtuple

MIN_CONFIDENCE = 0.5


# define SuggestedWord NamedTuple with attributes
# word (str) and confidence (float)
SuggestedWord = namedtuple('SuggestedWord', ['word','confidence'])


def get_spelling_suggestions(
    word: str, min_confidence: float = MIN_CONFIDENCE
) -> List[SuggestedWord]:
    """
    Find spelling suggestions with at least minimum confidence score
    Use textblob.Word (check out the docs)
    """
    w = Word(word)
    return [SuggestedWord(word, confidence) for word, confidence in w.spellcheck() if confidence >= min_confidence]


"""
print(get_spelling_suggestions('pron', min_confidence=0.1))
"""