# rec-01
Parse ingredients, dealing with preparation method.
- Ex: 1 lb chicken thighs, cut into 1 inch pieces
- ideal -> make suggestions, and user approves.

# rec-02
Print to pdf
- Organize by location in grocery store.
- Separately, organize by recipe - here, include preparation method.

# rec-03
Streamline import recipe:
- Ideally, just pass a url link (optimistic).
- Copy/paste ingredients and steps into parser, return some sort of recipe object.

# rec-04
Testing
- Review test_parse_ingredients. Now the expected ingredient count is manual. How can we make this automatic?
- Folder structure -> put all the test_*.py into a subfolder. 