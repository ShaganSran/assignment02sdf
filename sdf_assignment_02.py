"""
Description: Created assignment 2
Author: Shaganpreet singh sran
Date: September 17, 2023
Usage: sdf assignment 2
"""

# Simple data types

# Declare a variable to store a name and initialize it to your first name.
first_name = "Shagan"

print(f"value: {first_name} type: {type(first_name).name}")

# Declare a variable for Manitoba Driver's License status and initialize it.
manitoba_license_status = True  

print(f"value: {manitoba_license_status} type: {type(manitoba_license_status).name}")

# Declare a variable to store the current year and initialize it.
current_year = 2023


print(f"this year: {current_year} type: {type(current_year).name}")

# Add 1 to the year.
current_year += 1

print(f"next year: {current_year} type: {type(current_year).name}")

# Performing Calculations

# Declare constants for GST and PST rates.
GST_RATE = 0.08  
PST_RATE = 0.16  

# Declare a variable for the vehicle price and initialize it.
vehicle_price = 100000.00  

# Calculate GST and PST taxes.
gst_tax = vehicle_price * GST_RATE
pst_tax = vehicle_price * PST_RATE

# Calculate the total cost including taxes.
total_cost = vehicle_price + gst_tax + pst_tax

print(f"pre-tax value: {vehicle_price} PST: {pst_tax} GST: {gst_tax} total: {total_cost}")

print(f"pre-tax value: ${vehicle_price:.2f} PST: ${pst_tax:.2f} GST: ${gst_tax:.2f} total: ${total_cost:.2f}")

# Lists

# Declare a list of numbers from 1 to 10.
numbers_list = list(range(1, 11))

print(f"Data type of the list: {type(numbers_list).name}")

print("List of numbers:", numbers_list)

# Add your first name to the list between values 5 and 6.
numbers_list.insert(5, first_name)

print("Updated list:", numbers_list)

# Remove the number 9 from the list.
numbers_list.remove(9)

print("List after removing 9:", numbers_list)

# Create a second list.
second_list = ['A', 'B', 'C']

# Create a third list containing values from the first and second lists.
combined_list = numbers_list + second_list

print("Combined list:", combined_list)



