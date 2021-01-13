def findKthLargest(nums, k):
    sorted_list = sorted(nums, reverse=True)
    return sorted_list[k-1]
