def count_orders(orders):
    counts = {}
    for dish in orders:
        counts[dish] = counts.get(dish, 0) + 1
    return counts


def sort_dishes(dishes):  # bubble sort
    for i in range(len(dishes) - 1):
        for j in range(len(dishes) - 1 - i):
            a = dishes[j]
            b = dishes[j + 1]
            # swap if b should come first: more orders, or same orders and smaller name
            if b[1] > a[1] or (b[1] == a[1] and b[0] < a[0]):
                dishes[j], dishes[j + 1] = b, a


counts = count_orders(input().split())
dishes = list(counts.items())
sort_dishes(dishes)
for name, count in dishes:
    print(name, count)
print(f"Different dishes: {len(dishes)}")
