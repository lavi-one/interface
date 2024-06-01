# Copyright (c) 2024, LAVI and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe import _  # Import the translation function


def Lavi_Dish_Ingredient_Nutrition_insert(doc, method):
    # Debugging: Check if _ is defined
    if '_' not in globals():
        frappe.msgprint("Translation function _ is not defined")
        return
    
    # Create a new document for Lavi_Dish_Ingredient_Nutrition
    new_ingredient_nutrition = frappe.get_doc({
        "doctype": "Lavi_Dish_Ingredient_Nutrition",
        "dish": doc.dish_name,
        "food_group": doc.food_group
    })
    # Ignore permission checks
    new_ingredient_nutrition.flags.ignore_permissions = True
    # Insert the new document into the database
    new_ingredient_nutrition.insert()
    
    # Display a message indicating success
    frappe.msgprint(_("Dish and ingredients added"))


