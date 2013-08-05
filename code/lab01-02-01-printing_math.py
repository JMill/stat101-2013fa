print "I expected the average temp in PHX in May to be 80.0 F"
print "Based on the historical average it is actually %s F" % 93.6
print "This is a difference of %s degrees" % (93.6 - 80.0)
# I sure was off in my original estimate!

print "Lets convert 93.6 degrees Fahrenheit to Celsius."
print "I looked up an equation."
print "It says take the Fahrenheit value and subtract 32"
print "then divide everything by 1.8."

# This is your first *real* equation in Python.
93.6 - 32 / 1.80

print "Hmmm, why did the answer not display on the screen?"
print "Oh, because I forgot to 'print' the answer. Silly me."
print 93.6 - 32 / 1.8

print "Hmm, now the answer displays, but it's wrong."
print "Aha, I forgot to use ('s and )'s to group the equation"
print "just like in algebra class!"
print (93.6 - 32) / 1.8

print ""    # What does this line do?

print "Convert our temperature back to Fahrenheit."
print "Starting with Celsius value, multiply by 1.8, and add 32."
print "Now converting 34.222 C to F: %s" % (34.22 * 1.8 + 32)
print "It matches (close enough)!"
