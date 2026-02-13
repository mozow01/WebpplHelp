Binomial
========

Constructor
-----------

``Binomial({p: ..., n: ...})``

- ``p``: success probability in ``[0, 1]``
- ``n``: number of trials (integer, ``>= 1``)
- Support: integers ``0..n``

Use cases
---------

- Counting successes in ``n`` independent Bernoulli trials.
- Likelihood for integer count data via ``observe(Binomial(...), k)``.

Executable example
------------------

.. literalinclude:: ../../examples/distributions/binomial.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/binomial.wppl --random-seed 0
