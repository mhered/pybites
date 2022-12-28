def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""

    line_count = 0
    word_count = 0
    char_count = 0

    with open(file_) as f:
        for line in f.readlines():
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())

    return f"   {line_count}    {word_count}    {char_count}    {file_}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))