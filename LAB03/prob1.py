def calculate_bill(unit_price, quantity):
    return float(unit_price * quantity)


unit_price, quantity = input().split()
total = calculate_bill(float(unit_price), int(quantity))
print(f"Total: {total:.2f}")
