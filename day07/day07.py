import pandas as pd

df = pd.read_csv("patients.csv")

#print(df.head())
#print(df.info())
#print(df.describe())
df.columns = df.columns.str.strip().str.lower()


#print(df["name"])
#print(df["weight"])
#print(df[["name", "age", "weight"]])

#older_patient = df[df["age"] > 30]
#print(older_patient)

#patients_overweight = df[df["weight"] > 75]
#print(patients_overweight)

#filtered = df[
 #   (df["age"] > 30 ) &
  #  (df["weight"] > 70)
#]

#print(filtered)

#average weight
#print(df["weight"].mean())

#averange age
#print(df["age"].mean())

#maximum weight
#print(df["weight"].max())

#minimum weight
#print(df["weight"].min())

#number of patients
#print(len(df))

df["bmi"] = df["weight"] / (df["height"] **2)
df["bmi"] = df["bmi"].round(2)
#print(df)

def classification(row):
    bmi = row["bmi"]
    
    if bmi < 18.5:
     return "Underweight"
    
    elif bmi >= 18.5 and bmi <= 24.9:
       return "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
       return "Overweight"
    elif bmi >= 30:
       return "Obesity"
    else:
       return "Something wrong"
    


df["classification"] = df.apply(classification, axis=1)
print(df)
