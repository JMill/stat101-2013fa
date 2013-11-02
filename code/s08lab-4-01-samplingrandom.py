### @export "import"
import random

### @export "recipes"
recipes = ['molasses', 'ginger', 'chocolate', 'samoa',
    'no bake', 'mint', 'sugar', 'peanut', 'oatmeal', 'bacon']

### @export "sample"
random.sample(recipes, 3)

### @export "sample again"
random.sample(recipes, 3)
random.sample(recipes, 3)
random.sample(recipes, 3)
random.sample(recipes, 1)
random.sample(recipes, 8)

### @export ""
listOfCars = ['hidden']

### @export "list copy"
copyOfListOfCars = listOfCars[:]

### @export "intermediates"
list1 = ['Rover', 'Infiniti', 'Honda', 'Kia']
list2 = list1[::2]
list3 = random.sample(list2, 1)
