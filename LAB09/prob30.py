def comes_before(a, b):
    if len(a) != len(b):
        return len(a) < len(b)
    return a < b


def find_first(words, start):
    first = start
    i = start + 1
    while i < len(words):
        if comes_before(words[i], words[first]):  # strict, so the leftmost wins ties
            first = i
        i += 1
    return first


words = input().split()
swaps = 0
k = 1
while k < len(words):
    first = find_first(words, k - 1)
    if first != k - 1:
        words[k - 1], words[first] = words[first], words[k - 1]
        swaps += 1
    print(f"Step {k}:", *words)
    k += 1
print(f"Swaps: {swaps}")
