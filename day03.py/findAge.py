patiens_age=[27,34,45,70,12,57,64,45,18,31]

def find_age():
    count=0
    positions=[]
    for age in range(len(patiens_age)):
        if patiens_age[age] == 45:
            count += 1
            positions.append(age)
    return (count,positions)

print("There is",find_age(),"persons with age 45")