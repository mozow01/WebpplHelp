Sampling and scoring
====================

This page is the "root" reference for WebPPL's two most important building blocks:

- ``sample(dist[, opts])``: create a random choice by drawing a value from a distribution object
- ``dist.score(value)``: compute the log probability / log density assigned to a value

If you are ever unsure about syntax, shapes, or what an option does, come back here first.

Quick glossary (read this once)
-------------------------------

.. glossary::

  distribution object
    An object representing a probability distribution, such as ``Bernoulli({p: 0.7})`` or
    ``Gaussian({mu: 0, sigma: 1})``. Distribution objects support at least:

    - sampling: via ``sample(dist)``
    - scoring: via ``dist.score(value)``

  random choice (sample site)
    A place in your program where ``sample(...)`` is called.
    During inference, WebPPL treats each sample site as a stochastic "choice" whose value can be explored.

  log probability / log density
    WebPPL uses **natural log** values (base *e*).
    For discrete distributions, ``score`` returns ``log P(X = value)``.
    For continuous distributions, it returns a **log density** (not a probability).

  inference
    The process of turning a stochastic program (a model) into a distribution on its return values,
    usually approximately (e.g. via MCMC, SMC, etc.).

  guide distribution
    An *auxiliary* distribution used by some inference strategies as a proposal / approximation.
    It does **not** change the model itself; it changes how inference explores it.

  drift kernel
    A proposal mechanism for MCMC (MH-based) methods.
    It proposes new values based on the *previous* value at a sample site.

Distribution objects in one minute
----------------------------------

A distribution object represents a distribution, and has two principal uses:

1. Draw samples from it using ``sample(dist)``.
2. Compute the (natural) log probability / density of a value using ``dist.score(value)``.

See also: the Distributions overview page.

Sampling: ``sample(dist[, opts])``
----------------------------------

Basic form
^^^^^^^^^^

Use ``sample(dist)`` to draw one value from a distribution object.

- For ``Bernoulli({p: ...})`` the result is a boolean (``true/false``).
- For continuous distributions like ``Gaussian(...)`` the result is a number.

Working example: one sample + scoring the sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/distributions/sample_score.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/sample_score.wppl --random-seed 0


Scoring: ``dist.score(value)``
------------------------------

``dist.score(value)`` returns the **natural log** of the probability (discrete)
or density (continuous) that ``dist`` assigns to ``value``.

Two practical notes:

- Log space is used because probabilities can get extremely small.
- If you ever need the probability (discrete), you can convert with ``Math.exp(logp)``.

For Bernoulli in particular:

- ``score(true)  = log(p)``
- ``score(false) = log(1 - p)``

(See also the Bernoulli page.)


The optional second argument to ``sample``
------------------------------------------

``sample`` also accepts an optional second argument ``opts``:

- ``sample(dist, {guide: ...})``
- ``sample(dist, {driftKernel: ...})``

These are **inference controls**:
they affect *how inference proposes values* at a sample site, but they do not change the intended target distribution of the model.

Guide distributions
-------------------

Definition (what is a guide?)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A **guide distribution** is an auxiliary distribution that some inference strategies can use
instead of sampling directly from the model's distribution at a sample site.

Syntax
^^^^^^

A guide distribution is specified like this:

``sample(dist, {guide: function() { return guideDist; }})``

Where ``guideDist`` is another distribution object (e.g. a Gaussian with different parameters).

When does it matter?
^^^^^^^^^^^^^^^^^^^^

It matters when the inference method is told to use guides.
For example, **forward sampling** has an option ``guide: true`` that samples random choices from guides.  
This is useful for debugging and for making the effect visible.

Working example: forward sampling from model vs from guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/distributions/sample_with_guide.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/sample_with_guide.wppl --random-seed 0


Drift kernels
-------------

Definition (what is a drift kernel?)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A **drift kernel** is a function that maps the *previous value* of a random choice
to a proposal distribution. It is mainly used by MH-based MCMC methods.

In other words: it tells MCMC how to propose a "nearby" value instead of proposing from the prior.

Syntax
^^^^^^

A drift kernel is specified like this:

``sample(dist, {driftKernel: function(prevVal) { return proposalDist; }})``

Working example: MCMC with and without a drift kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/distributions/sample_with_drift_kernel.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/sample_with_drift_kernel.wppl --random-seed 0


How to run examples locally
---------------------------

From the repository root you can run any example with:

- ``npx webppl examples/distributions/<file>.wppl --random-seed 0``

(We use ``--random-seed`` in the docs so outputs stay reproducible.)
