def checkPalindrome(inputString):
    if inputString == ''.join(list(reversed(inputString))):
        return True
    else:
        return False
