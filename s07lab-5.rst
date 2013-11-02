{% import "macros/ork.jinja" as ork with context %}

Cookie Sample Challenge
************************************************************

You can combine different sampling techniques in sequence to help mitigate the sampling bias. Statisticians do this all the time to ensure they aren't accidentally influencing the data and making the wrong decisions.

This exercise is called a Challenge, and rightfully so.  It's different than the previous exercises; I'm not going to show you a complete script and ask you to just type it into your computer. This time, I've provided below a list of sampling tasks.  You have to write a script that performs the tasks so that you minimize sampling bias in a batch of ten cookie flavors.

Write a script that:

1. loads the ``random`` module
#. creates a list of ten cookie flavors
#. makes a copy of the list.
#. randomizes the list.
#. slices the randomized list in half.
#. gets 3 interval samples from the sliced+random list.
#. prints the final list, your sample.

The sample displayed after running your script should contain three cookie flavors, like this (the specific flavors your computer generates will likely be different than mine)::

    {{ d['code/s07lab-5-01-challenge-steps4.py|py']|indent(4) }}

While the previous exercises have been performed in the console, your final script should be written in the space *above* the console. Save your script as "lab07-cookie_sample_challenge.py". 

Don't fret too much about writing a script all by yourself. Being a nice person at heart, I made it so you can combine bits of code from the past few exercises to make your new script.

While you have completed nearly all of the prescribed steps individually, you may have trouble 'synthesizing' it and getting the script to run properly. That's okay and common. Review past exercises, play with some test code, and make sure you can understand how to complete each step **on its own**. Then, slowly write the script one step at a time, running the script after each command you type to ensure the script is running and there are no typos. 

For example, write the command to complete the first step, run the program, and make sure there is no error.  If there is no error, add a command to complete the second step, run the program, and make sure there is no error. Repeat.

To help give you a nudge, below is a code skeleton. Open a new file with Canopy, type in the following code, and then add more code to make the program do what it is supposed to do.

{{ ork.code('code/s07lab-5-00-challenge-starter.py|pyg') }}



Hints
=======

- Use the following slicing trick to copy a list into a new variable.

.. raw:: html

    {{ d['code/s07lab-4-01-samplingrandom.py|idio|pycon|pyg']['list copy']|indent(4) }}

- Create new variables to hold intermediate lists.

.. raw:: html

    {{ d['code/s07lab-4-01-samplingrandom.py|idio|pycon|pyg']['intermediates']|indent(4) }}


After you have spent time solving the challenge (or trying but failing miserably -- that's okay), then review the solution below.

Solution
==============

To start tackling the challenge, I used the numbered steps as a coding guide, commenting-out the steps with the ``#`` symbol (called "hash", "pound", or "octothorpe").

**Phase 1**

{{ ork.code('code/s07lab-5-01-challenge-steps.py|pyg') }}

Next, below each commented line, I typed in the code to satisfy that specific step, testing the script after every command I wrote.

**Phase 2**

{{ ork.code('code/s07lab-5-01-challenge-steps2.py|pyg') }}

**Phase 3**

{{ ork.code('code/s07lab-5-01-challenge-steps3.py|pyg') }}

**Phase 4, the end**

{{ ork.code('code/s07lab-5-01-challenge-steps4.py|pyg') }}

Output::

    {{ d['code/s07lab-5-01-challenge-steps4.py|py']|indent(4) }}

    
Sampling Summary
======================

The approaches to sampling that you've seen so far get more useful as the amount of data increases. If you are given 100,000 records of political campaign donations, it may be unmanageable to review each one. But by sampling every 10th donation, for example, the number of donations through which to shift is reduced dramatically while still preserving much of the 'character' if the data. That is, the sample may be suitable enough for basic analysis. If you find something interesting with the sample, such as one political party receiving much more funding than another, you can then take more samples of the original data set to see if your finding holds true across all the samples, and the population as a whole. Statisticians call the concept of studying a sample to see if it applies to the whole *inferential statistics*. You can *infer* characteristics about a population by studying samples that are representative. This is both an art and a science, and is a field of statistics unto itself. 

You can perhaps infer that your recent batch of baked cookies are tasty by randomly sampling just a couple cookies, perhaps one from the edge of the pan and one from the center of the pan.

Just like it would be foolish to eat all of the cookies that you baked for other people, it's often infeasible to collect data on every person or thing that you want to study. 

Suppose you are interested in studying people diagnosed with schizophrenia. It would be a monumental task to try locating all schizophrenic people. Instead, what you or a medical researcher may do is to study schizophrenia people who are served by a particular hospital, and then carefully draw conclusions about the population as a whole. These conclusions may then be supported by a different researcher who studied schizophrenia at a different hospital.

.. BEWARE:
    No single sampling technique, whether interval, random, or whatever, is perfect or absolutely free of bias. If so, we'd all just use whichever one is best and forget about the rest. Different sampling techniques work better in different circumstances, and usually a mix of two or more techniques is best. 

    The ability to mitigate bias is an important skill for you to develop. It takes practice, but helps to lead to healthy 'statistical thinking'.

