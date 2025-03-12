
# Pneumatic Task Report 

## Stamping Machine

![Stamping Machine - FluidSIM Diagram|400](Stamping%20Machine%20-%20FluidSIM%20Diagram.png)

- Single acting cylinder
- 3/2 Way Valve 
	- Pneumatically Actuated 
	- Spring Return
	- Normally Closed
- 2/2 Way Valve 
	- Pneumatically Actuated 
	- Spring Return
	- Normally Closed
- Twin Pressure Valve
- 4/2 Way Valve
	- Roller Plunger actuated
	- Spring Return
- 4/2 Way Valve
	- Roller Plunger actuated
	- Pneumatically Actuated 
- 3/2 Way Valve
	- Detent Switch
- 3/2 Way Valve
	- Detent Button
	- Spring Return

## Metal Casing 

This section describes a modular automated process for constructing a metal casing (inspired by my Steinberg UR22C) from a roll of sheet metal. 

### Cutting Sections

![Cut Sections - Flow Diagram|500](Cut%20Sections%20-%20Flow%20Diagram.svg)

A sheet is fed by conveyor of driven rollers, these have enough friction to pull the sheet forward when it is free but not to crumple/tear it.
When the sheet roll reaches the roller switch, the shear is actuated.
This cuts a section of sheet allowing the cut section to advance while blocking the progress of the roll.
Once the sheet section is clear from the switch the shear retracts, this allows the sheet roll to advance again and the cycle repeats.
The cut sections can be deposited into a magazine, this gives the production line some buffer between modules. 

![Cut Sections - FluidSIM Diagram|300](Cut%20Sections%20-%20FluidSIM%20Diagram.png)

- Single Acting Cylinder
- 3/2 Way Valve
	- Pneumatic
	- Spring Return
- 3/2 Way Valve
	- Roller Switch
	- Spring return
- 3/2 Way Valve
	- Detent Switch
	- Spring return
- 2/2 Way Valve
	- Detent Button
	- Spring Return
	- Normally Closed

### Magazine Dispense

![Mag Dispense - Flow Diagram|550](Mag%20Dispense%20-%20Flow%20Diagram.svg)

The magazines store a stack of sheet sections, when triggered by a pneumatic signal the bottom most part is dispensed. 
A roller switch at the base of the magazine pulls double duty, detecting when a part is dispensed correctly and if the magazine is empty.

![Mag Dispense - FluidSIM Diagram|300](Mag%20Dispense%20-%20FluidSIM%20Diagram.png)

- Single Acting Cylinder
- 3/2 Way Valve
	- Pneumatic
	- Spring Return
- 3/2 Way Valve
	- Roller Switch
	- Spring return
- 3/2 Way Valve
	- Detent Switch
	- Spring return
- 3/2 Way Valve
	- Detent Button
	- Spring Return

### Fold Section

![Fold 1 - Flow Diagram](Fold%201%20-%20Flow%20Diagram.svg)

When **B6** detects the clamp is empty the magazine dispense is triggered advancing a sheet section. 
When this reaches **B6** the clamp is engaged, and after a brief delay so is the folding mechanism.
When the folding mechanism reaches **B7** the folding mechanism is disengaged followed more slowly by the clamp.
This allows the folded section to advance out of the clamp into a magazine of the same principle discussed in the previous section. 

![Fold 2 - Flow Diagram|550](Fold%202%20-%20Flow%20Diagram.svg)

A similar mechanism following the same principle is used to achieve the second fold.



![Fold - FluidSIM Diagram|400](Fold%20-%20FluidSIM%20Diagram.png)

- Single Acting Cylinder
- One Way Flow Control Valve
- 3/2 Way Valve
	- Pneumatic
	- Spring Return
- 3/2 Way Valve
	- Pneumatic with Pneumatic Timer (normally open)
	- Spring Return
- Twin Pressure Valve
- 4/2 Way Valve
	- Roller Switch
	- Spring return
- 3/2 Way Valve
	- Probe Switch
	- Spring return
- 3/2 Way Valve
	- Detent Switch
	- Spring return
- 2/2 Way Valve
	- Detent Button
	- Spring Return
	- Normally Closed


