### @export "make data"
flavors = ['molasses', 'ginger', 'chocolate', 'samoa', 'no bake']

### @export "forgot data"
moreFlavors = ['mint', 'sugar', 'peanut', 'oatmeal']

### @export "combine data"
recipes = flavors + moreFlavors

### @export "append data"
recipes.append('bacon')

### @export "print data"
recipes

### @export "print-len"
len(recipes)


### @export "position0"
recipes[0]

### @export "position9"
recipes[9]

### @export "range10"
range(10)

### @export "index chocolate"
recipes.index('chocolate')

### @export "position2"
recipes[2]
