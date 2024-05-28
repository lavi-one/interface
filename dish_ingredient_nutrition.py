from frappe.ui.form import on

@on('Lavi_Dish_Ingredient_Nutrition', 'refresh')
def populate_ingredients(frm):
  if frm.doc.dish:
    frappe.db.get_list('Dish', {
      'filters': {'dish_name': frm.doc.dish},
      'fields': ['ingredients_list']
    }) \
    .then(data => {
      # Clear existing child table entries
      frm.doc.ingredients = []
      frm.refresh_field('ingredients');

      if (data && data.length) {
        const ingredients = data[0].ingredients;
        ingredients.forEach(ingredient => {
          frm.add_child('ingredients', {
            'name': ingredient.ingredient,  # Use 'name' for ingredient name
            'qty': ingredient.quantity,    # Use 'quantity' for quantity
            'unit': ingredient.size, # Use 'serving_size' for size
            'prep_method': ingredient.prep_method, # Use 'prep_method' for prep method
          });
        });
      }
    });

