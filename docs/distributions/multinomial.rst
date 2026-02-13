Multinomial
===========

Constructor
-----------

``Multinomial({ps: ..., n: ...})``

- ``ps``: probability vector (a JS array of reals) whose elements **sum to 1**
- ``n``: number of trials (integer, ``>= 1``)
- Support: a vector/array of **counts** with the same length as ``ps`` and sum ``n``

This differs from ``Discrete``/``Categorical``, which allow **unnormalized** weights.

Executable example
------------------

.. literalinclude:: ../../examples/distributions/multinomial.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/multinomial.wppl --random-seed 0

Common failure modes
--------------------

- ``ps`` does not sum to 1 (use ``normalize(ps)`` if you have weights).
- The observed count vector:
  - has a different length than ``ps``, or
  - does not sum to ``n``.
