Sampling and scoring
====================

Two primitives to remember
--------------------------

**1) Sampling**

Use ``sample(dist)`` to draw a value from a distribution object.

**2) Scoring**

Use ``dist.score(val)`` to compute the log probability (discrete)
or log density (continuous) that the distribution assigns to ``val``.

A minimal example
-----------------

.. program-output:: python ../../scripts/run_webppl.py ../../examples/distributions/sample_score.wppl --random-seed 0
   :prompt:
   :ellipsis: 0

The optional second argument to ``sample``
------------------------------------------

``sample`` also accepts an optional second argument for things like
**guide distributions** and **drift kernels**.

Guide distributions
~~~~~~~~~~~~~~~~~~~

A guide distribution is specified like this:

- ``sample(dist, {guide: function() { return guideDist; }})``

The example below shows the *syntax* and uses forward sampling to make the
difference visible:

.. program-output:: python ../../scripts/run_webppl.py ../../examples/distributions/sample_with_guide.wppl --random-seed 0
   :prompt:
   :ellipsis: 0

Drift kernels
~~~~~~~~~~~~~

A drift kernel is specified like this:

- ``sample(dist, {driftKernel: function(prevVal) { return proposalDist; }})``

This is mainly used by MH-based inference methods.
