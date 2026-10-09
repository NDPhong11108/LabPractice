def calculate_bill(unit_price, quantity):
    return unit_price * quantity


unit_price, quantity = input().split()
print(f"Total: {calculate_bill(float(unit_price), int(quantity)):.2f}")
