# Day 2 task
#Attempting on my own first

#2. Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# 3. Declare a first name variable and assign a value to it
# 4. Declare a last name variable and assign a value to it
# 5. Declare a full name variable and assign a value to it
# 6. Declare a country variable and assign a value to it
# 7. Declare a city variable and assign a value to it
# 8. Declare an age variable and assign a value to it
# 9. Declare a year variable and assign a value to it
# 10. Declare a variable is_married and assign a value to it
# 11. Declare a variable is_true and assign a value to it
# 12. Declare a variable is_light_on and assign a value to it
# 13. Declare multiple variable on one line

first_name = "John"
last_name = "Jones"
full_name = first_name + last_name
country = "UK"
city = "London"
age = 69
year = 1969
is_married = False
is_true = True
is_light_on = True

football_team, captain, position, table_position = "Arsenal", "Saka", "RW", 1

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(football_team))

print("---------------------")
print(len(first_name))

if len(first_name) > len(last_name):
    print("First Name is longer")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two

pi = 3.141592
R = 30
area_of_circle = pi * R**2
circum_of_circle = 2 * pi * R
R_user = input("Enter a Radius: ")
# R_user is now a string - Cast to int with int(VARIABLE)
user_area_of_circle = pi * (int(R_user)**2)
print(user_area_of_circle)

