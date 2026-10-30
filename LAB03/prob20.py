def classify_mirror_balance(numbers):
    half = len(numbers) // 2
    first = numbers[:half]  # first half
    second = numbers[len(numbers) - half:]  # second half (middle skipped if odd)
    if first == second[::-1]:
        print("Mirror")
    elif sum(first) == sum(second):
        print("Balance")
    else:
        print("Unordered")


numbers = []
for x in input().split():
    numbers.append(int(x))
classify_mirror_balance(numbers)
