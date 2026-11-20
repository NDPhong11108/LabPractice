def square_roots(numbers):
    result = []
    i = 0
    while i < len(numbers):
        r = 0
        while r * r <= numbers[i]:
            if r * r == numbers[i]:
                result.append(r)
                break
            r += 1
        else:  # no break: not a perfect square
            result.append(-1)
        i += 1
    return result


n = int(input())
numbers = []
for x in input().split():
    numbers.append(int(x))
for r in square_roots(tuple(numbers)):
    if r == -1:
        print("NONE")
    else:
        print(r)
