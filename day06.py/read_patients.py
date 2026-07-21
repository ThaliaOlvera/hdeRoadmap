import csv

with open("patients.csv", "r") as file:
    content = file.read()
    print(content)