
[[Lecture 4 - Exergy.pdf#page=16|Lecture 4 - Exergy, page 16]] - [[Lecture 4 - Exergy.pdf#page=18|page 18]]

## Question 1 - exergy without work

![[Lecture 4 - Exergy.pdf#page=16|Lecture 4 - Exergy, page 16]]

### a) rate of exergy destruction in the wall
#### Givens
$T_{1}= 20 \degree C \to 293.15 \degree K$
$T_{2}= 5 \degree C \to 278.15 \degree K$

$T_{o} = 0 \degree C \to 273.15 \degree K$

Energy flow rate:
$1100 \ W$

given:
![[exergy#Exergy of a Heat transfer process]]

Where in this case the the change in exergy is due to its destruction as no useful work is being done by the wall.

(1-(273.15)/(293.15)) * 1100 (1-(273.15)/(278.150)) * 1100 = `=(1-(273.15)/(293.15)) * 1100 -(1-(273.15)/(278.150)) * 1100`

%%$$\dot X = \left(1-\frac{293.15}{278.15}\right) \times 1100 = -59.32$$%%

### b) rate of exergy destruction total
%%[[2024-10-18]] @ 12:12%%

#### Givens
$T_{1}= 27 \degree C \to 300.15 \degree K$
$T_{2}= 5 \degree C \to 273.15 \degree K$

$T_{1}= 27 \degree C \to 300.15 \degree K$
$T_{2}= 5 \degree C \to 273.15 \degree K$
Energy flow rate:
$1100 \ W$

given:
![[exergy#Exergy change for a Heat transfer process]]

Where in this case the the change in exergy is due to its destruction as no useful work is being done by the wall.

%% (1-(300.15)/(273.150)) * 1100 = `=(1-(300.15)/(273.150)) * 1100` %%

(1-(273.15)/(300.15)) * 1100 (1-(273.15)/(278.150)) * 1100 = `=(1-(273.15)/(300.15)) * 1100 -(1-(273.15)/(278.150)) * 1100`

$$\dot X = \left(1-\frac{300.15}{273.15}\right) \times 1100 = -108.73$$

## Question 2 - exergy with work

![[Lecture 4 - Exergy.pdf#page=17|Lecture 4 - Exergy, page 17]]

#### Givens
##### Steam:
$m = 0.05 \ kg$

###### initial
$p_{1} = 1 \ MPa$
$T_{1} = 300 \degree C$

###### final
$p_{2} = 200 \ kPa$
$T_{2} = 150 \degree C$

##### Heat loss
$\dot Q = 2000 \ J$
$T_{o} = 25 \degree C$

### a) exergy of the steam at the initial and the final states
%%[[2024-10-18]] @ 15:48%%

#### Givens
##### steam:
$m = 0.05 \ kg$

###### initial
$p_{1} = 1 \ MPa$
$T_{1} = 300 \degree C$

###### final
$p_{2} = 200 \ kPa$
$T_{2} = 150 \degree C$

##### Heat loss
$\dot Q = 2000 \ J$
$T_{o} = 25 \degree C$

#### 
![[exergy#Energy balance of a closed system]]

#### Initial
%%[[2024-10-18]] @ 16:19%%

$$E_{2}-E_{1} -T_{o} (s_{2} - s_{1}) = X_{2} - X_{1} - p_{0} (V_{2} - V_{1})$$
can be rearranged to the form:
$$X_{2} = p_{o}(V_{2}-V_{1}) - T_{o}(s_{2}-s_{1}) + X_{1} +E_{2} - E_{1}$$
given that $X + E = Mu$ we can substitute:
$$E_{2} - E_{1} = M ()$$

%% Substitue for mass outside entropy to get rid of mass %%

$$X_{1} = p_{o}(V_{1}-V_{o}) - T_{o}(s_{1}-s_{o}) + M(u_{1} - u_{o})$$
$$\dot X = \dot X_{thermal} $$
$$\dot X_{thermal} = \left(1-\frac{298.15}{573.15}\right) 2000$$

`=(1-298.15/573.15) * 2000`

#### Final

$$\dot X = \left(1-\frac{298.15}{423.15}\right) 2000$$

`=(1-298.15/423.15) * 2000`

### b) exergy change of the steam
%%[[2024-10-18]] @ 15:48%%

#### Givens
$\dot X_{1} = 959.61$
$\dot X_{2} = 590.81$

#### 
