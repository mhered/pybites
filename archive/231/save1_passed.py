import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [i for i, ch in enumerate(text) if ch in IS_EMOJI.findall(text)]


text = "We see more and more 🐍 Python 🥋 ninjas, keep it up 💪"
print(get_emoji_indices(text))