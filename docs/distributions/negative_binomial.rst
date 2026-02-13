Negative Binomial
=================

The negative binomial distribution is one of the most important discrete distributions.
It models a count with **more variability than a Poisson** (overdispersion), and it also has a clean
"waiting time" interpretation in terms of Bernoulli trials.

Important note (WebPPL)
-----------------------

WebPPL does not provide a built-in primitive constructor named ``NegativeBinomial``.
In this reference we therefore show:

1) how to *sample* a negative-binomially distributed value using ordinary WebPPL code, and
2) how to use the negative binomial as a *likelihood* via ``factor(logp)`` during inference.

Definition (waiting time)
-------------------------

Fix two parameters:

- ``r``: the target number of **successes** (integer, ``r >= 1``)
- ``p``: success probability in each Bernoulli trial (real, ``0 < p <= 1``)

Run independent Bernoulli trials with success probability ``p`` until the ``r``-th success occurs.
Let ``K`` be the number of **failures** observed before that ``r``-th success.

Then:

``K ~ NB(r, p)``

Support: ``K ∈ {0, 1, 2, ...}`` (infinite support).


PMF (probability mass function)
-------------------------------

For ``k = 0, 1, 2, ...``:

.. math::

   P(K = k) = \binom{k + r - 1}{k} (1-p)^k p^r

Intuition (combinatorics)
-------------------------

To have exactly ``k`` failures before the ``r``-th success:

- the final trial must be a success (the ``r``-th success),
- among the first ``k + r - 1`` trials, we need exactly ``k`` failures and ``r-1`` successes.

The number of ways to place ``k`` failures among ``k + r - 1`` positions is
``C(k+r-1, k)``. Each such sequence has probability ``(1-p)^k p^r`` by independence.
Multiplying gives the PMF above.

Parameterization gotchas
------------------------

Different sources use different conventions. This page uses:

- ``K`` = number of **failures** before the ``r``-th success
- ``p`` = probability of **success** in each trial

A common alternative is to return the **total number of trials** ``T = K + r``.
(So be careful when comparing to libraries that define the negative binomial in terms of ``T``.)

Special case: Geometric
-----------------------

When ``r = 1``, the negative binomial becomes the geometric distribution over
"failures before the first success":

.. math::

   P(K = k) = (1-p)^k p

In other words, ``NB(1, p)`` is geometric in this parameterization.

How to use it in WebPPL
-----------------------

Sampling (waiting-time simulation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can sample ``K`` directly by simulating Bernoulli trials until ``r`` successes occur.

.. literalinclude:: ../../examples/distributions/negative_binomial_waiting_time.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/negative_binomial_waiting_time.wppl --random-seed 0


Scoring / likelihood via ``factor``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WebPPL supports conditioning using ``factor(score)``, which adds ``score`` to the log probability
of the current execution. This lets us treat the negative binomial as a likelihood if we implement
its log-PMF.

.. literalinclude:: ../../examples/distributions/negative_binomial_logpmf_and_posterior.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/negative_binomial_logpmf_and_posterior.wppl --random-seed 0


Alternative construction: Gamma–Poisson mixture
-----------------------------------------------

The negative binomial can also be seen as a Poisson distribution whose rate is gamma-distributed.
This is one reason it is widely used for **overdispersed count data**.

In the ``(r, p)`` parameterization used above, one convenient mapping is:

.. math::

   \lambda \sim \mathrm{Gamma}(shape=r,\, scale=(1-p)/p), \quad K \mid \lambda \sim \mathrm{Poisson}(\lambda)

Then the marginal distribution of ``K`` is ``NB(r, p)``.

.. literalinclude:: ../../examples/distributions/negative_binomial_gamma_poisson.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/negative_binomial_gamma_poisson.wppl --random-seed 0
