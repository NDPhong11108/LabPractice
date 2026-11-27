def due_earlier(a, b):
    # a task is (name, duration, deadline): earlier deadline, then shorter, then smaller name
    if a[2] != b[2]:
        return a[2] < b[2]
    if a[1] != b[1]:
        return a[1] < b[1]
    return a[0] < b[0]


n = int(input())
tasks = []
for _ in range(n):
    name, duration, deadline = input().split()
    tasks.append((name, int(duration), int(deadline)))

# insertion sort
for i in range(1, len(tasks)):
    current = tasks[i]
    j = i - 1
    while j >= 0 and due_earlier(current, tasks[j]):
        tasks[j + 1] = tasks[j]
        j -= 1
    tasks[j + 1] = current

time = 0
max_late = 0
for name, duration, deadline in tasks:
    start = time
    time += duration
    if time > deadline:
        late = time - deadline
        max_late = max(max_late, late)
        print(f"{name}: {start}-{time} (late by {late})")
    else:
        print(f"{name}: {start}-{time} (on time)")
print(f"Max lateness: {max_late}")
