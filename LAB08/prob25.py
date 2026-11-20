def sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10  # last digit
        number //= 10  # remove the last digit
    return total


number = int(input())
print(sum_digits(number))
