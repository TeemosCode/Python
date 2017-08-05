#codecademy python practice
#is_prime number (質數判定)
'''
Define a function called is_prime that takes a number x as input.
For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False.
If none of them are, then return True.
'''

def is_prime(x):
    if x > 1:
        for n in range(2,x):
            if x != 2 and x % n == 0 :
                return False
        else:
            return True
    else:
        return False
