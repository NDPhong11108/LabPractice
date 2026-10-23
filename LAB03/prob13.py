def trip_advice(battery, distance):
    if battery < 0 or battery > 100 or distance < 0 or distance != distance or distance == float("inf"):
        raise ValueError
    if distance > battery * 4:
        return "Cannot Reach"
    left = battery - distance / 4
    if left < 20:
        return f"Charge Recommended: {left:.1f}% left"
    return f"Go: {left:.1f}% left"


try:
    print(trip_advice(int(input()), float(input())))
except ValueError:
    print("Error: Invalid input")
