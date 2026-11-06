def collapse_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
        elif result != "" and result[-1] != " ":  # no leading spaces, no double spaces
            result += ch
    if result != "" and result[-1] == " ":  # drop the trailing space
        result = result[:-1]
    if result == "":
        return "Empty string"
    return result


def last_index(haystack, needle):
    if needle == "":
        return "Empty needle"
    for i in range(len(haystack) - len(needle), -1, -1):  # try the highest start first
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


s = input()
mode = input()
line = input()
if mode == "clean":
    print(collapse_spaces(s))
elif mode == "last":
    print(last_index(s, line))
