{% import "macros/ork.jinja" as ork with context %}

Sampling Intervals
************************************

You should have the list of ten cookie flavors from the previous exercises. If not, type this

.. raw:: html

    {{ d['code/s08lab-3-01-samplinginterval.py|idio|pycon|pyg']['make list']|indent(4) }}

In the previous exercise, you saw how to carve out a specific sample from our recipe list. This was a dangerous way to collect a sample, because I, as the instuctor and cookie connoisseur, deliberately influenced the sampling. Why would I do that? Because I really like peanut, oatmeal, and bacon cookies, and wanted to make sure we baked those flavors for our community taste test. That was quite rotten of me, huh?

You have to watch out for events like this, in which someone consciously or unconsciously influences the sampling. By influencing the sampling to get the flavors I wanted to offer for the upcoming community taste test, I may not have caused any real trouble. However, there's the chance that by picking *my* favorite flavors, I have risked us in getting unreliable results for the community taste test.  Maybe I'm the only person in the region who likes peanut, oatmeal, or bacon cookies. Our new bakery may fail because we aren't providing the cookie flavors the community, as a whole, wants.

Researchers hate it when their samples or results are *biased*, intentionally or not. So they have devised techniques to reduce the risk of introducing bias.

One bias-busting approach is to collect a sample based on an arbitrary interval, such as choosing every third item in a list.

This is easy to do.

List Intervals
=====================

Before we sample the recipe list, lets see how intervals work on a list of numbers.

First, here's a short review of ``range()``:

.. raw:: html

    {{ d['code/s08lab-3-01-samplinginterval.py|idio|pycon|pyg']['range review']|indent(4) }}

``range(5)`` creates a list of five numbers, counting from the first number, 0, to the fifth number, 4. (Remember, computers count differently than humans.)

Now, lets create *pretend data*: 165 numbers in a single list.

.. raw:: html

    {{ d['code/s08lab-3-01-samplinginterval.py|idio|pycon|pyg']['pretend data']|indent(4) }}

The variable ``pretendData`` holds a list, which, in turn, holds a bunch of sequential numbers from 0 to 164. This should be conceptually easy for you by now. If not, play with ``range()``, variables, and lists some more, then come back here.

Next, lets say that we need to amass a sample of nine or ten values from our big list of numbers. We can use an interval to achieve this.

.. raw:: html

    {{ d['code/s08lab-3-01-samplinginterval.py|idio|pycon|pyg']['interval10']|indent(4) }}

The interval worked well, choosing every 10th item in the list. But how many items are in our sample?

.. raw:: html

    {{ d['code/s08lab-3-01-samplinginterval.py|idio|pycon|pyg']['interval10len']|indent(4) }}

Oops, too many items. Lets try again by tweaking the interval amount.

.. raw:: html

    {{ d['code/s08lab-3-01-samplinginterval.py|idio|pycon|pyg']['interval20']|indent(4) }}

Choosing every 20th item gives us nine items in our sample, which was our goal. We are done.

In a more advanced exercise you will see how using a sampling interval can help make data analysis much easier, particulary when dealing with thousands, or even hundreds of thousands, of items. Since any computers have difficulty processing so much data, studying the data in intervals is a convenient way to 'get a feel' for the data without causing the computer to suffer from *too much* data.

Interval testing is especially common in assembly line environments, such as testing every fifth robot toy that comes off the line to ensure the toy will fulfill its goal of delivering mechanized joy to a young girl or boy.
