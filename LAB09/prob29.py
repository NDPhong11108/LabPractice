def gnome_sort(heights):
    swaps = 0
    pos = 0
    while pos < len(heights):
        if pos == 0 or heights[pos - 1] <= heights[pos]:
            pos += 1
        else:
            heights[pos - 1], heights[pos] = heights[pos], heights[pos - 1]
            swaps += 1
            print(f"Swap {swaps}: {heights}")
            pos -= 1
    return swaps


heights = []
for x in input().split():
    heights.append(int(x))
print(f"Total swaps: {gnome_sort(heights)}")
