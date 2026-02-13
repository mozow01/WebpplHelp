Discrete vs. Categorical
========================

Both ``Discrete`` and ``Categorical`` represent a finite distribution parameterized by a list of non-negative numbers.

- ``Discrete({ps: ...})`` returns an **index** in ``{0, 1, ..., ps.length-1}``.
- ``Categorical({ps: ..., vs: ...})`` returns the **corresponding value** from ``vs``. When ``ps`` is omitted,
  you get a uniform distribution over ``vs``.

Important: unnormalized weights
-------------------------------

For both constructors, ``ps`` can be an unnormalized weight vector:
``P(i)`` is proportional to ``ps[i]``.

Executable example
------------------

.. literalinclude:: ../../examples/distributions/discrete_vs_categorical.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/discrete_vs_categorical.wppl --random-seed 0
