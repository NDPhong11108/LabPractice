def merged_median(a, b):
    a.extend(b)  # put all numbers into one list
    a.sort()  # order them from small to big
    size = len(a)
    middle = size // 2
    if size % 2 == 1:  # odd: take the middle number
        return float(a[middle])
    return (a[middle - 1] + a[middle]) / 2  # even: average the two middle numbers


input()  # skip the size of the first list
a = []
for x in input().split():
    a.append(int(x))

input()  # skip the size of the second list
b = []
for x in input().split():
    b.append(int(x))

print(f"{merged_median(a, b):.1f}")
