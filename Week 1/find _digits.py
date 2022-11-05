#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    counter = 0
    for i in list(str(n)):
        try:
            if n % int(i) == 0:
                counter += 1
        except:
            pass
    
    return counter