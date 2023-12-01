def binary_search_rec(nums, target, low, high):
    if low > high:
        return -1

    # Finding the mid using floor division
    mid = low + ((high - low) // 2)

    # Target value is present at the middle of the array
    if nums[mid] == target:
        return mid

    # Target value is present in the low subarray
    elif target < nums[mid]:
        return binary_search_rec(nums, target, low, mid - 1)

    # Target value is present in the high subarray
    else:
        return binary_search_rec(nums, target, mid + 1, high)


def binary_search(nums, target):
    return binary_search_rec(nums, target, 0, len(nums) - 1)


def main():
    nums_lists = [[], [0, 1], [1, 2, 3], [-1, 0, 3, 5, 9, 12], [-1, 0, 3, 5, 9, 12]]
    target_list = [12, 1, 3, 9, 2]
    for i in range(len(nums_lists)):
        nums = nums_lists[i]
        target = target_list[i]
        index = binary_search(nums, target)
        print(str(i + 1) + ". Array to search: " + str(nums))
        print("   Target: " + str(target))
        if index != -1:
            print("   " + str(target) + " exists in the array at index", index)
        else:
            print("   " + str(target) + " does not exist in the array so the return value is", index)
        print("----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()