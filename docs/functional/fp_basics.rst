Functional programming basics
=============================

WebPPL is a functional subset of JavaScript
-------------------------------------------

WebPPL *looks* like JavaScript, but you should treat it as a **functional subset**
of JavaScript: most idiomatic WebPPL programs are expression-oriented and built
by composing functions.

This is not only a matter of style. WebPPL supports probabilistic inference by
transforming your program internally (for example into continuation-passing style).
Those transformations work best—and most predictably—when your code is written in
a functional way.

In practice, for probabilistic modeling in WebPPL, the functional style is the
**only reliable style**.

What "functional programming" means here
-----------------------------------------

Functional programming (FP) is a way of writing programs by **building and
composing functions**, rather than by repeatedly mutating variables and data
structures.

A practical checklist for WebPPL:

- **Prefer expressions over statements.**
  Write code that *returns values* instead of code that *updates state*.
- **Prefer pure functions.**
  A pure function always returns the same result for the same inputs.
  (Randomness is a deliberate exception in probabilistic programs.)
- **Avoid mutation.**
  Instead of changing an array/object in-place, create a new one.
- **Use higher-order functions.**
  Functions like ``map``, ``reduce``, and ``repeat`` are central tools.

A useful mental model
---------------------

In FP, a program is a pipeline:

1. **Generate** values (often by sampling).
2. **Transform** them (with functions like ``map``).
3. **Summarize** them (with ``reduce`` or a custom aggregator).
4. **Return** the result.

This is exactly how many WebPPL models are structured.

Key terms (short definitions)
-----------------------------

Expression
  A piece of code that evaluates to a value (e.g. ``1 + 2``, ``flip(0.7)``,
  or a function call).

Pure function
  A function with no side effects and deterministic behavior:
  same inputs -> same output.

Higher-order function
  A function that takes a function as an argument or returns a function
  (e.g. ``map(f, xs)`` or a function that returns another function).

Closure
  A function that "remembers" variables from the scope where it was created.

Immutability
  The practice of not modifying data in-place. Instead, create new values.

Why this matters in probabilistic programming
---------------------------------------------

Probabilistic models are naturally described by composition:

- a *prior* is a function that produces uncertain values,
- a *likelihood* scores or observes data given those values,
- *inference* turns the model into a posterior distribution.

This "functions all the way down" structure is exactly what FP encourages.

Common pitfalls (and the FP-friendly alternative)
-------------------------------------------------

Mutation-heavy code
  Avoid patterns like repeatedly pushing into arrays or updating objects in-place.
  Prefer building a new list with ``map``/``repeat`` and returning it.

Hidden state
  Avoid relying on variables that change across time in complex ways.
  Prefer passing values explicitly through function arguments.

Deep imperative control flow
  Prefer small helper functions and expression-oriented conditionals.

Executable micro-example: closures
----------------------------------

This example demonstrates a **closure**: a function that remembers variables from
its environment, and how that plays nicely with ``map``.

.. literalinclude:: ../../examples/functional/closures.wppl
   :language: javascript

.. program-output:: python ../scripts/run_webppl.py ../examples/functional/closures.wppl --random-seed 0

Where to go next
----------------

- If you are new to functions in WebPPL, continue with :doc:`functions_and_closures`.
- For the most common list-processing patterns, see :doc:`map_filter_reduce`.
- For WebPPL-specific quirks, see :doc:`gotchas_js_webppl`.
