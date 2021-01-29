def insertionSort(nums):
    for i in range(1, len(nums)-1):
        val = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > val:
            nums[j + 1] = nums[j]
            i -= 1 
        nums[i+2] = val

    return nums














