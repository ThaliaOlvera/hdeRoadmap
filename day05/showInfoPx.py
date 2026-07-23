
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



user_info=input("Search the patient name :").strip()
def show_info(user_info):
    return[patient for patient in patients if patient["name"].lower()==user_info.lower()]

result= show_info(user_info)

if result:
    for patient in result:
     print(f"Name: {patient['name']}")
     print(f"Age: {patient['age']}")
     print(f"Weight: {patient['weight']} kg")
     print(f"Height: {patient['height']} m")
     print(f"BMI: {patient['bmi']}")
     print()
else:
    print("There is no patient with this name")


