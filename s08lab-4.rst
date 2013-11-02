{% import "macros/ork.jinja" as ork with context %}

Random Sampling
************************************************************

Random sampling is the workhorse of statistics. It's a popular and generaly appropriate method. But why isn't it the *de facto* sampling method, relegating interval sampling and its kin to the annals of statistical nostalgia? Random is random is random, right? Wrong, unfortunately. 

In a sense, a random selection from a population provides a sensation of 'fairness'. Millionaire lotteries work on this principle, that so long as you have a ticket, you have a chance at winning. Yet, even a lottery's random selection can lead to events that *appear* unfair. Take for example, the rare event that one person wins two mega jackpots in as many years. It's common to hear claims of unfairness, luck, etc., but such events aren't particularly rare, statistically. 

In a later exercise you will also learn that a randomly chosen sample does not necessarily indicate that the sample is representative of the population. If you have a dumptruck that contains one strawberry and a mililon blueberries, there's a chance, however slight, that a single berry, picked at random, could be the strawberry.  Sampling a single random berry and having it be a strawberry produces a woefully inaccurate representation of the truck's berry contents.

Random
==============

Python has a built-in module, ``random``, for doing things randomly. (Recall how you used a different module, pylab, in previous exercises.)  In the console, ``import`` the ``random`` module.

.. raw:: html

    {{ d['code/s08lab-4-01-samplingrandom.py|idio|pycon|pyg']['import']|indent(4) }}

If the module loads properly, you will not see any output in the console. If you see an ``ImportError``, look for a typo.

When working with a module, Python uses a *dot notation*. It's like an address. If someone asked me where I live, I might reply, in dot notation, ``usa.pennsylvania``.  Pennsylvania is within the United States.

Python's ``random`` module contains many functions. You will use one, ``sample()``, in a moment. If you haven't already done so, create the recipe list again.

.. raw:: html

    {{ d['code/s08lab-4-01-samplingrandom.py|idio|pycon|pyg']['recipes']|indent(4) }}
    
Pick three recipes, randomly.

.. raw:: html

    {{ d['code/s08lab-4-01-samplingrandom.py|idio|pycon|pyg']['sample']|indent(4) }}
    
It's very unlikely your list of three recipes is the same as mine. (Though, of course, it is well within statistical possibility that you *did* get the same result as I.)  For fun, run the script again by pressing the "up arrow" key on your keyboard. Do this a couple times.

.. raw:: html

    {{ d['code/s08lab-4-01-samplingrandom.py|idio|pycon|pyg']['sample again']|indent(4) }}
    
Though generating random samples over and over would keep me entertained for at least five minutes, we should move on to more challenging things.
