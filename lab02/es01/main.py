import functools
import math

# Sum all the natural numbers below one thousand that are multiples of 3 or 5
result = functools.reduce(lambda i, j: i + j, [x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
print(result)

# Calculate the smallest number divisible by each of the numbers 1 to 20.
result = functools.reduce(lambda i, j: int((i * j) / math.gcd(i, j)), range(1, 21))
print(result)

# Calculate the sum of the figures of 2^1000
result = functools.reduce(lambda i, j: int(i) + int(j), list(str(2**1000)))
print(result)

# Calculate the first term in the Fibonacci sequence to contain 1000 digits
def fibonacci():
  a, b = 1, 1
  yield a, b

  while True:
    a, b = b, a + b
    yield b

result = next(j for _, j in enumerate(fibonacci(), start=1) if len(str(j)) == 1000)
print(result)
