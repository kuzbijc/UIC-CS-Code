
def mult():
    print(sum([n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0]))

def even_fib():
    a = 1
    b = 2
    s = 0
    for i in range(7):
        if a % 2 == 0:
            s += a
            print(a) # even ints
        c = a + b
        a = b
        b = c
    print(s) # sum of even ints

def largest_prime():
    l = []
    for num in range(2,2000000):
        prime = True
        for i in range(2,num):
            if num % i == 0:
                prime = False
        if prime:
            l.append(num)
    print(max(l))

def largest_palindrome_product():
    print([i for i in range(100,1000)])

def smallest_mult():
    n = 1
    l = [1,2,3,4,5,6,7,8,9,10]

def sum_square_diff():
    a = sum([e**2 for e in range(1,101)])
    b = sum([e for e in range(1,101)])**2
    print(b - a)

#def ten_thou_prime():

def prod_series(n):
    l = []
    for i in range(1,len(n)):
        if i % 12 == 0:
            l.append(int(n[i])*int(n[i-1])*int(n[i-2])*int(n[i-3])*int(n[i-4])*int(n[i-5])*int(n[i-6])*int(n[i-7])*int(n[i-8])*int(n[i-9])*int(n[i-10])*int(n[i-11])*int(n[i-12]))
    print(max(l))

def pyth_triplet():
    print([[a,b,c] for a in range(1000) for b in range(1000) for c in range(1000) if a < b and b < c and a**2 + b**2 == c**2 if a + b + c == 1000])

def sum_primes():
    l = []
    for num in range(2,20):
        prime = True
        for i in range(2,num):
            if num % i == 0:
                prime = False
        if prime:
            l.append(num)
    print(sum(l))

#def largest_prod_grid():

def tri_numbers(n):
    s = 0
    l = []
    l2 = []
    d = {}.fromkeys(l)
    for i in range(1,n):
        s += i
        l.append(s)
    for e in l:
        for j in range(1,e+1):
            if e % j == 0:
                l2.append(e)
    l3 = [l2.count(e2) for e2 in set(l2)]
    l4 = list(set(l2))
    for e2 in l3:
        if e2 >= 500:
            ind = l3.index(e2)
            print(l4[ind])
        else:
            print("not large enough number")

def collatz_sequence(n):
    l = []
    l.append(n)
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3*n) + 1
        l.append(n)
    print(len(l))
                
def main():
    #mult()
    #even_fib()
    #largest_prime()
    #largest_palindrome_product() # !!!
    #smallest_mult() # !!!
    #sum_square_diff()
    #ten_thou_prime() # !!!
    n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    #prod_series(n)    
    #pyth_triplet() # takes 3 mins
    #sum_primes()
    #largest_prod_grid()
    #tri_numbers(20000)
    collatz_sequence(13)

main()
