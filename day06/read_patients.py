import csv

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)
    
    patients=[]

    for patient in reader:
        patients.append(patient)
        

for patient in patients:
    print(f"Name: {patient['Name']}")
    print(f"Age: {patient['Age']}")
    print(f"Weight: {patient['Weight']}")
    print()
        


      

   

