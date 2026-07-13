#Function that determines if a person is of legal age.
print("Enter your age: ")
UserAge=int(input());

def legal_age(age):
    if age >= 18:
        print ("You have a legal age")
    elif age <18:
        print ("You don't have a legal age")
    else:
        print("Something wrong, introduce your age")
    return(age);

print(legal_age(UserAge));
    