from util import generate_grocery_list_pdf

# Example ingredients list
ingredients = [
    {'quantity': '2', 'unit': 'cups', 'ingredient': 'flour'},
    {'quantity': '1', 'unit': 'cup', 'ingredient': 'sugar'},
    {'quantity': '1/2', 'unit': 'teaspoon', 'ingredient': 'salt'},
    {'quantity': '1', 'unit': 'cup', 'ingredient': 'olive oil'},
    {'quantity': '3', 'unit': 'eggs', 'ingredient': ''},
    {'quantity': '1', 'unit': 'teaspoon', 'ingredient': 'cinnamon'},
    {'quantity': '1/2', 'unit': 'teaspoon', 'ingredient': 'nutmeg'},
    {'quantity': '1', 'unit': 'cup', 'ingredient': 'water'},
    {'quantity': '1', 'unit': 'teaspoon', 'ingredient': 'vanilla extract'}
]

# Output file path
output_pdf_file = "grocery_lists/test/test_print_to_pdf.pdf"

# Generate the PDF
generate_grocery_list_pdf(ingredients, output_pdf_file)

print(f"PDF with grocery list has been created: {output_pdf_file}")
