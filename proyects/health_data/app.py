# 1. Registrar paciente
# 2. Mostrar pacientes registrados
# 3. Mostrar promedio de IMC
# 4. Mostrar paciente con mayor IMC
# 5. Salir


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


def register_patient(name,age,weight,height):
    bmi_fn=calculate_bmi(weight,height)
    patientInfo=[name,age,weight,height,bmi_fn]
    return patientInfo


patients=[]
patients.append(register_patient(userName, userAge, userWeight, userHeight))

print("Patient information: ", patients)