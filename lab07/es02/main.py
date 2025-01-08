from collections import defaultdict

def goldbach(n):
    if n <= 2 or n % 2 != 0:
        return ()
    
    dif = defaultdict(int)
    mul, prm = [], []

    for i in range(2, n + 1):
        if i not in mul:
            prm.append(i)

            for j in range(i * i, n + 1, i):
                mul.append(j)
    
    for p in prm:
        if p in dif:
            return (p, dif[p])
        elif p * 2 == n:
            return (p, p)
        else:
            dif[n - p] = p

    return ()

def goldbach_list(n, m):
    d = defaultdict(list)

    for i in range(n, m + 1):
        if i % 2 == 0:
            d[i] = goldbach(i)
    
    return d

def main():
    print(goldbach(20))
    print(goldbach_list(4, 20))

if __name__ == '__main__':
    main()