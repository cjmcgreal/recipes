import re
import datetime

#%% Prod
def get_ingredients(recipe_markdown):
    # Regex pattern to match the ingredients (e.g., '2 cups of flour')
    pattern = r"- \*\*(\d+[\d\/]*)\s*(\w+)\*\* of (.*)"
    
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

def aggregate_ingredients(file_paths):
    aggregated_ingredients = {}

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            recipe_markdown = file.read()
            ingredients = get_ingredients(recipe_markdown)
            
            for ingredient in ingredients:
                key = ingredient['ingredient'].lower()  # Use a case-insensitive key
                if key in aggregated_ingredients:
                    # Update the quantity if needed or just append
                    aggregated_ingredients[key]['quantity'] += f" + {ingredient['quantity']}"
                else:
                    aggregated_ingredients[key] = ingredient

    return list(aggregated_ingredients.values())

#%% Dev
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

def get_shelf_life():
    # Extracting shelf life information using regular expressions
    shelf_life = re.findall(r"## Shelf Life\n([\s\S]+?)(?=\n##|\Z)", recipe_markdown)

    # Output Shelf Life info
    if shelf_life:
        print(f"Shelf Life Information: {shelf_life[0].strip()}")


if __name__ == "__main__":

    #%% test_get_ingredients
    recipe_markdown = 'Recipe Template.md'

    with open(recipe_markdown, 'r') as file:
        recipe = file.read()

    ingredients = get_ingredients(recipe)

    #%% test_aggregate_ingredients
    recipe_files = ['Recipe Template.md', 'Recipe Template 1.md']
    all_ingredients = aggregate_ingredients(recipe_files)
