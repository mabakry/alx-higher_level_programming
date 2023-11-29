#!/usr/bin/python3
"""Print text Module"""


def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return

    for i in range(0, len(text)):
        if text[i] in ('.', '?', ':'):
            print(text[i])
            print()
        elif text[i] == " " and text[i - 1] in ('.', '?', ':'):
            pass
        else:
            if text[i - 1] not in ('.', '?', ':') or text[i] != " ":
                print(text[i], end="")
    if text[i] != "\n":
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
