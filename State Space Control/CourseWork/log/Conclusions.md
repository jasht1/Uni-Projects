
## Discussion
%%[[2024-12-19]] @ 14:08%%

The results of the simulations are promising, but the results must be considered in context. These results rely on the [[Designing State Space Model#Assumptions and Approximations|assumptions and approximations]] discussed previously several of which do not hold in reality. 
For example the damping coefficient is assumed to be linear in terms of force/velocity, this simplifies the calculations and is likely how a predictive controller might model the system for processing speed but likely deviates from reality. The behaviour of dampers depends heavily on the type of damper used in the vehicles shocks and can change over the course a single use and over its useful lifespan.[^1] It's a similar case with the approximations of elasticity for the tire and the spring but this provides an illustration of the trade off's that must be made between accuracy and practicality. The usefulness of a model is not in it's perfection but in it's ease of application. 
It should be considered that the system would behave quite differently if the controller introduced any significant latency, in which case additional modes of resonance emerge that can cause instability. 
In addition the physical constraints of the actuator should be accounted for in future simulations should this project be carried forward. These results may depend on unreasonable force, response time, travel speed, accuracy, ect. and taking these limitations into account may require a different tuning.
It would also be wise to utilise some more advanced tuning methods such as the $\text{H}_\infty$ synthesis methods provided by the `control systems` package that could optimise weights across a range of uncertainties through the system. [^2]

## Conclusion 
%%[[2024-12-19]] @ 15:05%%

The simulations show the use of an actuator and tuned PD controller can provide significant improvements in system performance as can be measured in the significant reduction in both peak magnitude and root mean square acceleration of the car body in every test. 

Overall, these simulations provide a strong foundation for moving forward with the active suspension design and demonstrate the potential benefits of this approach for enhancing vehicle ride quality and passenger comfort.

%% ### Refs %%

[^1]: T. P. Waters, Y. Hyun, and M. J. Brennan, “The Effect of Dual-Rate Suspension Damping on Vehicle Response to Transient Road Inputs,” _Journal of Vibration and Acoustics_, vol. 131, no. 1, Jan. 2009, doi: https://doi.org/10.1115/1.2980370.
	[read online](https://eprints.soton.ac.uk/465852/1/1004256.pdf)

[^2]: “control.hinfsyn — MATLAB Control Systems Library documentation.” [Online]. Available: https://www.mathworks.com/help/robust/ref/dynamicsystem.hinfsyn.html. [Accessed: 19-Dec-2024].
