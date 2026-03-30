Beta
====

The Beta distribution is a **continuous** probability distribution defined on the interval :math:`[0, 1]`.
It is most commonly used in Bayesian statistics to model uncertainty about a **probability** or a **proportion**
(such as a click-through rate, a success rate, or a coin's fairness).

Intuition:

- While the Binomial distribution counts successes, the Beta distribution models the **probability of success** itself.
- If you think of a probability :math:`p` as a random variable, the Beta distribution describes which values of :math:`p` are more or less likely based on prior knowledge or observed data.

What question does the Beta answer?
-----------------------------------

The Beta distribution answers the following core question:

Given that I have seen :math:`\alpha - 1` successes and :math:`\beta - 1` failures (or have equivalent prior belief),
what is the probability distribution over the unknown parameter :math:`p \in [0, 1]`?

Closed form (probability density function)
------------------------------------------

For :math:`x \in [0, 1]` and shape parameters :math:`\alpha > 0`, :math:`\beta > 0`:

.. math::

   f(x; \alpha, \beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}

where the denominator :math:`B(\alpha, \beta)` is the **Beta function**, which ensures the total area under the curve is 1.

Intuition (Alpha and Beta as "pseudo-counts")
---------------------------------------------

A very helpful way to think about the parameters :math:`\alpha` (alpha) and :math:`\beta` (beta) is as "counts" of observations:

- :math:`\alpha - 1`: The number of "successes" previously seen.
- :math:`\beta - 1`: The number of "failures" previously seen.

For example:

- ``Beta({a: 1, b: 1})`` is a **Uniform distribution** (0 successes, 0 failures; every value of :math:`p` is equally likely).
- ``Beta({a: 10, b: 10})`` is a symmetric bell-shaped curve centered at :math:`0.5`.
- ``Beta({a: 2, b: 8})`` is skewed toward low values (more failures than successes).

Constructor
-----------

``Beta({a: ..., b: ...})``

- ``a``: shape parameter 1 (alpha), real number ``> 0``
- ``b``: shape parameter 2 (beta), real number ``> 0``
- support: real numbers in ``[0, 1]``

Relationship to Binomial (Conjugacy)
------------------------------------

The Beta distribution is the **conjugate prior** for the Binomial likelihood. This is the core of simple Bayesian updating:

1. Start with a Prior: :math:`p \sim Beta(\alpha, \beta)`
2. Observe Data: Observe :math:`k` successes and :math:`n-k` failures in :math:`n` Binomial trials.
3. Compute Posterior: The updated distribution for :math:`p` is exactly :math:`Beta(\alpha + k, \beta + n - k)`.

Typical use cases
-----------------

- Modeling uncertainty about a success probability :math:`p`.
- Serving as a prior distribution for Bernoulli or Binomial observation models.
- Representing any continuous random variable that is strictly bounded between 0 and 1.

Executable example: basics (samples and score)
----------------------------------------------

.. literalinclude:: ../../examples/distributions/beta_basics.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/beta_basics.wppl --random-seed 0

Scoring
-------

``d.score(x)`` is the **log density** of the value ``x`` in ``[0, 1]``.

Because the Beta is a continuous distribution, ``score(x)`` represents the log of the Probability Density Function (PDF), not a discrete probability.

.. math::

   d.score(x) = (\alpha - 1) \log x + (\beta - 1) \log (1 - x) - \log B(\alpha, \beta)

Executable example: Bayesian updating
-------------------------------------

Story: We start with a "Flat" (Uniform) prior because we know nothing about a coin.
We then observe 8 heads out of 10 tosses. We use ``observe`` to see how our belief about the coin's fairness updates.

.. literalinclude:: ../../examples/distributions/beta_bayesian_update.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/beta_bayesian_update.wppl --random-seed 0