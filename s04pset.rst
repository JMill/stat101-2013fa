{% import "macros/ork.jinja" as ork with context %}

PSet 04
**********

This PSet is for you to practice. Some questions from PSets may appear again on ESets and Exams. To aid you in your learning of statistics, do not look at the correct solutions (bottom of page) until you have made an effort to solve each problem.


[#]_ If the probability of snow falling in Loretto tomorrow is 0.43, what is the probability that it will not snow tomorrow?

[#]_ If you were to toss a coin enough times, the number of heads and tails will tend to "even out." This is an example of the law of ___________.

[#]_ What is the probability of getting a sum less than 5 if two dice are rolled simultaneously.

[#]_ If a single card is drawn from an ordinary deck of cards, what is the probability of drawing a jack, queen, king, or ace?

[#]_ Below are listed numbers of engineers in various fields by sex. Choose one engineer at random. Find :math:`P ( \text{electrical} \mid \text{male} )`.

======= =========== =========== ===========
Sex     Mechanical  Electrical  Biomedical
======= =========== =========== ===========
Male    9601        4357        6318
Female  2039        1181        5168
======= =========== =========== ===========

[#]_ A certain system has two components. There are 9 different models of the first component and 12 different models of the second. Any first component can be paired with any second component. A salesperson must select 2 of the first component and 3 of the second to take on a sales call. How many different sets of components can the salesman take?  (Hint: Consider reviewing Section 11.2 (pp. 872-879) of `this text <http://www.cengage.com/resource_uploads/downloads/0534492770_65932.pdf>`_ for a review of permutations and combinations.)

|
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


.. [#] 0.57.  Use the "1 - ..." Rule, like this: :math:`1-0.43 = 0.57`.

.. [#] The law of large numbers, aka Bernoulli's Law.

.. [#] :math:`\frac{1}{6}`. Worked solution is below:

.. math::
    \begin{split}
        \left( P(1) \cdot P(1) \right) + \left( P(1) \cdot (2) \right) + \left( P(1) \cdot P(3) \right) &+ \left( P(2) \cdot P(2) \right) + \left( P(3) \cdot P(1) \right) + \left( P(2) \cdot P(1) \right) \\
         = \left( \frac{1}{6} \cdot \frac{1}{6} \right) + \left( \frac{1}{6} \cdot \frac{1}{6} \right) + \left( \frac{1}{6} \cdot \frac{1}{6} \right) &+ \left( \frac{1}{6} \cdot \frac{1}{6} \right) + \left( \frac{1}{6} \cdot \frac{1}{6} \right) + \left( \frac{1}{6} \cdot \frac{1}{6} \right) \\
         & = \frac{6}{36} \\
         & = \frac{1}{6}
    \end{split}

    
.. [#] :math:`\frac{4}{13}`. Worked solution is below: 

.. math::
	\begin{split}
		P(\text{jack}) + P(\text{queen}) &+ P(\text{king}) + P(\text{ace}) \\
		= \frac{4}{52} + \frac{4}{52} &+ \frac{4}{52} + \frac{4}{52} = \frac{16}{52} \\
		& = \frac{4}{13}	
	\end{split}

.. [#] :math:`P(\text{electrical} \mid \text{male}) = 0.215`. Worked solution below:

.. math::
	\begin{split}
		&\frac{ P(\text{electrical} \mid \text{male}) }{ P(\text{fields with males}) }\\
		&= \frac{ P(\text{electrical} \mid \text{male}) }{ P( \text{mechanical} \mid \text{male}) + P( \text{electrical} \mid \text{male})  + P( \text{biomedical} \mid \text{male}) } \\
		&=\frac{4357}{9601 + 4357 + 6318} \\
		&= 0.215
	\end{split}

.. [#] :math:`_9C_2 \cdot _{12}C_3 = 36 \cdot 220 = 7920`.
