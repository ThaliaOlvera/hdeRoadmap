#Function that converts Celsius to Fahrenheit.

userNumber=int(input());

def celsius_to_fahrenheit(number):
    return ((number*9)/5+32);

print(celsius_to_fahrenheit(userNumber));