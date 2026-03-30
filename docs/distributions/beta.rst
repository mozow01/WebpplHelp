Beta
====

The Beta distribution is a **continuous** probability distribution defined on the interval :math:`[0, 1]`.
It is most commonly used in Bayesian statistics to model uncertainty about a **probability** or a **proportion**
(such as a click-through rate, a success rate, or a coin's fairness).

Intuition:

- While the Binomial distribution counts successes, the Beta distribution models the **probability of success** itself.
- If you think of a probability :math:`p` as a random variable, the Beta distribution describes which values of :math:`p` are more or less likely based on prior knowledge or observed data.

What question does the Beta answer?
-----------------------------------

The Beta distribution answers the following core question:

Given that I have seen :math:`\alpha - 1` successes and :math:`\beta - 1` failures (or have equivalent prior belief),
what is the probability distribution over the unknown parameter :math:`p \in [0, 1]`?

Closed form (probability density function)
------------------------------------------

For :math:`x \in [0, 1]` and shape parameters :math:`\alpha > 0`, :math:`\beta > 0`:

.. math::

   f(x; \alpha, \beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}

where the denominator :math:`B(\alpha, \beta)` is the **Beta function**, which ensures the total area under the curve is 1.

Intuition (Alpha and Beta as "pseudo-counts")
---------------------------------------------

A very helpful way to think about the parameters :math:`\alpha` (alpha) and :math:`\beta` (beta) is as "counts" of observations:

- :math:`\alpha - 1`: The number of "successes" previously seen.
- :math:`\beta - 1`: The number of "failures" previously seen.

For example:

- ``Beta({a: 1, b: 1})`` is a **Uniform distribution** (0 successes, 0 failures; every value of :math:`p` is equally likely).
- ``Beta({a: 10, b: 10})`` is a symmetric bell-shaped curve centered at :math:`0.5`.
- ``Beta({a: 2, b: 8})`` is skewed toward low values (more failures than successes).

Constructor
-----------

``Beta({a: ..., b: ...})``

- ``a``: shape parameter 1 (alpha), real number ``> 0``
- ``b``: shape parameter 2 (beta), real number ``> 0``
- support: real numbers in ``[0, 1]``

Interactive Visualization
-------------------------

Experiment with the :math:`\alpha` and :math:`\beta` parameters below to see how the shape of the Beta distribution changes in real-time.

.. raw:: html

   <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
   
   <style>
       .beta-generator-wrapper {
           margin: 2rem 0;
           padding: 1rem;
           border: 1px solid #e1e4e8;
           border-radius: 6px;
           background-color: #ffffff;
       }
       .beta-controls {
           background: #f6f8fa;
           padding: 1rem;
           border-radius: 6px;
           display: flex;
           justify-content: center;
           align-items: center;
           gap: 20px;
           margin-bottom: 1rem;
       }
       .beta-controls label { font-weight: bold; margin-right: 5px; }
       .beta-controls input {
           width: 70px;
           padding: 6px;
           border: 1px solid #d1d5da;
           border-radius: 4px;
       }
       .beta-controls button {
           padding: 8px 16px;
           background-color: #2ea44f;
           color: white;
           border: none;
           border-radius: 4px;
           font-weight: bold;
           cursor: pointer;
       }
       .beta-controls button:hover { background-color: #2c974b; }
       .beta-canvas-container {
           position: relative;
           height: 350px;
           width: 100%;
       }
   </style>

   <div class="beta-generator-wrapper">
       <div class="beta-controls">
           <div>
               <label for="alphaInput">Alpha (α):</label>
               <input type="number" id="alphaInput" value="2" min="1" max="150" step="1">
           </div>
           <div>
               <label for="betaInput">Beta (β):</label>
               <input type="number" id="betaInput" value="5" min="1" max="150" step="1">
           </div>
           <button onclick="updateBetaChart()">Draw Distribution</button>
       </div>
       <div class="beta-canvas-container">
           <canvas id="betaChartCanvas"></canvas>
       </div>
   </div>

   <script>
       function betaFactorial(n) {
           if (n === 0 || n === 1) return 1;
           let result = 1;
           for (let i = n; i > 1; i--) { result *= i; }
           return result;
       }

       function betaFunc(alpha, beta) {
           return (betaFactorial(alpha - 1) * betaFactorial(beta - 1)) / betaFactorial(alpha + beta - 1);
       }

       function calculateBetaPDF(x, alpha, beta) {
           if (x < 0 || x > 1) return 0;
           const normalizer = betaFunc(alpha, beta);
           return (Math.pow(x, alpha - 1) * Math.pow(1 - x, beta - 1)) / normalizer;
       }

       function generatePlotData(alpha, beta, numPoints = 100) {
           const labels = [];
           const data = [];
           for (let i = 0; i <= numPoints; i++) {
               const x = i / numPoints;
               labels.push(x.toFixed(2));
               data.push(calculateBetaPDF(x, alpha, beta));
           }
           return { labels, data };
       }

       let myBetaChart = null;

       function updateBetaChart() {
           let alpha = parseInt(document.getElementById('alphaInput').value);
           let beta = parseInt(document.getElementById('betaInput').value);

           if (isNaN(alpha) || alpha < 1) alpha = 1;
           if (isNaN(beta) || beta < 1) beta = 1;
           if (alpha > 150) alpha = 150;
           if (beta > 150) beta = 150;

           const plotData = generatePlotData(alpha, beta);
           const ctx = document.getElementById('betaChartCanvas').getContext('2d');

           if (myBetaChart) {
               myBetaChart.destroy();
           }

           myBetaChart = new Chart(ctx, {
               type: 'line',
               data: {
                   labels: plotData.labels,
                   datasets: [{
                       label: `Beta(${alpha}, ${beta}) PDF`,
                       data: plotData.data,
                       borderColor: '#0366d6',
                       backgroundColor: 'rgba(3, 102, 214, 0.1)',
                       borderWidth: 2,
                       fill: true,
                       pointRadius: 0,
                       tension: 0.4
                   }]
               },
               options: {
                   responsive: true,
                   maintainAspectRatio: false,
                   scales: {
                       x: { title: { display: true, text: 'Probability (p)' }, ticks: { maxTicksLimit: 11 } },
                       y: { title: { display: true, text: 'Density' }, beginAtZero: true }
                   },
                   plugins: {
                       tooltip: {
                           callbacks: { label: function(context) { return `Density: ${context.parsed.y.toFixed(4)}`; } }
                       }
                   }
               }
           });
       }

       // Initialize the chart once the DOM is fully loaded
       document.addEventListener('DOMContentLoaded', updateBetaChart);
   </script>


Relationship to Binomial (Conjugacy)
------------------------------------

The Beta distribution is the **conjugate prior** for the Binomial likelihood. This is the core of simple Bayesian updating:

1. Start with a Prior: :math:`p \sim Beta(\alpha, \beta)`
2. Observe Data: Observe :math:`k` successes and :math:`n-k` failures in :math:`n` Binomial trials.
3. Compute Posterior: The updated distribution for :math:`p` is exactly :math:`Beta(\alpha + k, \beta + n - k)`.

Typical use cases
-----------------

- Modeling uncertainty about a success probability :math:`p`.
- Serving as a prior distribution for Bernoulli or Binomial observation models.
- Representing any continuous random variable that is strictly bounded between 0 and 1.

Executable example: basics (samples and score)
----------------------------------------------

.. literalinclude:: ../../examples/distributions/beta_basics.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/beta_basics.wppl --random-seed 0

Scoring
-------

``d.score(x)`` is the **log density** of the value ``x`` in ``[0, 1]``.

Because the Beta is a continuous distribution, ``score(x)`` represents the log of the Probability Density Function (PDF), not a discrete probability.

.. math::

   d.score(x) = (\alpha - 1) \log x + (\beta - 1) \log (1 - x) - \log B(\alpha, \beta)

Executable example: Bayesian updating
-------------------------------------

Story: We start with a "Flat" (Uniform) prior because we know nothing about a coin.
We then observe 8 heads out of 10 tosses. We use ``observe`` to see how our belief about the coin's fairness updates.

.. literalinclude:: ../../examples/distributions/beta_bayesian_update.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/distributions/beta_bayesian_update.wppl --random-seed 0