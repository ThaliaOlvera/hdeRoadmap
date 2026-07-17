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


def get_total_patients(patients):
    return len(patients)

print("Total patients is : ", get_total_patients(patients))

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
