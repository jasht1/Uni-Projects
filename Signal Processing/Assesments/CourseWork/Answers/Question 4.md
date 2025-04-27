%%
![Question 4 (15 marks)](Projects/Uni%20Projects/Signal%20Processing/Assesments/CourseWork/Brief.md#Question%204%20(15%20marks))
%%

It is often the case that a digital system must be determined to match an existing black box system where an engineer can only test inputs and observe outputs. A predictable system can be expected to fit a standard form such as:

$$G(z) = \frac{Y(z)}{X(z)} = \frac
{a_{0} + a_{1} z^{-1} +a_{2} z^{-2} + \dots + a_{n}z^{-n}}
{1 + b_{1} z^{-1} + b_{2} z^{-2} - \dots + b_{n}z^{-n}}
$$

And thus the problem is reduced to tuning the values coefficients to match the observed behaviour of the system. The engineer must be able to determine and distinguish the systems tendency to react to the input vs itself, measured by its cross-correlation and its auto-correlation respectively. Cross-correlation correlates the system output with a time shift of the input data a measure of it's reactivity, whereas auto-correlation measures the system outputs similarity to a time shifted version of it's self, in other words, the systems own resonance. It should then be considered what input data is the best test to get meaningful output data to compare, contrast and thus improve the modelling. The input should at once be random and chaotic to be able to observe the system responding to the greatest verity of stimuli but also be periodic so that the system response to the input can be seen multiple times in different contexts / starting points. These are the properties of pseudo random binary sequences (PRBS)s along with being computationally trivial to produce and tune to fit a given need. This makes PRBS optimal as input data to fit/train a model of an unknown system, as it is has near 0 auto-correlation of it's own apart from at 0 time shift with it being periodic making it easy to account for and contrast with genuine auto-correlation of the system.