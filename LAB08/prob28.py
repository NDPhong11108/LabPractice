def apply_command(records, command):
    if command[0] == "SHOW":
        if not records:
            return "EMPTY"
        parts = []
        for key in sorted(records):  # sorted by event, then category
            parts.append(f"{key[0]}/{key[1]}: {records[key]}")
        return ", ".join(parts)

    key = (command[1], command[2])
    amount = int(command[3])
    if command[0] == "ADD":
        records[key] = records.get(key, 0) + amount
    else:  # SELL
        if key not in records:
            return "NOT FOUND"
        if amount > records[key]:
            return "INSUFFICIENT"
        records[key] -= amount
    left = records[key]
    if left == 0:
        del records[key]
    return f"{key[0]}/{key[1]}: {left}"


records = {}
n = int(input())
i = 0
while i < n:
    event, category, count = input().split()
    records[(event, category)] = int(count)
    i += 1

while True:
    command = input().split()
    if command[0] == "END":
        break
    print(apply_command(records, command))
