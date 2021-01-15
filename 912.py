# soft merge
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return marge(merge_sort(left), merge_sort(right))

def marge(left, right):
    res = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
        else:
            res.append(right[0])

    res += left
    res += right
    return res 

