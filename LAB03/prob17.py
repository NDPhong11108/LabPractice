def list_operations(numbers):
    print(sum(numbers))
    print(min(numbers))
    print(max(numbers))
    print(*numbers[::-1])


n = int(input())
numbers = []
for x in input().split():
    numbers.append(int(x))
list_operations(numbers)
