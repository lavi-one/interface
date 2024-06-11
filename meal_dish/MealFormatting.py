import pandas as pd
import re
import os

def format_dish_name(name):
    # Replace spaces and slashes with hyphens, remove parentheses and single quotes
    name = re.sub(r'\s+', '-', name)  # Replace spaces with hyphens
    name = re.sub(r'[/]', '-', name)  # Replace slashes with hyphens
    name = re.sub(r'[()]', '', name)  # Remove parentheses
    name = re.sub(r"'", '', name)  # Remove single quotes
    name = re.sub(r'[-]+', '-', name)  # Replace multiple hyphens with a single hyphen
    return name.lower().strip('-')  # C
    
    
# Path to the Excel file (adjust the path as needed)
file_path = '/home/ujjwal/Meal_code_check_file.xlsx'

# Read the Excel file
meal_dish_nutrition = pd.read_excel(file_path, sheet_name='meal_nutrition')

# Apply the formatting to the 'Raw Ingredient name' column
meal_dish_nutrition['Dish name'] = meal_dish_nutrition['Dish name'].apply(format_dish_name)


columns = ['ID', 'Name', 'Portion Size', 'Serving Size','ID (Dish Information)','Dish (Dish Information)', 'Serving Size (Dish Information)', 'Unit (Dish Information)']
meal_format = pd.DataFrame(columns=columns)

unique_meal = meal_dish_nutrition['Meal name'].unique()
for meal in unique_meal:
    dish_rows = meal_dish_nutrition[meal_dish_nutrition['Meal name'] == meal]
    for idx, row in dish_rows.iterrows():
        new_row = {
            'ID': '',  # Leave ID blank
            'Name': meal if idx == dish_rows.index[0] else '',  # Keep Dish Name only for the first row of each dish
            'Portion Size': row['Portion size'],
            'Serving Size': row['Serving size (no)'],
            'ID (Dish Information)': '',  # Leave ID (Ingredients) blank
            'Dish (Dish Information)': row['Dish name'],
            'Serving Size (Dish Information)': '',
            'Unit (Dish Information)': '',
          }
        meal_format = pd.concat([meal_format, pd.DataFrame([new_row])], ignore_index=True)
        
        
# Define the output file path
output_file_path = '/home/ujjwal/Converted_Meal_Format.xlsx'

# Save the formatted DataFrame to an Excel file
meal_format.to_excel(output_file_path, index=False, sheet_name='meal')

# Print the DataFrame to verify the result
print("Formatted DataFrame:")
print(meal_format)

# Since this script is to be run in a Frappe Bench environment,
# there's no need to include the code for uploading to Frappe.

