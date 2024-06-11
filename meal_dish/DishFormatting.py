import pandas as pd
import re
import os

def format_ingredient_name(name):
    name = re.sub(r'\s+', '-', name)
    name = re.sub(r'[/]', '-', name)
    name = re.sub(r'[()]', '', name)
    name = re.sub(r"'", '', name)
    name = re.sub(r'[-]+', '-', name)
    return name.lower().strip('-')

# Path to the Excel file (adjust the path as needed)
file_path = '/home/ujjwal/Dish_code_check_file.xlsx'

# Read the Excel file
dish_ingredient_nutrition = pd.read_excel(file_path, sheet_name='dish_ingredient_nutrition')

# Apply the formatting to the 'Raw Ingredient name' column
dish_ingredient_nutrition['Raw Ingredient name'] = dish_ingredient_nutrition['Raw Ingredient name'].apply(format_ingredient_name)

# Define the columns for the new DataFrame
columns = ['ID', 'Dish Name', 'ID (Ingredients)', 'Qty (Ingredients)', 'Unit (Ingredients)', 'Name (Ingredients)', 'Prep Method (Ingredients)']
dish_format = pd.DataFrame(columns=columns)

# Get the unique dish names
unique_dishes = dish_ingredient_nutrition['Dish name'].unique()

# Format the data for each dish
for dish in unique_dishes:
    dish_rows = dish_ingredient_nutrition[dish_ingredient_nutrition['Dish name'] == dish]
    for idx, row in dish_rows.iterrows():
        new_row = {
            'ID': '',
            'Dish Name': dish if idx == dish_rows.index[0] else '',
            'ID (Ingredients)': '',
            'Qty (Ingredients)': row['Quantity'],
            'Unit (Ingredients)': row['Unit'],
            'Name (Ingredients)': row['Raw Ingredient name'],
            'Prep Method (Ingredients)': ''
        }
        dish_format = pd.concat([dish_format, pd.DataFrame([new_row])], ignore_index=True)

# Define the output file path
output_file_path = '/home/ujjwal/Converted_Dish_Format.xlsx'

# Save the formatted DataFrame to an Excel file
dish_format.to_excel(output_file_path, index=False, sheet_name='Dish')

# Print the DataFrame to verify the result
print("Formatted DataFrame:")
print(dish_format)

# Since this script is to be run in a Frappe Bench environment,
# there's no need to include the code for uploading to Frappe.

