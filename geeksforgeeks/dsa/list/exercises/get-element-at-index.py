'''
https://practice.geeksforgeeks.org/batch/DS-With-Python/track/list-basic-python/problem/get-element-at-index

You are given an array arr(0-based indexing). The size of the array is given by n. You need to get the element at index i and return it. If no element exists at i then return -1.
'''


# User function Template for python3

def getByIndex(arr, n, idx):
    # return required ans
    if idx < n:
        return arr[idx]
    else:
        return -1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        idx = int(input())

        print(getByIndex(arr, n, idx))
# } Driver Code Ends