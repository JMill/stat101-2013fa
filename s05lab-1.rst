{% import "macros/ork.jinja" as ork with context %}

Lab 05-1 - The Birthday Paradox
*************************************

A fun statistical party trick is to perform The Birthday Paradox when you're with about thirty or more friends. Suppose we want to find the probability that, out of a group of thirty people, two people share a birthday. It's a classic problem in probability, with a surprisingly large answer.

Classically [#]_, the paradox can be approached like this: Pick people (and their birthdays) randomly, one at a time. We will keep track of the probability that there are no shared birthdays.

1. The first person can have any birthday, and there is still a 100% chance of no shared birthdays, since there is noone else with which to share. (It's lonely being alone.)
#. The second person has one chance of overlapping with the first person, so there is a :math:`\frac{364}{365}` chance of placing him/her without an overlap. The probability of no shared birthdays is :math:`\frac{364}{365}`.
#. The third person has two chances of overlapping with the first two people, so there is a :math:`\frac{363}{365}` chance of placing him/her without overlaps (two days are taken). The probability of no shared birtdays is now :math:`\frac{364}{365} \cdot \frac{363}{365}`.
#. The fourth person has three chances of overlapping with the first three people, so there is a :math:`\frac{362}{365}` chance of placing him/her without overlaps. The probability of no shared birthdays is now :math:`\frac{364}{365} \cdot \frac{363}{365} \cdot \frac{362}{365}`.
#. :math:`\dots`
30. The thirtieth person has 29 chances of overlapping with the first three people, so there is a :math:`\frac{336}{365}` chance of placing him/her without overlaps. The probability of having no shared birthdays is now :math:`\frac{364}{365} \cdot \frac{363}{365} \cdot \frac{362}{365} \cdot \dots \cdot \frac{336}{365}`.

The overall probability of no overlapping birthdays is then 0.294, giving a 71\% chance that at least one pair of people have overlapping birthdays. It's not too complex if you see the trick of keeping track of the probability of zero overlaps, rather than trying to add up the probabiilty of one or more overlaps. It also takes some thought to realzie that the probabilities are conditioned properly, so that multiplying together all the various :math:`P(N^{th} \text{ person doesn't overlap } \mid \text{ first } N - 1 \text{ people don't overlap } )` factors.


.. [#] The term *classic* refers to the use of probability notation and basic math to arrive at a solution, in fraction form. You learned about classic probability in the previous lecture sequence.


The Monte Carlo Approach
=======================================================

The solution for calculating the Birthday Paradox using the Monte Carlo Approach is to:

1. Pick 30 random numbers in the range [1, 365]. Each number represents one day of the year.
#. Check to see if any of the thirty are equal.
#. Go back to step 1 and repeat 10,000 times.
#. Report the fraction of trials that have matching birthdays.

Type this
-----------------

Create a new empty file in Canopy. Then type the following:

{{ ork.code('code/s05lab-birthdayparadox.py|pyg') }}

Save the file as *lab05-birthdayparadox.py* and run it.

Results
~~~~~~~~~~~~

Python's console should display a single statement::

	{{ d['code/s05lab-birthdayparadox.py|py']|indent(4) }}

Because this is a Monte Carlo experiment, your result may be slightly different. It's all due to chance. Run the script a couple more times to see how the ratio changes.


Stepping through the code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first command in our script is to get a random number generator, via ``import random``. Then we create two variables, ``NTRIALS`` for the number of trials, and ``NPEOPLE`` for the number of people in our simulated party. Running 10,000 trials is enough to get a reasonably accurate answer.  The line ``matches = 0`` is a *counter* -- it is a variable that we will continuously updatea to keep track of how many trials have matching birthdays. Next, we start a ``for`` loop to do a bunch of trials, tracking which birthdays have already been taken on the current trial. This is accomplished by initially creating a Python *dictionary* by typing ``taken = {}``. Python dictionaries are like special types of lists. We'll learn more about them later. After creating the ``taken`` dictionary for the current trial, the script then commences to generate random birthdays for each person at our party. On a randomly chosen day, ``day = random.randint(0, 365)``, the script checks to see if there is a match. If there is a match, we ``break`` from the current loop because there is no need to look for more than one match and waste our time. We wrap up by marking the specific birthday that is taken, and showing the user (us) the computed percentage of matching birthdays over 10,000 trials.

