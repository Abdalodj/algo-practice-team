#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    a = []
    i = 1
    x = 0
    while(i <= len(p)):
        tmp = p[x]
        if p[tmp - 1] == i:
            a.append(x+1)
            i += 1
            x = 0
        else:
            x += 1
        
    return a