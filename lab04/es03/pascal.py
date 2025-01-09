class PascalsTriangle:
    def __init__(self, steps):
        self.steps = steps
        self.triangle = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.steps >= 0:
            if not self.triangle:
                self.steps -= 1
                self.triangle.append(1)

                return self.triangle
            
            t = []

            for i in range(len(self.triangle) - 1):
                t.append(self.triangle[i] + self.triangle[i + 1])
            
            t.insert(0, 1)
            t.append(1)
            self.triangle = t
            self.steps -= 1

            return self.triangle
        else:
            raise StopIteration