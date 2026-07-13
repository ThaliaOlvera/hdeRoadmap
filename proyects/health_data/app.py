
#Register patient
userName=input("Introduce your name: ")
userAge=int(input("Introduce your age: "))
userWeight=float(input("Introduce your weight: "))
userHeight=float(input("Introduce your height: "))

def calculate_bmi(weight,height):
        bmi= weight / (height*height)
        print("BMI: ", round(bmi, 2))

        if bmi <18.5:
           print ("underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
           print ("normal weight")
        elif bmi >=25 and bmi <= 29.9:
           print ("overweight")
        elif bmi >=30 and bmi <= 34.9:
           print ("Class I Obesity")
        elif bmi >=35 and bmi <= 39.9:
           print ("Class II Obesity")
        elif bmi >=40:
           print ("Class III Obesity")
        else:
           print("Error")


def register_patient(name,age,weight,height):
    print("Patient: ", name)
    print("Age: ", age)
    calculate_bmi(weight,height)



register_patient(userName,userAge,userWeight,userHeight)

