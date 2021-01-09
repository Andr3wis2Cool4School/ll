def findMaxConsecutiveOnes(nums):
    
    res = 0 
    cou = 0

    for i in nums:
        if i == 1:
            cou += 1
        else:
            res = max(cou, res)
            cou = 0
    return max(cou, res)


print(findMaxConsecutiveOnes([1,1,0,0,1,1]))
