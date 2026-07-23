patiens_age=[27,34,56,70,12,57,64,45,18,31]

for age in patiens_age:
    if age > 60:
        print (age)

def counter():
    count=0
    for age in patiens_age:
        if age >= 18:
            count += 1
    return count

print("There is : ", counter(), " legal age persons")



        
