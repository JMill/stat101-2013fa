### @export "make list"
recipes = ['molasses', 'ginger', 'chocolate', 'samoa',
    'no bake', 'mint', 'sugar', 'peanut', 'oatmeal', 'bacon']

### @export "slicing0"
recipes[0:4]

### @export "more slicing"
recipes[1:4]
recipes[0:]
recipes[:4]
recipes[0:len(recipes)/2]
recipes[:]


### @export "last three"
samples = recipes[len(recipes) - 3:]

### @export "how many"
len(samples)

### @export "view sample"
samples

### @export "sample safe"
recipeCopy = recipes[:]

"""

### @export "rest"
datacopy = data[:]
datacopy

datacopy.append(0)
datacopy
datacopy.sort()
datacopy

halfdata = data[:7]
halfdata

everyOther = data[0:13:2]
everyOtherAlt = data[::2]
everyOther
everyOtherAlt

sample = data[::5]
sample

import random
randomSample = random.sample(data, 4)
randomSample

range(5)

pretendData = range(165)
pretendData[:10]
pretendData[-10:]
pretendSample = pretendData[::20]
pretendSample
"""