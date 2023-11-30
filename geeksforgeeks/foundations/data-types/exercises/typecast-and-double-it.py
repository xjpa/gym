# https://practice.geeksforgeeks.org/batch/Python-Foundation/track/Python-Foundation-Data-Types/problem/typecast-and-double-it
# Given an input 
# Typecast it to int and double

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

def utility():
    # The line below takes the input
    num = input()

    # Complete the syntax below. Convert num to int and double it
    ans = int(num) * 2
    # Complete the syntax above

    # The line below prints the output
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