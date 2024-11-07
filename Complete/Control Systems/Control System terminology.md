
# Terminology
### Plant
 **the plant is the the thing which your system is trying to control**, it can be considered synonymous with the word "system". It could be anything that has an input and gives an output. In control theory is depicted as a box with a relation Output VS. Input, we call this transfer function. It may have also multiple inputs and/or multiple outputs.
	https://www.circuitbread.com/glossary/plant-control-systems
### Disturbance
External factors that effect the output of the [[#Plant]]
### Noise
unwanted signal effecting sensor values
	https://uk.mathworks.com/videos/understanding-control-systems-part-3-components-of-a-feedback-control-system-123645.html

### Inversion
Creating a inverted model of the system that predicts the input required to produce the desired output.
	https://faculty.washington.edu/devasia/Talks/Inversion_Theory.pdf
### Feedback
using the difference of the measured system output and the desired output to account for uncertainties & [[Control System terminology#Disturbance|disturbance]].
	https://faculty.washington.edu/devasia/Talks/Inversion_Theory.pdf
### Feedforward
using prior knowledge of the system ([[Control System terminology#Inversion|inversion]]) to convert desired output into useful input. 

## Types of control system
![[Open vs closed loop systems]]
## Variables
$u(t)$ : control signal #definition , the output of the control system
$e(t)$ : error signal #definition , the input to a control system 
![[physics variables#Types of variables]]

## Acronymns
### LTI
Linear time invariant
### LTF
linear transfer function
### MIMO
multiple input multiple output
### SISO
single input single output