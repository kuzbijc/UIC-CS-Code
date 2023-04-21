"""
RECURSION
function that calls itself inside its own function,
or "a call to intself"
this is subset of divide and conquer approach

divide:
dive the problem into a number of subproblems

conquer:
conquer the subproblems by solving them recursively

combine:
combine the solutions to subproblems in the solution
for the original problem

KEY COMPONENTS
-stopping condition
prevents recursive definitions from looping infinitely often

-a set of procedures that reduce all condtions toward the stopping condition

EX fibonacci sequence
f(0) = 1 # first stopping condition
f(1) = 1 # second stopping condition

f(n) = f(n-1) + f(n-2) (for all other n > 1)
so f(3) = f(2) + f(1)

EX factorial function
f(1) = 1 # stopping condition
f(n) = n*f(n-1)

EX palidrome
stopping conditions
word is empty or one char long, return true
first and last chars are different, return false
word consists of two equal char, return true

otherwise
remove first and last chars of word
pass it to function again


"""

