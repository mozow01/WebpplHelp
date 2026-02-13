Discrete vs. Categorical
========================

Both ``Discrete`` and ``Categorical`` represent finite (discrete) distributions parameterized by
a vector of non-negative weights.

They differ in **what they return**:

- ``Discrete({ps: ...})`` returns an **index** in ``{0, 1, ..., ps.length - 1}``.
- ``Categorical({ps: ..., vs: ...})`` returns the **corresponding value** from ``vs``.

If you remember only one thing, remember this: **Discrete returns an index; Categorical returns a value.**


Constructors
------------

Discrete
^^^^^^^^

``Discrete({ps: ...})``

- ``ps``: list/array of non-negative numbers (weights)
- return value: an integer index

Categorical
^^^^^^^^^^^

``Categorical({ps: ..., vs: ...})``

- ``vs``: list/array of values (any type)
- ``ps``: list/array of non-negative numbers (weights), same length as ``vs``

Uniform categorical (omit ``ps``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you omit ``ps``:

``Categorical({vs: vs})``

you get a **uniform** distribution over the values in ``vs``.


Important: unnormalized weights
-------------------------------

For both constructors, ``ps`` may be **unnormalized**.
That is, ``ps`` is treated as weights and then internally normalized:

``P(i) ∝ ps[i]``

Example: ``ps = [1, 3, 6]`` corresponds to probabilities ``[0.1, 0.3, 0.6]``.

(Contrast: ``Multinomial`` requires a normalized probability vector.)


Shape and typing rules (common gotchas)
---------------------------------------

- ``ps`` must contain **non-negative** numbers.
- In ``Categorical``, ``ps.length`` must equal ``vs.length``.
- ``Discrete`` returns an **index**; to map to an actual value, you must index into your own ``vs`` list.
- ``score`` expects the same type that ``sample`` would return:
  - ``Discrete({ps}).score(k)`` expects an **integer index** ``k``.
  - ``Categorical({ps, vs}).score(v)`` expects a value from **``vs``**.


Executable example
------------------

.. literalinclude:: ../../examples/distributions/discrete_vs_categorical.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/discrete_vs_categorical.wppl --random-seed 0


Real-life pattern: weighted choice among actions
------------------------------------------------

A common use case is selecting among options with different prior plausibilities
(e.g. "try easy fix", "reboot", "ask for help").

``Categorical`` is often more convenient than ``Discrete`` here because it returns the option directly.

Tip: if you later need to attach more information, you can store objects in ``vs`` (e.g. ``{name: ..., cost: ...}``).

Measurement scales note
-----------------------

``Categorical``/``Discrete`` are foundational because they match the first measurement levels in the classic scale taxonomy:
**nominal** (categories with no inherent order) and **ordinal** (categories with an order).
At these levels, observations are not “quantities” in the arithmetic sense but **labels** (nominal) or **orderable labels** (ordinal),
so the natural probabilistic model is a finite choice among outcomes—exactly what ``Categorical``/``Discrete`` represent.
For **interval** and **ratio** scales, differences and ratios are meaningful and one often uses continuous (or otherwise quantitative)
distributions—though discretization is always possible when appropriate.

Examples: nominal vs ordinal
----------------------------

This example demonstrates how ``Categorical`` naturally models the first two measurement levels:

- **Nominal**: outcomes are *labels* with no inherent order (e.g. colors).
- **Ordinal**: outcomes are still labels, but we interpret them as ordered (e.g. low < medium < high).

The key point is that ``Categorical`` itself does **not** “know” about order. It simply returns one of the values in ``vs``
according to the weights in ``ps``. If you want to perform numeric operations that rely on order (for example, compute an
“average level”), you must **explicitly encode** your ordinal labels as **ranks** (e.g. low→1, medium→2, high→3).

The code below therefore prints three exact (enumerated) distributions:

1. a nominal distribution over color labels,
2. an ordinal distribution over level labels (still just labels),
3. the same ordinal distribution after mapping labels to numeric ranks, which makes quantities like expected rank well-defined.


.. literalinclude:: ../../examples/distributions/categorical_nominal_vs_ordinal.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/categorical_nominal_vs_ordinal.wppl --random-seed 0
