#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 17:05:19 2025

@author: conrad
"""
import re
from util import get_ingredients

# Sample markdown for testing
recipe_markdown = """
## Ingredients
- **1 lb** of boneless skinless chicken breast
- **1 pinch** of salt and pepper, to taste
- **2 tbsp** of olive oil
- **2 cups** of broccoli florets
- **1/2 count** of yellow bell pepper
- **1/2 count** of red bell pepper
- **1/2 cup** of baby carrots sliced
- **2 tsp** of minced ginger
- **2 count** of garlic cloves minced
- **1 count** of stir fry sauce
"""

# Step 1: Manually count how many ingredients there should be
expected_ingredient_count = 10

# Step 2: Run the 'parse_ingredients' function and count the returned ingredients
parsed_ingredients = get_ingredients(recipe_markdown)
parsed_ingredient_count = len(parsed_ingredients)

# Step 3: Assert that the two counts are equal
assert expected_ingredient_count == parsed_ingredient_count, f"Test failed: Expected {expected_ingredient_count} but got {parsed_ingredient_count}."

# If the assertion passes, print a success message
print(f"Test passed: {parsed_ingredient_count} ingredients correctly parsed.")
