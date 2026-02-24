Binomial
========

A Binomial distribution models the number of **successes** in :math:`n` independent trials,
where each trial is a Bernoulli event with success probability _math:`p`.

Intuition:

- One Bernoulli trial answers a yes/no question (``true/false``).
- A Binomial aggregates :math:`n` such trials and returns a **count** in :math:`\{0, 1, ..., n\}`.


What question does the Binomial answer?
---------------------------------------

The Binomial distribution answers the following core question:

If each individual in a population independently has a certain feature with probability :math:`p`
(e.g. "this email gets clicked", "this part is defective", "this person tests positive"),
then for a random sample of :math:`n` individuals, what is the probability that the feature is present in
**exactly** :math:`k` of them?

We write this as:

:math:`X \sim Binomial(n, p)` and ask for :math:`P(X = k)`.

Closed form (probability mass function)
---------------------------------------

For :math:`k = 0, 1, ..., n`:

.. math::

   P(X = k) = {n \choose k} p^k (1-p)^{n-k}

where

.. math::

   {n \choose k} = \frac{n!}{k!(n-k)!}

is the number of ways to choose which `:math:`k` of the :math:`n` trials are successes.

Intuition (why this formula is true)
------------------------------------

Think of :math:`n` independent Bernoulli trials (success probability ``p``).

1. Pick one *specific* sequence of outcomes that has exactly :math:`k` successes and :math:`n-k` failures,
   for example:

   ``S S F S F ...``

   Because the trials are independent:

   - the probability of the :math:`k` successes is :math:`p^k`
   - the probability of the :math:`n-k` failures is :math:`(1-p)^{n-k}`

   so the probability of this particular sequence is :math:`p^k (1-p)^{n-k}`.

2. Now count how many different sequences have exactly :math:`k` successes.
   This is purely combinatorial: you choose which :math:`k` positions (out of :math:`n`)
   are successes, so there are :math:`C(n,k) = {n \choose k}` such sequences.

3. These sequences are disjoint events, and each has the same probability
   :math:`p^k (1-p)^{n-k}`, so you multiply:

.. math::

   P(X = k) = {n \choose k} p^k (1-p)^(n-k).

This is why the Binomial is one of the most important distributions:
it is the canonical model for counts of "how many successes out of n independent tries?"


Constructor
-----------

``Binomial({p: ..., n: ...})``

- ``p``: success probability in ``[0, 1]``
- ``n``: number of trials (integer, ``n >= 1``)
- support: integers ``0..n``



Relationship to Bernoulli
-------------------------

A Binomial random variable can be understood as the sum of ``n`` Bernoulli trials.

In code, these two ideas align:

- One Bernoulli outcome: ``sample(Bernoulli({p: p}))`` → boolean
- Many trials + counting successes → integer count

Use ``Binomial`` when you only care about the **total number of successes**, not the individual trial outcomes.


Typical use cases
-----------------

- Counting successes in ``n`` independent Bernoulli trials (e.g. "how many clicks out of 10 emails?")
- Likelihood for count data via ``observe(Binomial(...), k)`` when you observe ``k`` successes out of ``n``


Executable example: basics (samples and score)
----------------------------------------------

.. literalinclude:: ../../examples/distributions/binomial_basics.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/binomial_basics.wppl --random-seed 0



Scoring
-------

``d.score(k)`` is the **log probability** of observing exactly ``k`` successes out of ``n``.

How does ``score(k)`` relate to the Binomial formula?
-----------------------------------------------------

Recall the Binomial probability mass function:

.. math::

   P(X = k) = {n \choose k} p^k (1-p)^{n-k}

WebPPL returns probabilities in **log space**. For ``d = Binomial({n: n, p: p})``:

- ``d.score(k)`` equals :math:`log P(X = k)` (natural log)
- therefore ``Math.exp(d.score(k))`` equals the ordinary probability :math:`P(X = k)`

Equivalently:

.. math::

   d.score(k) = \log {n \choose k} + k \log p + (n-k) \log (1-p)

This is convenient because very small probabilities remain representable as log values,
and you can always convert back with ``exp`` when you want human-readable probabilities.


Executable example: converting ``score(k)`` back to probability
---------------------------------------------------------------

.. literalinclude:: ../../examples/distributions/binomial_score_to_prob.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/binomial_score_to_prob.wppl --random-seed 0

Beyond :math:`P(X = k)`: CDF and tail probabilities
-----------------------------------------------

In practice you often want cumulative questions such as:

- :math:`P(X ≤ k)` ("at most k successes")
- :math:`P(X ≥ k)` ("at least k successes")

For a Binomial, these can be computed by summing the point probabilities:

.. math::

   P(X \le k) = \sum\limits_{i=0}^{k} P(X=i)

.. math::

   P(X \ge k) = \sum\limits_{i=k}^{n} P(X=i)

In WebPPL you can obtain :math:`P(X=i)` as ``Math.exp(d.score(i))`` and then sum over the desired range.


Executable example: CDF and tail probabilities
----------------------------------------------

.. literalinclude:: ../../examples/distributions/binomial_cdf_tail.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/binomial_cdf_tail.wppl --random-seed 0



A real-life example: estimating click-through rate (CTR) on a small grid
------------------------------------------------------------------------

Story: you send ``n = 10`` emails and observe ``k = 4`` clicks.
Assume clicks are independent with unknown click probability ``p`` (a Bernoulli success rate).
We place a discrete prior on a small candidate set for ``p`` and compute the posterior exactly using enumeration.

.. literalinclude:: ../../examples/distributions/binomial_ctr_posterior.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/binomial_ctr_posterior.wppl --random-seed 0

