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


# Tuples

# Declare a tuple of Canadian provinces.
canadian_provinces = ('Ontario', 'Quebec', 'British Columbia', 'Alberta')

print("Tuple of Canadian provinces:", canadian_provinces)
print(f"Data type of the tuple: {type(canadian_provinces).name}")



# Dictionaries

# Declare a dictionary for Canadian currency values.
currency_dict = {'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}

print("Dictionary of currency values:", currency_dict)
print(f"Data type of the dictionary: {type(currency_dict).name}")

# Modify values to use whole numbers.
for key in currency_dict:
    currency_dict[key] = int(currency_dict[key] * 100)

print("Modified dictionary of currency values:", currency_dict)

# Add loonie and toonie.
currency_dict['loonie'] = 100
currency_dict['toonie'] = 200

print("Dictionary with loonie and toonie:", currency_dict)




# Sets

# Declare a set of even numbers from 2 to 20.
even_numbers = set(range(2, 21, 2))

print("Set of even numbers:", even_numbers)
print(f"Data type of the set: {type(even_numbers).name}")

# Declare a set of multiples of 5 from 5 to 20.
multiples_of_5 = set(range(5, 21, 5))

print("Set of multiples of 5:", multiples_of_5)

# Declare a set containing unique values from both sets.
unique_values_set = even_numbers.union(multiples_of_5)

print("Set of unique values:", unique_values_set)

# Declare a set containing values in both sets.
intersection_set = even_numbers.intersection(multiples_of_5)

print("Set of values in both sets:", intersection_set)

# Declare a set containing values in the first set but not in the second set.
difference_set = even_numbers.difference(multiples_of_5)

print("Set of values in the first set but not in the second set:", difference_set)

# Declare a set containing values in the second set but not in the first set.
difference_set_2 = multiples_of_5.difference(even_numbers)

print("Set of values in the second set but not in the first set:", difference_set_2)