def delivery_fee(distance, base_fee=3.00):
    return base_fee + distance * 1.50


print(f"{delivery_fee(float(input())):.2f}")
