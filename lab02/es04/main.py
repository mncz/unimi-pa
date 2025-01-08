from prime_sieve.array import PrimeArraySieve

def prime_factors(n):
    f, d = [], 2

    while n > 1:
        c = 0
        while n % d == 0:
            c += 1
            n /= d
        
        if c > 0:
            f.append([d, c])
        
        d += 1

        if d * d > n:
            if n > 1:
                f.append([int(n), 1])
            break
    
    return f

def is_practical(n):
    pf = prime_factors(n)

    if pf[0][0] != 2:   # Verifico che 2 sia un fattore primo, condizione 
        return False    # necessaria per i numeri pratici (numeri pari).
    if len(pf) == 1:    # Questo significa che 2 è l'unico fattore primo e 
        return True     # quindi è un numero pratico.
    
    for x in range(1, len(pf)):
        p1, _ = pf[x]
        t = 1

        for y in range(x):
            p, e = pf[y]

            if p != p1:
                # Calcola la somma dei divisori di x senza il fattore primo p1.
                t *= ((pow(p, (e + 1)) - 1) // (p - 1))
        
        if p1 > t + 1:
            # Se un fattore primo non verifica la condizione, allora x non è 
            # un numero pratico.
            return False
    return True

if __name__ == '__main__':
    limit = 10 ** 8
    sieve = PrimeArraySieve()
    primes = sieve.primes_in_range(1, limit)
    t, c, x = 0, 0, 1

    while True:
        p1, p2, p3, p4 = primes[x], primes[x + 1], primes[x + 2], primes[x + 3]
        x += 1

        if limit - p1 < 1000:
            # Se arriviamo alla fine dei nostri numeri primi, generiamo un 
            # altro set di 10^8 numeri.
            limit += 10 ** 8
            primes = sieve.primes_in_range(p1 + 1, limit)
            x = 0
        
        if (p4 - p3 == 6) and (p3 - p2 == 6) and (p2 - p1 == 6):
            # Trovate tre coppie sexy primi
            n = p1 + 9
            if all([is_practical(i) for i in [n - 8, n - 4, n, n + 4, n + 8]]):
                c += 1
                t += n
                if c == 4:
                    break
    
    print(t)