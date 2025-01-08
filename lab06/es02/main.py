class MyMath:

    def fib(self, n):
        return 1 if n <= 1 else self.fib(n - 1) + self.fib(n - 2)

    def fact(self, n):
        return 1 if n <= 1 else n * self.fact(n - 1)

    def taylor(self, n):
        pass