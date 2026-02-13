Bernoulli
=========

A Bernoulli distribution models a single **yes/no** (two-outcome) event.

Typical real-world meanings:

- "Did it rain today?" (yes/no)
- "Did the user click the link?" (yes/no)
- "Is the item defective?" (yes/no)

In WebPPL, Bernoulli samples are **booleans**: ``true`` / ``false``.


Constructor
-----------

``Bernoulli({p: ...})``

- ``p``: success probability in ``[0, 1]``
- support: ``{true, false}``


Relationship to booleans
------------------------

Bernoulli is the canonical distribution when your random variable is literally a boolean.
That means:

- ``sample(Bernoulli({p: 0.7}))`` returns either ``true`` or ``false``.
- The exact meaning of "success" is up to you. Often we interpret:
  - ``true``  = success / yes / event happens
  - ``false`` = failure / no / event does not happen


Relationship to ``flip``
------------------------

``flip`` is shorthand for a Bernoulli draw:

- ``flip(p)`` is equivalent to ``sample(Bernoulli({p: p}))``.
- ``flip()`` uses the default ``p = 0.5`` (a fair coin).

Rule of thumb:

- Use ``flip`` when you just want a quick boolean coin flip.
- Use ``Bernoulli({p: ...})`` when you want an explicit distribution object
  (e.g. to call ``score`` or pass it around).


Relationship to ``Categorical``
-------------------------------

You can also express the same two-outcome distribution using ``Categorical`` by making
the outcomes explicit:

``sample(Categorical({ps: [p, 1-p], vs: [true, false]}))``

This is useful when you want non-boolean outcomes, e.g. ``['H','T']`` or ``[1,0]``,
or when you later generalize to more than two outcomes.


Scoring
-------

For Bernoulli:

- ``d.score(true)  = log(p)``
- ``d.score(false) = log(1 - p)``

These are **natural logs** (base *e*). If you want the ordinary probability back,
use ``Math.exp(logp)``.


Gotcha: booleans vs 0/1
-----------------------

Bernoulli returns booleans (``true/false``).

If you need numeric 0/1 values, either:

- convert explicitly:

  ``(sample(Bernoulli({p: p})) ? 1 : 0)``

- or if you need a *vector* of 0/1 outcomes, consider ``MultivariateBernoulli({ps: ...})``.


Executable example: basics (sample, score, flip)
------------------------------------------------

.. literalinclude:: ../../examples/distributions/bernoulli.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/bernoulli.wppl --random-seed 0


A real-life example: estimating a biased coin (discrete grid)
-------------------------------------------------------------

Suppose you flipped a coin 10 times and observed the outcomes (``true`` = heads).
We want to infer which ``p`` values are plausible.

To keep everything **finite and exactly enumerable**, we put a prior on a discrete grid
(e.g. ``p in {0.1, 0.2, ..., 0.9}``) and use ``Infer({method: 'enumerate'})``.

.. literalinclude:: ../../examples/distributions/bernoulli_coin_posterior.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/bernoulli_coin_posterior.wppl --random-seed 0
