def count_pattern(text, pattern):
    text = text.lower()
    pattern = pattern.lower()
    total = 0
    for i in range(len(text) - len(pattern) + 1):  # every starting position
        if text[i:i + len(pattern)] == pattern:
            total += 1
    return total


try:
    text = input()
    pattern = input()
    if pattern == "":
        print("Invalid pattern")
    else:
        print(count_pattern(text, pattern))
except EOFError:
    print("Invalid pattern")
