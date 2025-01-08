from shapes import (
    EquilateralTriangle,
    Circle,
    Rectangle,
    Square,
    Pentagon)

def main():
    shapes = [
        EquilateralTriangle(6),
        Circle(5),
        Rectangle(4, 11),
        Square(7),
        Pentagon(8)
    ]

    for s in shapes:
        print(s.calculate_area())
        print(s.calculate_perimeter())

if __name__ == '__main__':
    main()
