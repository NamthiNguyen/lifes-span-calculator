# important information : there are 365 days in a year , 52 weeks in a year , 12 months in a year 
total_days = 365
total_weeks = 52
total_months = 12 
#grab users age 
current_age = input("What is your current age?")
desire_age = input("What is your desire age?")

#converting input from string to integer
user_current_age = int(current_age)
final_age = int(desire_age)

# need to caculate how many years left, days left, weeks left, month, left

# grab the year left 
year_left = final_age - user_current_age

#calculate the days left 
days_left = year_left * total_days

# calculate weeks left 
weeks_left = year_left * total_weeks

# calculate months left 
months_left = year_left * total_months

#store everything into a f-string 

final_calc = f"You have {days_left} days , {weeks_left} weeks, {months_left} months"

#print final calculation 
print(final_calc + " remember to use your time wisely")
