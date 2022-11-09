#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    for i in range(k):
        tmp = k - i
        if s in t and tmp <= len(t[len(s):]):
            s += t[len(s)]
        else: 
            s = s[0:-1]
                  
    return 'Yes' if t == s else 'No'