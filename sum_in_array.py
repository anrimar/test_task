# solution 1:
# Time complexity: O(n^2)
def simple_solution(nums, S):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == S - nums[i]:
                return nums[i], nums[j]
    return -1


# solution 2:
# Time complexity:  O(nlogn)
# The binary search works perfectly in the case of the sorted array
def binary_search(array, x, low, high):
    """"helper function for later solution"""
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    return -1


def binary_solution(nums, S):
    for i in range(len(nums)):
        k = S - nums[i]
        j = binary_search(nums, k, 0, len(nums) - 1)

        if j != -1:
            return nums[i], nums[j]
    return -1


# solution 3:
# time complexity is O(n)
def hash_map_solution(nums, S):
    hashmap = {}
    for i in range(0, len(nums)):
        temp = S - nums[i]
        if (temp in hashmap):
            return temp, nums[i]
        hashmap[nums[i]] = i
    return -1
