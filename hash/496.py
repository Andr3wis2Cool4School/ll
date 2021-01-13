def nextGreaterElement(nums1, nums2):
    hp = dict()
    stack = list()
    res = list()

    for num in nums2:
        while len(stack) != 0 and num > stack[-1]:
            temp = stack.pop()
            hp[temp] = num
        stack.append(num)

    while len(stack) != 0:
        temp = stack.pop()
        hp[temp] = -1

    for num in nums1:
        res.append(hp[num])

    return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
