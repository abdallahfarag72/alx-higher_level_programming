#!/usr/bin/python3

"""
Defines a function text_indentation
that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): text to be printed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    chars = [".", "?", ":"]
    for char in text:
        result += char
        if char in chars:
            result += "\n\n"

    lines = result.split("\n")
    formatted_lines = [line.strip() for line in lines if line.strip()]
    output = "\n".join(formatted_lines)
    print(output)
