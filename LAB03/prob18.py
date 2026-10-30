def merged_median(a, b):
    merged = a + b
    merged.sort()
    mid = len(merged) // 2
    if len(merged) % 2 == 1:
        return float(merged[mid])
    return (merged[mid - 1] + merged[mid]) / 2


n = int(input())
a = []
for x in input().split():
    a.append(int(x))
m = int(input())
b = []
for x in input().split():
    b.append(int(x))
print(f"{merged_median(a, b):.1f}")
