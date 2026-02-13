Distributions
=============

This chapter focuses on the part of WebPPL that tends to cause the most frustration in practice:
**the exact shape of parameters** (especially probability vectors) and **what the return value looks like**.

WebPPL distribution constructors generally take a single **options object** (a JS object literal)
and return a *distribution object*. Distribution objects are mainly used in two ways:

- ``sample(dist[, opts])`` draws a value.
- ``dist.score(val)`` returns the log-probability / log-density for a specific value.

.. toctree::
   :maxdepth: 2

   sample_and_score
   flip
   bernoulli
   discrete_vs_categorical
   binomial
   multinomial
   negative_binomial

