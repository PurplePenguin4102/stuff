def is_prime(n):
    """Return True if n is a prime number.

    is_prime(int) -> bool
    """
    
    for i in xrange(2, n+1):
        #Check if i is a factor of n
        if (n % i == 0) and (i < n):
            return False
        elif (n % i == 0) and (i == n):
            return True


def get_primes(n):
    """Return a list of the first n primes.

    get_primes(int) -> list(int)
    """
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def interact():
    
    n = int(raw_input("How many primes? "))
    primes = get_primes(n)
    if n == 1:
        print "The first prime is:", primes
    else:
        print "The first", str(n), "primes are:", primes

def find_functions(filename):

    fi = open(filename)
    text = fi.read()
    lines = text.splitlines()
    func = []

    for i,line in enumerate(lines):
        if line[:3] == "def":
            part = line.partition('(')
            name = part[0][4:]
            args = tuple(part[2][:-2].split(','))
            func.append((i,name,args))

    for e in func:
        print e
    return 
