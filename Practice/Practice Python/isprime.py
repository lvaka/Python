#This function determines if the integer sent is a prime number
def is_prime(x):
    #1 is not a prime number so it is the first check and will return false
    if x == 1:
        return False
    #Loop will cycle through numbers 2-(x-1) and find the remainder.
    #If the remainder is 0, that means the number is not a prime.
    for n in range(2,x):
        if (x % n) == 0:
            return False
            break
    
    #If the above conditions are not met, then the number must be prime
    else:
        return True
