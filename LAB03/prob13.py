import math

KM_PER_PERCENT = 4
LOW_BATTERY = 20


def trip_advice(battery, distance):
    if not isinstance(battery, int) or isinstance(battery, bool) or not 0 <= battery <= 100:
        raise ValueError("Invalid input")
    if not isinstance(distance, (int, float)) or isinstance(distance, bool):
        raise ValueError("Invalid input")
    if not math.isfinite(distance) or distance < 0:
        raise ValueError("Invalid input")

    if distance > battery * KM_PER_PERCENT:
        return "Cannot Reach"

    left = battery - distance / KM_PER_PERCENT
    if left < LOW_BATTERY:
        return f"Charge Recommended: {left:.1f}% left"
    return f"Go: {left:.1f}% left"


def main():
    try:
        battery = int(input().strip())
        distance = float(input().strip())
        print(trip_advice(battery, distance))
    except ValueError:
        print("Error: Invalid input")


if __name__ == "__main__":
    main()
