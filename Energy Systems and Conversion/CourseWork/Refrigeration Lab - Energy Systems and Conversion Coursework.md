
## Procedure
%%[[2024-11-11]] @ 11:38%%

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

