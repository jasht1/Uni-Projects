# Modelling by Analysis
Mathematical models are based on first principles, including differential equations.
## Approach
2023-03-02 @ 14:32 
1. Define the system and its components.
2. Formulate the mathematical model and fundamental necessary assumptions based on basic principles.
3. Obtain the differential equations representing the mathematical model.
4. Solve the equations for the desired output variables.
5. Examine the solutions and the assumptions.
6. If necessary, reanalyse or redesign the system.
## Process
- Look up relevant physical laws (conservation principles)
- Define inputs and outputs
- Derive balance equations and establish initial conditions
- Verify existence of solutions
## Limitations
- To design systematically and verify a controller, one needs a mathematical description of the process to be controlled. 
- A model is never perfect, hence modelling errors are a fact of life. 
- Some models can be developed from first principles, others are obtained from observing the process in action. 
- Simple mechanical systems and electrical circuits lead to similar differential equations and transfer function relations – they are analogous.

## Force-Current equivalence
![[analysis system equations force-current equivelant.png]]

| current $i$     | force $f$            |
| --------------- | -------------------- |
| voltage $V$     | velocity $v$         |
| resistance $R$  | damper $\frac{1}{b}$ |
| capacitance $c$ | mass $M$             |
| inductance $L$  | spring $\frac{1}{k}$ |

# Examples
## Spring-Mass-Damper System

--- start-multi-column: ID_ekr2
```column-settings
Number of Columns: 2
Largest Column: standard
Border: off
```

![[analysis spring-damper system model.png]]

--- column-end ---

$$ F(t) = f(t) - kx - c\dot x $$

--- end-multi-column
## Two-Mass System

--- start-multi-column: ID_n6gl
```column-settings
Number of Columns: 2
Largest Column: right
Border: off
```

![[analysis two-mass system model.png]]

--- column-end ---

$$m \ddot x = f(t) - Kx +K_1(x_1-x)+C_1(\dot x_1 - \dot x)$$
$$ m_1 \ddot x_1 -K_1(x_1-x) - C_1(\dot x_1 - \dot x_1)$$

--- end-multi-column

