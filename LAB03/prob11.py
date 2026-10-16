import string as textlib

PREFIX = "FEEDBACK:"


def format_feedback(text):
    stripped = text.strip()
    formatted = textlib.capwords(stripped)
    bracketed = "[" + formatted + "]"
    return PREFIX + " " + bracketed


text = input()
result = format_feedback(text)
print(result)
