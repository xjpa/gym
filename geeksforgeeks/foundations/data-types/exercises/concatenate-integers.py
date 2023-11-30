# https://practice.geeksforgeeks.org/batch/Python-Foundation/track/Python-Foundation-Data-Types/problem/concatenate-integers
'''
Input:
a = 5
b = 6
Output:
56
Explanation: Concatenate them.
'''


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3


def utility():
    # The two lines below take input.
    a = int(input())
    b = int(input())

    # Complete the code below to concatenate a and b
    ans = str(a) + str(b)
    # Complete the code above to concatenate a and b

    # The line below prints the output.
    print(ans)


# {
# Driver Code Starts.

def main():
    t = int(input())
    while (t > 0):
        utility()
        t -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends