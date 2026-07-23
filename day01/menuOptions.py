# Menú principal
print("Menú de opciones:")
print("1. Calcular IMC")
print("2. Convertir Celsius a Fahrenheit")

opcion = input("Elige una opcion (1 o 2): ")

if opcion == "1":
    weight = float(input());
    height = float(input());
    print(weight/(height*height));
elif opcion == "2":
    celsius=float(input());
    print(celsius*9/5+32);
else:
    print("No valid option")