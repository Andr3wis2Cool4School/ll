def moveZeroes(nums):
    for index, i in enumerate(nums):
        if i == 0:
            nums.remove(nums[index])
            nums.append(0)
    return nums
