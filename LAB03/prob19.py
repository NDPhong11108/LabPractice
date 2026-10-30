def edit_list(nums, rm_index, to_append, to_insert_front, target, new_value):
    if 0 <= rm_index < len(nums):  # remove only if the index is valid
        nums.pop(rm_index)
    nums.append(to_append)
    nums.insert(0, to_insert_front)
    if target in nums:  # replace only the first match
        nums[nums.index(target)] = new_value
    print(*nums)


nums = []
for x in input().split():
    nums.append(int(x))
rm_index = int(input())
to_append = int(input())
to_insert_front = int(input())
target = int(input())
new_value = int(input())
edit_list(nums, rm_index, to_append, to_insert_front, target, new_value)
