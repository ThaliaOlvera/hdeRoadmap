# Show all your information. 
# Count how many patients are registered. 
# Show BMI average. 
# Show the patient with the highest BMI.

patients_name=[
    "Alexander",
    "Sophia",
    "Liam",
    "Emma",
    "Noah",
    "Olivia",
    "Ethan",
    "Isabella",
    "Lucas",
    "Mia"
]

#Search for a patient by name. 

user_info=input("Search the patient name :")


def search_patient(user_info):
    return[name for name in patients_name if name.lower() == user_info.lower()]

result= search_patient(user_info)

if result:
    print(result)
else:
    print("There is no patient with this name")
