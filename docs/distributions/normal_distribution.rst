Normal (Gaussian) Distribution
==============================

The normal distribution (or Gaussian distribution) is a fundamental continuous probability distribution. It is symmetric and describes data that clusters around a central mean, with the spread determined by the standard deviation.

It is defined by two parameters:

* **Mean** (``mu``): The expected value or center of the distribution.
* **Standard Deviation** (``sigma``): The spread of the distribution.

Executable example: Basic properties and sampling
-------------------------------------------------

In WebPPL, you can define a normal distribution using the ``Gaussian`` object. Here we sample from it and calculate its probability density.

.. literalinclude:: ../../examples/distributions/normal_basic.wppl
   :language: javascript
   :linenos:

**Output:**

.. program-output:: python ../scripts/run_webppl.py examples/distributions/normal_basic.wppl --random-seed 0


Executable example: Bayesian Inference with Gaussian
----------------------------------------------------

The normal distribution is heavily used in Bayesian inference to model continuous parameters or measurement noise. In this example, we estimate the true length of an object based on several noisy measurements.

.. literalinclude:: ../../examples/distributions/normal_inference.wppl
   :language: javascript
   :linenos:

**Output:**

.. program-output:: python ../scripts/run_webppl.py examples/distributions/normal_inference.wppl --random-seed 0