def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    languages = list(programmers.values())
    return list(set(languages[0]).intersection(*languages))

