def correct_record(records, name, value):
    new_records = dict(records)  # copy, so the original stays unchanged
    new_records[name] = (records[name][0], value)  # replace only the second value
    return new_records


def choose_record(records):
    winner = None
    best = 0
    for name in sorted(records):  # alphabetical, so ties keep the smaller name
        total = records[name][0] + records[name][1]
        if winner is None or total < best:
            winner = name
            best = total
    return winner


records = {}
for _ in range(2):
    name, d1, d2 = input().split()
    records[name] = (int(d1), int(d2))
name, value = input().split()

corrected = correct_record(records, name, int(value))
for name in sorted(corrected):
    print(f"{name}: {corrected[name][0]} {corrected[name][1]}")
winner = choose_record(corrected)
print(f"Lowest: {winner} {corrected[winner][0] + corrected[winner][1]}")
