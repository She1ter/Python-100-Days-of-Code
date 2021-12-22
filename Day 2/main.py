# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#90 years it is:
years_left = 90 - int(age)
days = 365 * years_left
weeks = 52 * years_left
month = 12 * years_left

print(f"You have {days} days, {weeks} weeks, and {month} months left.")
