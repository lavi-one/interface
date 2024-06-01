# Copyright (c) 2024, LAVI and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


def Lavi_Dish_Ingredient_Nutrition_insert(doc, method):
    # Create a new document for Lavi_Dish_Ingredient_Nutrition
    new_ingredient_nutrition = frappe.get_doc({
        "doctype": "Lavi_Dish_Ingredient_Nutrition",
        "dish": doc.dish_name,
        "food_group": doc.food_group
    })
    
    # Iterate over the ingredients in the child table of doc
    for ingredient in doc.ingredients:
        # Fetch the nutrition values from Lavi_Ingredients_Nutrition
        nutrition = frappe.get_doc("Lavi_Ingredients_Nutrition", ingredient.name1)
        
        # Append ingredient details to the ingredients child table
        new_ingredient_nutrition.append("ingredients", {
            "name1": ingredient.name1,
            "qty": ingredient.qty,
            "unit": ingredient.unit,
            "prep_method": ingredient.prep_method
        })
        
        # Append values to tableone
        new_ingredient_nutrition.append("tableone", {
            "energy_kcal": nutrition.energy_kcal,
            "carbohydrates": nutrition.carbohydrates,
            "sugars": nutrition.sugars,
            "protein": nutrition.protein,
            "fibre": nutrition.fibre,
            "total_fat": nutrition.total_fat,
            "sat_fat": nutrition.sat_fat
        })
        
        # Append values to tabletwo
        new_ingredient_nutrition.append("tabletwo", {
            "cholestrol_mg": nutrition.cholestrol_mg,
            "sodium_mg": nutrition.sodium_mg,
            "mono_unsat_fat": nutrition.mono_unsat_fat,
            "poly_unsat_fat": nutrition.poly_unsat_fat,
            "calcium_mg": nutrition.calcium_mg,
            "iron_mg": nutrition.iron_mg
        })
    
    # Ignore permission checks
    new_ingredient_nutrition.flags.ignore_permissions = True
    # Insert the new document into the database
    new_ingredient_nutrition.insert()
    
    # Display a message indicating success
    frappe.msgprint(_("Dish and ingredients added with nutrition information"))
    
####################################################################################################################################################################  

def update_dish_nutrition(doc, method):
    # Fetch the Lavi_Dish_Ingredient_Nutrition document
    dish_ingredient_nutrition = frappe.get_doc("Lavi_Dish_Ingredient_Nutrition", doc.name)

    # Initialize sums for child table 1
    energy_kcal = 0.0
    carbohydrates = 0.0
    sugars = 0.0
    protein = 0.0
    fibre = 0.0
    total_fat = 0.0
    sat_fat = 0.0

    # Sum values from the first child table
    if dish_ingredient_nutrition.tableone:
        for row in dish_ingredient_nutrition.tableone:
            energy_kcal += float(row.energy_kcal or 0)
            carbohydrates += float(row.carbohydrates or 0)
            sugars += float(row.sugars or 0)
            protein += float(row.protein or 0)
            fibre += float(row.fibre or 0)
            total_fat += float(row.total_fat or 0)
            sat_fat += float(row.sat_fat or 0)

    # Initialize sums for child table 2
    cholestrol_mg = 0.0
    sodium_mg = 0.0
    mono_unsat_fat = 0.0
    poly_unsat_fat = 0.0
    calcium_mg = 0.0
    iron_mg = 0.0

    # Sum values from the second child table
    if dish_ingredient_nutrition.tabletwo:
        for row in dish_ingredient_nutrition.tabletwo:
            cholestrol_mg += float(row.cholestrol_mg or 0)
            sodium_mg += float(row.sodium_mg or 0)
            mono_unsat_fat += float(row.mono_unsat_fat or 0)
            poly_unsat_fat += float(row.poly_unsat_fat or 0)
            calcium_mg += float(row.calcium_mg or 0)
            iron_mg += float(row.iron_mg or 0)

    # Fetch or create the Lavi_Dish_Nutrition document
    dish_nutrition_name = frappe.db.exists("Lavi_Dish_Nutrition", {"dish": doc.dish})
    if dish_nutrition_name:
        dish_nutrition = frappe.get_doc("Lavi_Dish_Nutrition", dish_nutrition_name)
    else:
        dish_nutrition = frappe.get_doc({
            "doctype": "Lavi_Dish_Nutrition",
            "dish": doc.dish
        })

    # Update the Lavi_Dish_Nutrition document
    dish_nutrition.energy_kcal = energy_kcal
    dish_nutrition.carbohydrates = carbohydrates
    dish_nutrition.sugars = sugars
    dish_nutrition.protein = protein
    dish_nutrition.fibre = fibre
    dish_nutrition.total_fat = total_fat
    dish_nutrition.sat_fat = sat_fat
    dish_nutrition.cholestrol_mg = cholestrol_mg
    dish_nutrition.sodium_mg = sodium_mg
    dish_nutrition.mono_unsat_fat = mono_unsat_fat
    dish_nutrition.poly_unsat_fat = poly_unsat_fat
    dish_nutrition.calcium_mg = calcium_mg
    dish_nutrition.iron_mg = iron_mg

    dish_nutrition.flags.ignore_permissions = True
    dish_nutrition.save()

    frappe.msgprint(_("Dish nutrition values updated"))
    
####################################################################################################################################################################

def Lavi_Meal_Dish_Nutrition_insert(doc, method):
    # Create a new document for Lavi_Dish_Ingredient_Nutrition
    new_dish_nutrition = frappe.get_doc({
        "doctype": "Lavi_Meal_Dish_Nutrition",
        "select_meal": doc.name1,
        "food_group": doc.food_group
    })
    
    # Iterate over the ingredients in the child table of doc
    for dishs in doc.dish_information:
        # Fetch the nutrition values from Lavi_Dish_Nutrition
        nutrition = frappe.get_doc("Lavi_Dish_Nutrition", dishs.dish)
        
        # Append dish details to the dish child table
        new_dish_nutrition.append("dish_information", {
            "dish": dishs.dish,
            "serving_size": dishs.serving_size,
            "unit": dishs.unit,
        
        })
        
        # Append values to tableone
        new_dish_nutrition.append("tableone", {
            "energy_kcal": nutrition.energy_kcal,
            "carbohydrates": nutrition.carbohydrates,
            "sugars": nutrition.sugars,
            "protein": nutrition.protein,
            "fibre": nutrition.fibre,
            "total_fat": nutrition.total_fat,
            "sat_fat": nutrition.sat_fat
        })
        
        # Append values to tabletwo
        new_dish_nutrition.append("tabletwo", {
            "cholestrol_mg": nutrition.cholestrol_mg,
            "sodium_mg": nutrition.sodium_mg,
            "mono_unsat_fat": nutrition.mono_unsat_fat,
            "poly_unsat_fat": nutrition.poly_unsat_fat,
            "calcium_mg": nutrition.calcium_mg,
            "iron_mg": nutrition.iron_mg
        })
    
    # Ignore permission checks
    new_dish_nutrition.flags.ignore_permissions = True
    # Insert the new document into the database
    new_dish_nutrition.insert()
    
    # Display a message indicating success
    frappe.msgprint(_("Meal and Dishes added with nutrition information"))
    
#########################################################################################################################################################################################

def update_meal_nutrition(doc, method):
    # Fetch the Lavi_Dish_Ingredient_Nutrition document
    dish_ingredient_nutrition = frappe.get_doc("Lavi_Meal_Dish_Nutrition", doc.name)

    # Initialize sums for child table 1
    energy_kcal = 0.0
    carbohydrates = 0.0
    sugars = 0.0
    protein = 0.0
    fibre = 0.0
    total_fat = 0.0
    sat_fat = 0.0

    # Sum values from the first child table
    if dish_ingredient_nutrition.tableone:
        for row in dish_ingredient_nutrition.tableone:
            energy_kcal += float(row.energy_kcal or 0)
            carbohydrates += float(row.carbohydrates or 0)
            sugars += float(row.sugars or 0)
            protein += float(row.protein or 0)
            fibre += float(row.fibre or 0)
            total_fat += float(row.total_fat or 0)
            sat_fat += float(row.sat_fat or 0)

    # Initialize sums for child table 2
    cholestrol_mg = 0.0
    sodium_mg = 0.0
    mono_unsat_fat = 0.0
    poly_unsat_fat = 0.0
    calcium_mg = 0.0
    iron_mg = 0.0

    # Sum values from the second child table
    if dish_ingredient_nutrition.tabletwo:
        for row in dish_ingredient_nutrition.tabletwo:
            cholestrol_mg += float(row.cholestrol_mg or 0)
            sodium_mg += float(row.sodium_mg or 0)
            mono_unsat_fat += float(row.mono_unsat_fat or 0)
            poly_unsat_fat += float(row.poly_unsat_fat or 0)
            calcium_mg += float(row.calcium_mg or 0)
            iron_mg += float(row.iron_mg or 0)

    # Fetch or create the Lavi_meal_Nutrition document
    meal_nutrition_name = frappe.db.exists("Lavi_Meal_Nutrition", {"meal_name": doc.select_meal})
    if meal_nutrition_name:
        meal_nutrition = frappe.get_doc("Lavi_Meal_Nutrition", meal_nutrition_name)
    else:
        meal_nutrition = frappe.get_doc({
            "doctype": "Lavi_Meal_Nutrition",
            "meal_name": doc.select_meal
        })

    # Update the Lavi_meal_Nutrition document
    meal_nutrition.energy_kcal = energy_kcal
    meal_nutrition.carbohydrates = carbohydrates
    meal_nutrition.sugars = sugars
    meal_nutrition.protein = protein
    meal_nutrition.fibre = fibre
    meal_nutrition.total_fat = total_fat
    meal_nutrition.sat_fat = sat_fat
    meal_nutrition.cholestrol_mg = cholestrol_mg
    meal_nutrition.sodium_mg = sodium_mg
    meal_nutrition.mono_unsat_fat = mono_unsat_fat
    meal_nutrition.poly_unsat_fat = poly_unsat_fat
    meal_nutrition.calcium_mg = calcium_mg
    meal_nutrition.iron_mg = iron_mg

    meal_nutrition.flags.ignore_permissions = True
    meal_nutrition.save()

    frappe.msgprint(_("meal nutrition values updated"))
    
########################################################################################################################################################################
