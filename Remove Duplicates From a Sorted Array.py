def removeDuplicates(nums):
    i = 0
    while i + 1 < len(nums):
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i + 1])
        else:
            i += 1

    print(nums)
    print(len(nums))
    return len(nums)