#Calculate the percentage of body fat
#Deurenberg
#%Fat=(1.20×BMI)+(0.23×Age)−(10.8×Gender)−5.4 (Where Gender: Male = 1, Female = 2
                                                   
userAge=int(input());
userGender=(input());
userIMC=(float(input()));

if userGender == "Male":
    print((1.20*userIMC)+(0.23*userAge)-(10.8*1)-5.4)
else:
    print((1.20*userIMC)+(0.23*userAge)-(10.8*2)-5.4);