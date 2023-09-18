"""
Description: Assignment the second
Author:Shaganpreet Singh Sran
Date: September 17,2023
Usage: (Integrated cevelopment Environment)
"""

#constants(which python really do not have)
FEDERAL_TAX = 0.5
PI = 3.1456
absolute_value = abs(-15)
print('absolute value:', absolute_value)
print('absolute_value:'+ str(absolute_value))

print('absolute value:', abs(-15))

print("I am",'19','years old!')
print("apple","oranges","bananas", sep = "*")

#variables
Name = 'Shaganpreet singh sran'
age = 19
pi = 3.14159
number = 2046983126
is_a_student= True

print(type(Name))
print(type(age))
print(type(pi))
print(type(number))
print(type(is_a_student))

print(f"My name is { Name } and I am { age } years old.")
#output: My name is Shaganpreet singh sran and I am 19 years old.
print(f"The value of pi to two decimal places is {pi:2f}.")
#output: The value of pi to two decimal places is 3.14590.
print(f"The number is {number:05}")
#output The number is 2046983126
print(f"Hello,{Name:>30}")

#Type Conversion
age = 19
current_salary = 75000
age_and_salary = age + current_salary
print(age_and_salary, type(age_and_salary))
months_old = "3"
years_old = "19"

age = years_old 
print(age )