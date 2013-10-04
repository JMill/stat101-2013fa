{% import "macros/ork.jinja" as ork with context %}

Lab 05 - Monte Carlo Experiments
*************************************

This lab extends the probability and simulation concepts you learned in Lab 04. For this lab, we will use the `Monte Carlo method <http://en.wikipedia.org/wiki/Monte_Carlo_method>`_ to write simulators of The Birthday Paradox and *The Monty Hall Show*. The Monte Carlo and Birthday Parodox content is based on content by `Greg Kochanski <http://kochanski.org/gpk>`_.

Introduction
===================

Monte Carlo simulations rely on repeated random sampling to obtain numerical results. In other words, by running simulations many, many times, we can calculate approximately the same probabilities as if we used our brains/math/probability to determine that we have a :math:`\frac{1}{36}` chance of rolling a die twice and getting {1, 2}. When the latter is too difficult, impossible, or we just want to double-check, we can perform a Monte Carlo experiment. The Monte Carlo method is akin to actually playing and recording your results in a real casino situation, hence the name.

The idea behind Monte Carlo simulations gained its name and its first major use in 1944, in research to develop the first atomic bomb. The scientists working on the Manhattan Project had intractably difficult equations to solve in order to calculate the probability with which a neutron from one fissioning Uranium (or Plutonium) atom would cause another to fission. At each step, the scientists could compute the probabilities that a neutron was absorbed, that it escaped from the bomb, or it strated another fission reaction. Researchers would pick random numbers, and, with the appropriate probabilties at each step, stop their simulated trajectories or start new chains from the fission reaction.

The brilliant insight, thanks to `Stanislaw Ulam <http://en.wikipedia.org/wiki/Stanislaw_Ulam>`_, was that the simulated trajectories would have identical statistical properties to the real neutron trajectories, so that the scientists could compute reliable answers for the important question, which was the probabibilty that a neutron would cause another fission reaction. All that had to be done was to simulate enough trajectories.

Ulam's method was called *Monte Carlo* by Nicholas Metropolis, named for the Monte Carlo Casino in Monaco, where Ulam's uncle regularly gambled.



It's time to build some Monte Carlo simulators! Complete the exercises below.

- `The Birthday Paradox <s05lab-1.html>`_
- `The Monty Hall Show <s05lab-2.html>`_

There is nothing to turn in for this lab. 
