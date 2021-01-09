def removeElement(nums, val):
    if nums == None or len(nums) == 0:
        return 0

    # 优雅的双指针
    i = 0
    j = len(nums) - 1 # two points

    while l < j:
        while (l < j and nums[l] != val):
            l += 1
        while (l <j and nums[j] == val):
            j -= 1

        nums[l], nums[j] = nums[j], nums[l]

        if nums[l] == val:
            return l 
        else:
            return l + 1




