# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    state = -1
    energy = 100
    jump = 0
    while(state != 0):
        jump = (jump + k) % len(c)
        if c[jump] == 0:
            energy -= 1
        if c[jump] == 1:
            energy = energy - 3
        
        state = jump
        
    return energy