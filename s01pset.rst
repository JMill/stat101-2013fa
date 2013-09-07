{% import "macros/ork.jinja" as ork with context %}

PSet 01
**********

This PSet is for you to practice. Some questions from PSets may appear again on ESets and Exams. To aid you in your learning of statistics, do not look at the correct solutions (bottom of page) until you have made an effort to solve each problem.


[#]_ Variables with values that are determined by chance are called _____.

- random variables
- specialized
- erratic variables
- inconsistent variables


[#]_ Inferential statistics is based on probability.

- true
- false
- there is no relationship
- inferential statistics is based on the study of flux capacitors, pioneered by Dr. Brown.


----

Be sure to have read `SticiGui Ch 3, Frequency Tables <http://www.stat.berkeley.edu/~stark/SticiGui/Text/histograms.htm#frequency_tables>`_.  Gravity data are described right above this section; there are 100 observations. The 'frequency' in an interval is the number of observations in that interval. Exercise 3-6 will be useful for what follows.

`SticiGui Ch 3, Histograms <http://www.stat.berkeley.edu/~stark/SticiGui/Text/histograms.htm#histograms>`_

'Bins' = 'bars'. When you get the the end of the section, just before Skewness and Modes, find the heights of a couple of the bars in the gravity histogram. Three have been done for you in the text. You'll need the data from Exercise 3-6.

[#]_ The height of -10 to 20 bar = ______ % per unit

[#]_ The height of 20 to 50 bar = _____% per unit


----

A recent statistics exam yielded the following 25 scores. 

::

    61 90 79 57 63
    55 83 70 62 95
    90 83 41 72 85
    76 82 75 94 57
    72 72 46 81 93

I've started by setting up the class limits for a grouped frequency distribution, seen below. 

[#]_ Determine the values for the Frequency column.

=============   ==========
Class Limits    Frequency
=============   ==========
41-50           ?
51-60           ?
61-70           ?
71-80           ?
81-90           ?
91-100          ?
=============   ==========


[#]_ Given the following data set, find the approximate value that corresponds to the 75th percentile.

10, 44, 15, 23, 14, 18, 72, 56

The 75th percentile is ______.


[#]_ Using table below, what grade would a student who ranked in the 50th percentile receive?

======   =================    =========
Grade    Class Boundaries     Frequency
======   =================    =========
A        89.5-99.5            4
B        79.5-89.5            7
C        69.5-79.5            11
D        59.5-69.5            3
F        49.5-59.5            3
======   =================    =========

The student should receive a letter grade of ______.


[#]_ The average weight of adult male bison in a particular federal wildlife preserve is 1650 pounds with a standard deviation of 250 poinds. Find the weight of an adult bull whose z-score is -0.5.

The weight is _______ pounds.


----

Here is some income data:

============================= ======= ==================================
income (thousands of dollars) percent cumulative percent starting from 0
============================= ======= ==================================
0-10                          20      20
10-25                         28      48
25-50                         27      75
50-100                        18      93
100-150                       7       100
============================= ======= ==================================


[#]_ Find the 40th percentile in thousands of dollars. 

[#]_ Find the 'inter-quartile range'. That is, the distance between the 75th percentile and the 25th percentile. 

----

Do a few parts each of Exercises 3-9 and 3-10 in SticiGui.

|
|
|
|
|
|
|
|

Solutions
==============

.. [#] Random variables.
.. [#] True
.. [#] 0.47%. The height of a bar is equal to: relative frequency in the class interval/width of class interval. Therefore, the height of the -10 to 20 bar is 14/30 = 0.467% per unit.
.. [#] 0.1666666. The height of the 20 to 50 bar is 5/30 = 0.167% per unit.
.. [#] 
    The completed table should look like this:

    =============   ==========
    Class Limits    Frequency
    =============   ==========
    41-50           2
    51-60           3
    61-70           4
    71-80           6
    81-90           7
    91-100          3
    =============   ==========

.. [#] 
    44. Arranged data order:

    10, 14, 15, 18, 23, 44, 56, 72

    To find 75th percentile, count the number of items in the list (8) and multiply by 0.75.

    :math:`0.75 \cdot 8 = 6`

    The item in position 6 corresponds to the 75th percentile.

    So 44 corresponds to the 75th percentile.

.. [#] Letter grade of 'C'.
.. [#] 1525 pounds.
.. [#] 
    20.7. 

    The area between 0 and 10 is 20%, and so we need another 20% to get to 40%. The area of the 10-25 bar is 28%. Therefore, the 40th percentile must be somewhere in the 10-25 interval. Assuming uniform distribution, an estimate for the 40th percentile is :math:`10 + \frac{20}{28} (25-10) = 20.71` thousand dollars.

.. [#]
    37.3

    The interquartile range is equal to the differenc between the 75th percentile and the 25th percentile. First, compute the 75th percentile: the area between 0 and 50 is 75%; therefore, the 75th percentile is 50 thousand dollars. Next, the 25th percentile must be somewhere in the 10-25 interval. The estimate, after assuming uniform distribution, is :math:`10+\frac{5}{28}(25-10)=12.68` thousand dollars. Therefore, the interquartile range is equal to :math:`50-12.68 = 37.32` thousand dollars.
