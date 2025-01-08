class MathUtils:
    @staticmethod
    def static_add(a, b):
        return a + b
    
    def add(self, a, b: int):
        return a + b


def main():
    # Chiama direttamente il metodo statico
    print(MathUtils.static_add(1, 2))

    # Crea un'istanza della classe e chiama il metodo di istanza
    print(MathUtils().add(1, 2))

if __name__ == '__main__':
    main()