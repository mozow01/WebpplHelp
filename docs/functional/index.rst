Functional Programming
======================

WebPPL looks like JavaScript, but in practice it should be treated as a
*functional fraction* of JavaScript.

In WebPPL, the functional style is not merely a best practice:
for probabilistic modeling it is effectively the *only reliable style*.

Why "functional subset"?
------------------------

WebPPL programs are transformed internally (e.g. into continuation-passing style)
to support probabilistic inference. These program transformations interact best
with code that is:

- **expression-oriented** (compute values and return them),
- built from **pure functions** (same input -> same output),
- uses **immutable data** (avoid in-place updates),
- composed from **higher-order functions** (functions that take/return functions).

Imperative patterns (especially mutation-heavy code) may still run in some cases,
but they are fragile: they tend to be harder to reason about, harder to infer
over, and easier to break with subtle bugs when inference methods or program
structure changes.

What this chapter covers
------------------------

This chapter introduces functional programming concepts as they are used in
WebPPL, with runnable examples and WebPPL-specific "gotchas".

.. toctree::
   :maxdepth: 2
   :caption: Contents

   fp_basics
   cache