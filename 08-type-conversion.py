# Data Types Conversion Demo

# take user input
grad_year = input("When do you graduate? ")
fav_class = input("What's your fav class? ")

#convert data types and do math
grad_year = int(grad_year)
years_till_grad = grad_year - 2022
years_till_grad = str(years_till_grad)

#give nice message to user
print("You get " + years_till_grad + " more years of " + fav_class)