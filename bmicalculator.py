'''
Name: Namthi Nguyen
course: The Complete Python Pro Bootcamp
Day 3 Exercise 2 - BMI 2.0
'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_calc = (weight / (height ** 2))
estimated_bmi = round(bmi_calc)

if estimated_bmi < 35:
    if estimated_bmi > 30:
        print(f"Your BMI is {estimated_bmi}, you are obese.")
    elif estimated_bmi > 25:
        print(f"Your BMI is {estimated_bmi}, you are slightly overweight.")
    elif estimated_bmi > 18.5: 
        
       print(f"Your BMI is {estimated_bmi}, you have a normal weight.")
       
    else: 
        print(f"Your BMI is {estimated_bmi}, you are underweight.")
else:
 print(f"Your BMI is {estimated_bmi}, you are clinically obese.")