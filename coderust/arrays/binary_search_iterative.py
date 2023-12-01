'''
pseudocode from https://en.wikipedia.org/wiki/Binary_search_algorithm:
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m − 1
        else:
            return m
    return unsuccessful
'''


def binary_search(nums, target):
  low = 0
  high = len(nums) - 1

  while low <= high:
    # Finding the mid using floor division
    mid = low + ((high - low) // 2)

    # Target value is present at the middle of the array
    if nums[mid] == target:
      return mid

    # Target value is present in the low subarray
    elif target < nums[mid]:
      high = mid - 1

    # Target value is present in the high subarray
    elif target > nums[mid]:
      low = mid + 1

  # Target value is not present in the array
  return -1


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