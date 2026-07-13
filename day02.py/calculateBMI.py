#Function that calculates BMI.
userWeight=float(input("Enter your weight in kg: "));
userHeight=float(input("Enter your height in meters: "));

def bmi(weight, height):
    return float(weight/(height*height));


print("Your bmi is: ", bmi(userWeight,userHeight));