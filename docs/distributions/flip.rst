flip
====

Signature
---------

``flip([p]) -> bool``

- ``p``: real number in ``[0, 1]`` (default: ``p = 0.5``)
- return value: ``true`` / ``false`` (boolean)

``flip`` is a convenience function: it samples from a Bernoulli distribution.


Relationship to Bernoulli
-------------------------

Conceptual and practical equivalence:

- ``flip(p)``  ~  ``sample(Bernoulli({p: p}))``

**When to use which?**

- Use ``flip`` when you just need a quick weighted coin flip and a boolean result is fine.
- Use ``Bernoulli({p: ...})`` when you want an explicit distribution object (e.g. to pass around,
  call ``score`` on it, or ``observe`` against it).


Relationship to Categorical
---------------------------

``Categorical({ps: ..., vs: ...})`` is the general discrete distribution that returns one of the values in ``vs``,
with probabilities proportional to ``ps`` (``ps`` may be unnormalized).

You can express ``flip(p)`` as a categorical distribution over explicit outcomes:

- ``sample(Categorical({ps: [p, 1-p], vs: [true, false]}))``

**When is Categorical better?**

- When you want non-boolean outcomes (e.g. ``'H'/'T'`` or ``1/0``).
- When you have more than two outcomes.


Working examples
----------------

1) One flip (default p=0.5 and explicit p)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/distributions/flip_one.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py ../examples/distributions/flip_one.wppl --random-seed 0
   :prompt:
   :ellipsis: 0


2) Many flips: repeat + count trues + empirical rate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/distributions/flip_many.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py ../examples/distributions/flip_many.wppl --random-seed 0
   :prompt:
   :ellipsis: 0


3) Same distribution: flip vs Bernoulli vs Categorical (enumerate)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/distributions/flip_equivalences.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py ../examples/distributions/flip_equivalences.wppl --random-seed 0
   :prompt:
   :ellipsis: 0


Common pitfall: function vs result (repeat)
-------------------------------------------

- ``flip`` (without parentheses) is a *function* you can pass: ``repeat(10, flip)``
- ``flip()`` is the *result of one flip* (a boolean), and cannot be passed as the callback

If you want repeated *parameterized* flips, wrap it:

- correct: ``repeat(10, function() { return flip(0.3); })``
