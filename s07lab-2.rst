{% import "macros/ork.jinja" as ork with context %}

A Sample of Lists
*************************************

This exercise follows directly from the previous. If you haven't already done so, create a list of ten cookie recipes.

.. raw:: html

    {{ d['code/s07lab-2-01-samplinglists.py|idio|pycon|pyg']['make list']|indent(4) }}
    
.. NOTE::
    When inputting the commmand above, after typing ``'samoa',``, I press the "Enter" key on the keyboard. The Python console automatically indents the next line, because it understands that I haven't finished typing in the rest of the list.

With our recipes in a list, lets start sampling the list in a couple different ways through the next several exercises.

Slicing
=========

You can choose to look at part of the list, such as only the first three items or the middle five items, for example. Looking at a section of a list is called *slicing*. I imagine it to be like slicing a stick of butter with a warm knife.

.. raw:: html

    {{ d['code/s07lab-2-01-samplinglists.py|idio|pycon|pyg']['slicing0']|indent(4) }}

In Python, slicing uses the 'crosshairs' notation, the left and right brackets (``[`` and ``]``), except instead of targeting a specific position, it's targeting all positions located between a starting position, such as ``0``, and *before* an ending position, such as ``4``. The start and end positions are separated by a ``:``, a colon. In practice, the command ``recipes[0:4]`` keeps the items in position 0, 1, 2, and 3, and tosses out the rest. Since "molasses", "ginger", "chocolate", and "samoa" are in positions 0 through 3, they form the slice.

Here are more ways of slicing our recipe list. After typing each command after the ``>>>``, press the Enter key to see Python's output. [#]_

.. raw:: html

    {{ d['code/s07lab-2-01-samplinglists.py|idio|pycon|pyg']['more slicing']|indent(4) }}
    
The last line, ``recipes[:]``, should look a bit strange to you. The command instructs Python to give you all the items that are between the start and the end. That is, the command gives the whole list back to us. This may sound dumb, but it's actually very useful when working with data, because it's a quick way to make a copy of your raw data, like this: ``newList = oldList[:]``. Then you can mess with the copy without accidentally disturbing the original data. It would be embarassing to lose one of our cookie recipes.

Instead of playing with slices, recall that we're supposed to be picking three cookie flavors for our community taste test. We could sample our recipe list by just taking a slice of any three sequential flavors. Lets sample the last three:

.. raw:: html

    {{ d['code/s07lab-2-01-samplinglists.py|idio|pycon|pyg']['last three']|indent(4) }}

We created a new variable, ``samples``, and stuffed into it a slice of our ``recipes`` list.  But how many items are in our sample?

.. raw:: html

    {{ d['code/s07lab-2-01-samplinglists.py|idio|pycon|pyg']['how many']|indent(4) }}

Peek inside ``samples`` to see what the items are:

.. raw:: html

    {{ d['code/s07lab-2-01-samplinglists.py|idio|pycon|pyg']['view sample']|indent(4) }}

So, we apparently got the last three items from our original recipe list, but how?  Lets dissect the command ``recipes[len(recipes) - 3:]``:

1. ``len(recipes)``. Whenever Python sees this, it counts how many items are in ``recipes`` (ten items), and puts an integer in its place.  So ``len(recipes)`` actually means ``10``.
#. ``len(recipes) - 3``. Python already knows ``len(recipes)`` is ``10``, so this line now looks like ``10 - 3``, which is ``7``.
#. Based on the above substitutions, the command now looks like ``recipes[7:]``. This instructs the computer to carve a slice out of the ``recipes`` list, from position 7 to the end.


Drill
=========
- What does the command ``recipes[:]`` do, as seen earlier in this exercise? Create a list of your three favorite song titles and call it ``myMusic``.  Remember to put each title in quotes as you construct the list.  Then type ``myMusic[:]``. What happened? 

.. [#] Remember, only type what follows the ``>>>`` on this page. You do not type "molasses", "ginger", or anything that isn't following the ```>>>```. Let the computer do the work, not you.
