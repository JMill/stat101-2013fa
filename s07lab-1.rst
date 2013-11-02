{% import "macros/ork.jinja" as ork with context %}

Sampling a Population
*******************************************

Lets say you've decided to be a nice person. You baked a batch of cookies for your friends and family. After pulling the cookies from the oven, it'd be a good idea to taste a cookie or two to make sure they are cooked well and that you didn't screw up the batter. By tasting a small subset of the batch, you can infer that if the cookies you tasted are good, the rest are probably good. In other words, you know with reasonable certainty that all the cookies you baked are tasty *without having to personally eat each one just to make sure*.  

Statisticians taste cookies all the time, sometimes literally but always figuratively. He or she study *samples*, analyzing a small piece of a much larger bunch.  Statisticians don't like being confused with bakers, however, so instead of talking about a 'bunch' or a 'batch', they refer to it as a *population*.

Just as the taste of one or two cookies gives you a good idea of the taste of a whole tray full of cookies, analysing a data sample can give you an idea of the greater population from which the sample was collected.

For example, suppose your family and friends claim that your cookies are really, really tasty, and that you should start a local bakery.  As the bakery's Baker In Chief, you need to determine what flavors to bake so you can win some customers. You have recipes for ten flavors, but it's too expensive right now to bake all ten flavors. You decide to offer a taste test of just three new cookie flavors. Since it would be very difficult to offer a taste test to **every** member of the community, you decide to make fifty cookies of one flavor, fifty of another, and fifty of a third flavor. Then, you walk around town giving away one cookie of each flavor to each random person you meet, and asking him/her to judge the tastes.

If the fifty random people who *sampled* your cookies are representative of the entire local community (the *population* who'd be served by your bakery), then you successfully used a small sample of people to *infer* the taste preferences of a much larger population.

.. NOTE::
     In everyday conversation and news reports, the word *population* refers to just living things, like the population of a city in Portugal or the population of blowfish in Japanese waters. However, in stats-land, the word *population* refers to just about any large collection of stuff, such as the population of sentences in a book, the population of all paperback books, or the population of humans who have read at least one book.


Using the Console
===========================

In order to show how you can easily collect samples of datasets, I will introduce you to an alternate way to explore data, using Python's *console*. You will see how to view data, perform statistics, and get results without having to type a bunch of code all at once, as you've done in previous exercises. Typing directly into the console is handy for experimenting with simple commands. Unlike when running long scripts (the .py files), the console tells you immediately if the computer can process the line of code you just typed.

On your computer, Python's console is located on the Canopy screen, below the word "Python", which is itself below where you've been typing in the scripts in prior exercises.

Yours may look a little different, but it probably shows something like ``In [1]`` or ``>>>``.  Regardless of the line's label, it conveys that you can *input* a command.  If the command you typed is error-free, any relevant *output* will be displayed beneath the command you just typed.

Lets play with the console to see how how sampling works. 


Samples and lists 
===========================

There are many techniques for collecting samples from a population.  We'll look at *interval* and *random* sampling.  

As mentioned earlier, there are ten cookie recipes but we can only afford to bake three flavors to offer as a taste test. I have a piece of paper here with several recipes on it. 

First, make a list of the flavors:

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['make data']|indent(4) }}
    
That's a list of five flavors. On a second piece of paper I have more flavor recipes:

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['forgot data']|indent(4) }}

Combine both lists into one big list of nine flavors.

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['combine data']|indent(4) }}

Oops, I forgot about my newest recipe, bacon-flavored cookies! Lets append that to the list, giving us ten total recipes.

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['append data']|indent(4) }}

Display all of the flavors. 

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['print data']|indent(4) }}

To review, do you remember what ``len()`` does? It counts how many items are in a list.

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['print-len']|indent(4) }}

We can thumb through the recipes in the list, picking a certain one. 

I like molasses cookies. I can choose molasses by specifying its position.

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['position0']|indent(4) }}

If you're curious about a bacon-flavored cookie, you can choose it by typing:

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['position9']|indent(4) }}

Try choosing other cookie flavors. Start by typing ``recipes[``, then input a number, and then end with a ``]``.

Why is it that the first recipe in our list, "molasses", is in position 0?

In Python, like many other programming languages, counting starts at 0, not 1 like you learned in school. Computers count like this: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, and so on. 

You can see this in action if you type

.. raw:: html

    {{ d['code/s07lab-1-01-listsamples.py|idio|pycon|pyg']['range10']|indent(4) }}

So how does ``recipes[0]`` mean "molasses" to the computer? Position 0 corresponds to the first item in any list.  To look up what value is in a specific position, in this case the 0th (pronounced "zero-th") position, put the 0 between a pair of brackets, [ and ].  The brackets act like crosshairs on a gun. You are setting sights on position 0. What's in position 0? "molasses".

Here are the positions for each recipe in our list:

============  ===========  ==========  =========  =====  =======  ====  ========  ======  =======  =====
Position #    0            1           2          3      4        5     6         7       8        9
------------  -----------  ----------  ---------  -----  -------  ----  --------  ------  -------  -----  
recipes =     molasses     gingersnap  chocolate  samoa  no bake  mint  do-si-do  peanut  oatmeal  bacon
============  ===========  ==========  =========  =====  =======  ====  ========  ======  =======  =====
