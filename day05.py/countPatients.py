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

def bmi_clasification(bmi):
      if bmi <18.5:
           result ="underweight"
      elif bmi >= 18.5 and bmi <= 24.9:
           result ="normal weight"
      elif bmi >=25 and bmi <= 29.9:
           result ="overweight"
      elif bmi >=30 and bmi <= 34.9:
           result ="Class I Obesity"
      elif bmi >=35 and bmi <= 39.9:
           result ="Class II Obesity"
      elif bmi >=40:
           result ="lass III Obesity"
      else:
           print("Error")
      return result

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

user_info=input("Write de patient's name : ")
user_update=float(input("Write de new weight in kg: "))

def update_weight(user_info, new_weight):
    for patient in patients:
        if patient["name"].lower() == user_info.lower():
            patient["weight"]=new_weight
            patient["bmi"]= calculate_bmi(patient["weight"],patient["height"])
            patient["clasification"]=bmi_clasification(patient["bmi"])
            return patient
        

def calculate_bmi(weight,height):
        bmi= weight / (height*height)
        return round(bmi, 2)


def delete_patient(user_info):
    for patient in patients:
        if patient["name"].lower()==user_info.lower():
          user_response=input("Do you want to delete this patient?")
          if user_response.lower()== "yes":
               patients.remove(patient)
               return patient
          else:
               return None
    print("Patient not found")
    return None

deleted = delete_patient(user_info)

if deleted:
    print("Patient deleted successfully.")
else:
    print("Patient not found or deletion canceled.")

updated = update_weight(user_info,user_update)
print("Total patients is : ", get_total_patients(patients))

if updated:
    print(f"Weight: {updated['weight']} kg")
    print(f"BMI: {updated['bmi']} kg")
    print(f"BMI Clasification: {updated['clasification']}")
else:
    print("Patient not found.")

#print("The bmi averange is: ", bmi_averange())
#print("Max value bmi : ", max_bmi())
#print("Minimun value bmi : ", min_bmi())
