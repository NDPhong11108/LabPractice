KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def encode(text):
    text = text.lower()
    if text == "":
        return "Invalid text"
    groups = []
    for ch in text:
        if ch == " ":
            groups.append("0")
        else:
            for key in KEYS:
                if ch in KEYS[key]:
                    groups.append(key * (KEYS[key].find(ch) + 1))
                    break
            else:  # not a letter
                return "Invalid text"
    return " ".join(groups)


def decode(code):
    result = ""
    for group in code.split(" "):
        if group == "0":
            result += " "
        elif group != "" and group[0] in KEYS and group == group[0] * len(group) \
                and len(group) <= len(KEYS[group[0]]):
            result += KEYS[group[0]][len(group) - 1]
        else:
            return "Invalid code"
    return result


mode = input()
line = input()
if mode == "encode":
    print(encode(line))
elif mode == "decode":
    print(decode(line))
