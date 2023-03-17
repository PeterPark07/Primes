# Lists primes until a certain number

def list_primes(until):
    # Create a list of True values representing numbers 0 to limit
    primes = [True] * (until + 1)
    # Mark 0 and 1 as non-prime
    primes[0] = primes[1] = False
    # Loop over all numbers up to sqrt(limit)
    for i in range(2, int(until ** 0.5) + 1):
        if primes[i]:
            # Mark all multiples of i as non-prime
            for j in range(i*i, until+1, i):
                primes[j] = False
    # Return a list of all prime numbers
    return [i for i in range(2, until+1) if primes[i]]
