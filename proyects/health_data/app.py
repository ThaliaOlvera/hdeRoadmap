# 1. Register patient 
# #2. Show registered patients 
# #3. Show average BMI 
# # 4. Show patient with higher BMI 
# #5. Go out 
# #6. Statistics 
# #7. Go out

patients = [
    {
        "name": "John Smith",
        "age": 45,
        "weight": 82,   # kg
        "height": 1.78, # meters
        "bmi": 25.9
    },
    {
        "name": "Emily Johnson",
        "age": 32,
        "weight": 68,
        "height": 1.65,
        "bmi": 24.9
    },
    {
        "name": "Michael Brown",
        "age": 54,
        "weight": 95,
        "height": 1.80,
        "bmi": 29.3
    },
    {
        "name": "Sophia Davis",
        "age": 29,
        "weight": 58,
        "height": 1.70,
        "bmi": 20.1
    }
]

user_menu_option1=input("Do you want")

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
        return round(bmi,2)


def register_patient(name, age, weight, height):
    bmi_fn = calculate_bmi(weight, height)
    patient_info = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "bmi": bmi_fn
    }
    return patient_info


patients=[]
patients.append(register_patient(userName, userAge, userWeight, userHeight))


def show_all_patients(patients):
    for idx, patient in enumerate(patients, start=1):
        print(f"Patient {idx}")
        for key, value in patient.items():
            print(key, value)

def get_total_patients(patients):
    return len(patients)


def bmi_averange():
    bmis=[patient["bmi"] for patient in patients ]
    return sum(bmis)/len(bmis)

def max_bmi():
    bmis=[patient["bmi"] for patient in patients ]
    return max(bmis)

def min_bmi():
    bmis=[patient["bmi"] for patient in patients ]
    return min(bmis)

print("The bmi averange is: ", bmi_averange())
print("Max value bmi : ", max_bmi())
print("Minimun value bmi : ", min_bmi())