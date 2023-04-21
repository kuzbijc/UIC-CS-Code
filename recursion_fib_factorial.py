
def fibonacci(n):
    if n <= 1: # stopping condition
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""
f(4) = f(3) + f(2)
      = f(2) + f(1) + f(1) + f(0)
      = f(1) + f(0) + f(0) + f(0) + f(0)
      = 1 + 1 + 1 + 1 + 1
      = 5
"""
fibonacci(6)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n - 1)
"""
f(4) = 4*f(4-1)
     = 4*3...   
"""
factorial(6)

def palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    elif len(word) == 2:
        return True
    else:
        return palindrome(word[1:len(word)-1])
p = palindrome("kayak")
print(p)
