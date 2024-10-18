primecheck = (2, 3, 5, 7, 11)
def is_prime():
    i = 0
    while i in range(primecheck):
        if input % primecheck[i] == 0:
            return False
        else:
            i += 1
            if i > 5:
                return True
def print_primes():
    i = 0
    while i in range(primecheck):
        if input > primecheck[i]:
            print(primecheck[i], " ")
        else:
            break
def get_primes():
    i = 0
    while i in range(primecheck):
        if input > primecheck[i]:
            return primecheck[i]
        else:
            break

    
