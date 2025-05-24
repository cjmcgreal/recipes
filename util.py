import re
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import os

#%% Prod
def load_recipe(recipe_filename):
    # input validation - make sure it's markdown
    markdown_extensions = ['.md', '.markdown', '.mdown', '.mkd', '.mdtext', '.mdtxt']
    _, ext = os.path.splitext(recipe_filename)
    if ext.lower() in markdown_extensions:
        print('loading recipe')
    else:
        raise ValueError("Recipe must be in markdown format")
    
    # add 
    folder = "recipes"
    filepath = os.path.join(folder, recipe_filename)
    with open(filepath, 'r') as file:
        recipe_markdown = file.read()
    return recipe_markdown

def get_ingredients(recipe_markdown):
    # Regex pattern to match the ingredients (e.g., '2 cups of flour')
    # pattern = r"- \*\*(\d+[\d\/]*)\s*(\w+)\*\* of (.*)"
    # pattern = r"- \*\*(\d+[\d\/\s]*)\s*([\w\s]+)\*\* of (.*)"
    pattern = r"\*\*(\d+[\d\/\s]*)\s*([\w\s]+)\*\* of\s*(.*)"
    
    # Finding all matching ingredients
    ingredients = re.findall(pattern, recipe_markdown)
    
    # Structured ingredients list
    structured_ingredients = []
    
    for quantity, unit, name in ingredients:
        # Convert the quantity to a more structured format (you can expand this as needed)
        structured_ingredients.append({
            'quantity': quantity,
            'unit': unit,
            'ingredient': name.strip()
        })
    
    return structured_ingredients

def aggregate_ingredients(file_paths: list):
    aggregated_ingredients = {}

    for file_path in file_paths:
        recipe_markdown = load_recipe(file_path)
        ingredients = get_ingredients(recipe_markdown)
        
        for ingredient in ingredients:
            key = ingredient['ingredient'].lower()  # Use a case-insensitive key
            if key in aggregated_ingredients:
                # Update the quantity if needed or just append
                aggregated_ingredients[key]['quantity'] += f" + {ingredient['quantity']}"
            else:
                aggregated_ingredients[key] = ingredient

    return list(aggregated_ingredients.values())

def generate_grocery_list_pdf(ingredients, output_file):
    # Get today's date in the format: "Grocery List YYYY-MM-DD"
    today_date = datetime.today().strftime('%Y-%m-%d')
    header_text = f"Grocery List {today_date}"
    
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    
    # Title of the document
    c.drawString(72, height - 40, header_text)
    
    # Y position for the ingredients list (start from top, move down for each item)
    y_position = height - 80
    
    for ingredient in ingredients:
        # Draw the checkbox (check mark will be added later if checked)
        c.rect(72, y_position, 12, 12, stroke=1, fill=0)  # Drawing the checkbox
        
        # Draw the text for ingredient
        text = f"{ingredient['quantity']} {ingredient['unit']} - {ingredient['ingredient']}"
        c.drawString(92, y_position + 2, text)
        
        # Move down for the next item
        y_position -= 20
        
        if y_position < 72:  # If the text goes below the page, create a new page
            c.showPage()  # Start a new page
            c.setFont("Helvetica", 12)
            c.drawString(72, height - 40, header_text)
            y_position = height - 80
    
    # Save the PDF
    c.save()

def main(recipes: list):
    all_ingredients = aggregate_ingredients(recipes)

    # Output file path
    today_date = datetime.today().strftime('%Y-%m-%d')
    output_pdf_file = f"Grocery_list_{today_date}.pdf"

    # Generate the PDF
    generate_grocery_list_pdf(all_ingredients, output_pdf_file)

#%% Dev - aka untested
def get_cooking_log(recipe_markdown):
    # Extracting cooking log entries using regular expressions
    log_entries = re.findall(r"- \*\*\[(.*?)\]\*\*:\n\s*- \*\*Changes\*\*: (.*?)\n\s*- \*\*Outcome\*\*: (.*?)\n\s*- \*\*Observations\*\*: (.*)", recipe_markdown)

    # Output Cooking Log
    for entry in log_entries:
        date_str, changes, outcome, observations = entry
        date = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"Date: {date.strftime('%B %d, %Y')}")
        print(f"Changes: {changes}")
        print(f"Outcome: {outcome}")
        print(f"Observations: {observations}\n")

def get_shelf_life(recipe_markdown):
    # Extracting shelf life information using regular expressions
    shelf_life = re.findall(r"## Shelf Life\n([\s\S]+?)(?=\n##|\Z)", recipe_markdown)

    # Output Shelf Life info
    if shelf_life:
        print(f"Shelf Life Information: {shelf_life[0].strip()}")

#%% run all as test, then run main
if __name__ == "__main__":

    # test_get_ingredients
    recipe_filename = 'Shakshuka.md'
    recipe = load_recipe(recipe_filename)
    ingredients = get_ingredients(recipe)

    # test_aggregate_ingredients
    recipe_files = ['Recipe Template.md', 'Recipe Template 1.md']
    all_ingredients = aggregate_ingredients(recipe_files)
    
    # main
    main(recipe_files)
