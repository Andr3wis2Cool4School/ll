def containsDuplicate(nums):
    dict = {} 
    if len(nums) == 0 or len(nums) == 1:
        return False

    for i in nums:
        if i in dict:
            return True
        dict[i] = 0
    return False








