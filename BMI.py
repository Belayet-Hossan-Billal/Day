height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 14.5:
    print(f"your bmi is {bmi},you are underweight.")
elif bmi < 25:
    print(f"you bmi is {bmi},you are normal weight.")
elif bmi < 30:
    print(f"you bmi is{bmi},you are overweight.")
elif bmi <35:
    print(f"you bmi is {bmi},you are obese.")
else:
    print(f"you bmi is {bmi}you are clinically obese.")
