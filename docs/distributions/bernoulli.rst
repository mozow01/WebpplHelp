Bernoulli
=========

Constructor
-----------

``Bernoulli({p: ...})``

- ``p``: success probability in ``[0, 1]``.
- Support: ``{true, false}``.

Gotcha: booleans vs 0/1
-----------------------

``Bernoulli`` returns **booleans** (``true``/``false``).
If you need 0/1 values, consider:

- ``(sample(Bernoulli({p: p})) ? 1 : 0)`` for an explicit conversion, or
- ``MultivariateBernoulli({ps: ...})`` for a vector of 0/1 values.

Executable example
------------------

.. literalinclude:: ../../examples/distributions/bernoulli.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py ../examples/distributions/bernoulli.wppl --random-seed 0
   :prompt:
   :ellipsis: 0
