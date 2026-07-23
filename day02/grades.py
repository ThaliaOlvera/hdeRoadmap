#Function that calculates the average of three grades.

print("Enter the first rating: ");
userRating1= int(input())
print("Enter the second rating: ");
userRating2= int(input())
print("Enter the third rating: ");
userRating3= int(input())

ratings=[userRating1,userRating2,userRating3];

def ratings_calculate():
    averange=((ratings[0]+ratings[1]+ratings[2])/len(ratings));
    return averange;


print("Your averange is: ",ratings_calculate());