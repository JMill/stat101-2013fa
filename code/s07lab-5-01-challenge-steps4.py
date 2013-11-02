# 1. loads the 'random' module
import random

# 2. creates a list of ten cookie flavors
recipes = ['molasses', 'ginger', 'chocolate', 'samoa',
    'no bake', 'mint', 'sugar', 'peanut', 'oatmeal', 'bacon']

# 3. makes a copy of the list.
recipeCopy = recipes[:]

# 4. randomizes the list.
recipeRandom = random.sample(recipeCopy, 10)

# 5. slices the randomized list in half.
recipeHalf = recipeRandom[:6]

# 6. gets 3 interval samples from the sliced+random list.
sample = recipeHalf[::2]

# 7. prints the final list, you sample.
print sample
