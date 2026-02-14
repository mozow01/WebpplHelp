Cache (memoization)
===================

WebPPL provides a ``cache`` combinator that *returns a new function* whose results
are remembered and reused. This is commonly called **memoization**.

At first glance, ``cache`` feels very "functional": for the same input you get
the same output. But the mechanism that makes this possible is *state*.

So ``cache`` is a good example of a deliberate, useful tension:

**cache is FP "returning" to stateful computation—on purpose—so you can model and
optimize reliably.**

What ``cache`` does
-------------------

Given a function ``f``, ``cache(f)`` returns a function ``g`` such that:

- On the first call with an argument ``x``, ``g(x)`` computes ``f(x)`` and stores the result.
- On later calls with the *same* argument ``x``, ``g(x)`` returns the stored result
  instead of recomputing.

In other words, ``cache`` creates a hidden lookup table:

- key: the argument(s)
- value: the computed result

From the outside, the cached function looks like a deterministic mapping.
Inside, it maintains **mutable state** (the memo table).

Why this matters for functional programming
-------------------------------------------

In "pure" functional programming, a function should have no hidden memory:
it should not depend on or modify hidden state.

``cache`` violates that purity internally, but it is still widely used in functional
settings because:

- it preserves the *interface* of a function,
- it can preserve the *observable behavior* (for pure functions),
- it gives large performance wins.

So you can think of ``cache`` as:

- a controlled "imperative" mechanism (state),
- wrapped in a functional interface (a returned function),
- to achieve a good goal (speed or stable latent structure).

In probabilistic programming, there is an additional motivation:
``cache`` can express a *single latent random choice per entity*.

When ``cache`` is safe: pure/deterministic computations
-------------------------------------------------------

If ``f`` is deterministic (no randomness, no side effects), then caching is
behavior-preserving: it only makes things faster.

Example: caching an expensive deterministic computation
-------------------------------------------------------

.. code-block:: javascript

   var expensive = function(x) {
     // imagine something computationally heavy here
     return x * x + 1;
   };

   var fastExpensive = cache(expensive);

   display(fastExpensive(10)); // computes and stores
   display(fastExpensive(10)); // reuses cached result

When ``cache`` is a modeling tool: one latent value per key
----------------------------------------------------------

If the body of ``f`` contains randomness, then caching changes *the meaning*:

- without caching: each call can create a *new* random choice
- with caching: the first random choice is stored and *reused* for that key

This is often exactly what you want when modeling hidden traits.

Good modeling example: a stable latent trait per individual
-----------------------------------------------------------

Suppose each person has an unobserved "type" (A or B) that should be consistent
everywhere in the program.

.. code-block:: javascript

   // A latent trait per person id
   var personType = cache(function(id) {
     return flip(0.3) ? "A" : "B";
   });

   display(personType("anna"));
   display(personType("anna")); // same as above: "anna" keeps one latent type
   display(personType("bela")); // different id => independent latent type

Here ``cache`` is not just an optimization; it expresses a modeling assumption:

- each id has exactly one latent draw.

This is a clean example of how probabilistic modeling often uses a small amount
of state internally to achieve a coherent *functional* model structure.

When ``cache`` is dangerous: you accidentally remove independence
---------------------------------------------------------------

If you *intended* independent random draws on each call, caching is the wrong tool.
It will "glue together" calls that should be independent.

Bad example: you wanted a fresh coin flip every time
-----------------------------------------------------

.. code-block:: javascript

   var coin = cache(function() { return flip(0.5); });

   display(coin()); // first draw
   display(coin()); // WARNING: returns the same result as above (cached)

This is usually a bug, because it turns two intended independent flips into
one shared latent flip.

A simple rule of thumb
----------------------

Use ``cache`` when you want either:

1) **Optimization** for expensive deterministic code, or
2) **One latent value per key** (a stable hidden property tied to an id).

Avoid ``cache`` when you want:

- independent random draws each time,
- time-varying or history-dependent behavior (unless that is explicitly modeled).

See also
--------

- :doc:`functions_and_closures` (``cache`` returns a function; it is a closure-like pattern)
- :doc:`immutability_lists_objects` (why FP prefers immutable data, and what ``cache`` is doing differently)
- Distributions: :doc:`../distributions/bernoulli` (for the ``flip`` examples above)


Executable example
------------------

.. literalinclude:: ../../examples/functional/cache.wppl
   :language: javascript

.. program-output:: python ../scripts/run_webppl.py ../examples/functional/cache.wppl --random-seed 0
