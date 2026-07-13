#Function that calculates the area of a rectangle.

base=float(input("Introduce the base : "))
height=float(input("Introduce the height : "))

def area(base, height):
    return (base * height)

print("El área del rectángulo es:", area(base, height))