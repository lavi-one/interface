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
file_path = '/home/ujjwal/Dish.xlsx'

# Read the Excel file
dish_ingredient_nutrition = pd.read_excel(file_path, sheet_name='Dish')

# Apply the formatting to the 'Dish Name' column and update the 'ID' column
dish_ingredient_nutrition['ID'] = dish_ingredient_nutrition['Dish Name'].apply(
    lambda x: format_ingredient_name(x) if pd.notna(x) else ''
)

# Define the output file path (overwrite the same file)
output_file_path = '/home/ujjwal/Dish.xlsx'

# Save the updated DataFrame to the existing Excel file
with pd.ExcelWriter(output_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    dish_ingredient_nutrition.to_excel(writer, index=False, sheet_name='Dish')

# Print the DataFrame to verify the result
print("Updated DataFrame:")
print(dish_ingredient_nutrition)

