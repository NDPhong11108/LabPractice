def list_operations(numbers):
    print(sum(numbers))
    print(min(numbers))
    print(max(numbers))
    print(*numbers[::-1])


input()
numbers = list(map(int, input().split()))
list_operations(numbers)
