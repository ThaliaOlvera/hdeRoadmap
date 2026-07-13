#Function that determines if a number is even.
print("Introduce a number :");
userNumber=int(input());

def identifier(num):
    if num % 2 == 0:
        print ("Your number is even")
    else:
        print("Your number is odd");
    return;

identifier(userNumber);
