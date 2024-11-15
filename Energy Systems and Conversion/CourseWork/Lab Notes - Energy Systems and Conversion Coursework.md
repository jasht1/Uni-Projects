
## Procedure
%%[[2024-11-11]] @ 11:38%%

[[Brief - Energy Systems and Conversion Coursework.pdf]]

1. Set the water flow rate to $20 \ g/s$
	Record: 
	- condenser pressure, $P_{c}$, 
	- evaporator pressure $P_{e}$, 
	- condensing temperature $t_{6}$, 
	- evaporating temperature $t_{5}$, 
	- any other temperatures.

2. Reduce the cooling water flow by a small increment so that the condenser pressure increases by about $10-20 \ kN/m^{2}$. 
	*This amount will vary depending on the cooling water inlet temperature.*
	Allow system to stabilise.
	Repeat Recordings of:
	- condenser pressure, $P_{c}$, 
	- evaporator pressure $P_{e}$, 
	- condensing temperature $t_{6}$, 
	- evaporating temperature $t_{5}$, 
	- any other temperatures.

3. Repeat step 2 for 5-7 flow rate changes up to a maximum condenser pressure of $150 \ kN/m^{2}$ and take corresponding readings.

## Readings

[[Lab Readings - Energy Systems Coursework.csv]]

```dataviewjs
const path = "Lab Readings - Energy Systems Coursework.csv";
const csvFile = await dv.io.load(path);
const rows = csvFile.split("\n").map(row => row.split(","));
const headers = rows[0];
const data = rows.slice(1);

dv.table(headers, data);
```

## Additional Resources
%%[[2024-11-11]] @ 23:33%%

[Demonstration unit manual](https://blackboard.lincoln.ac.uk/ultra/courses/_200912_1/outline/file/_9801625_1)

## Notes

### Condenser flow rate oscillatory behaviour
%%[[2024-11-12]] @ 12:55%%

During the experiment while waiting for the system to stabilise after adjusting the condenser flow rate valve the rotameter float would observably fall and rise multiple times. It appeared there was a distinctively oscillatory process taking place. There was a significant time delay between our inputs, rising events and falling events in which the float would appear stationary. 

During the experiment the following possible factors where proposed:

1. The change in mass flow rate changes the effective thermal conductance throughout the condenser coil by several mechanisms:
   - flow rate will affect the boundary temperature differential throughout the pipe.  
   - flow rate is proportional to [[Reynolds number]] which affects boundary thermal conductance.
2. The condenser flow rate valve also effects the pressure in the condensation coil which will change the evaporating/condensing point.
3. Rapid changes in flow rate could induce pressure waves in the pipes which would be partially reflected at any elements with associated pressure changes.
4. The system is connected to the INB buildings plumbing, it could simply be observation bias that we have correlated it with our inputs. The flow rate changes could be associated with pressure drops in the buildings water system when toilets are flushed etc.

Mechanisms for the effect where proposed based on these factors

#WIP  

https://www.sciencedirect.com/science/article/pii/S1110016821004646