
### Contact Mechanics

In order to calculate elasticity the experimental data must be fit to a theoretical mechanical model of the interaction. Below is a table outlining different model indention relationships.

![Elasticity comparison tex table](Elasticity%20comparison%20tex%20table.md)

%% Expand on obstacles with applying contact mechanics models to cells %%

%% 
Full Fung equation 
$$F = B\pi (\frac{a^5- 15Ra^4 + 75R^2a^3}{5Ra^2- 50R^2a + 125R^3})\text{exp}[b(\frac{a^3- 15Ra^2}{25R^2a- 125R^3})]$$
Thinner Fung equation
$$
\begin{align*}
N(a) &= a^5 - 15Ra^4 + 75R^2a^3 \\
D(a) &= 5Ra^2 - 50R^2a + 125R^3 \\
E(a) &= a^3 - 15Ra^2 \\
F(a) &= 25R^2a - 125R^3 \\
\\
F =\ &B\pi \left( \frac{N(a)}{D(a)} \right) \exp\left[ b \left( \frac{E(a)}{F(a)} \right) \right]
\end{align*}
$$ 
$$ \begin{align*} N(a) &= a^5 - 15Ra^4 + 75R^2a^3 \\ D(a) &= 5Ra^2 - 50R^2a + 125R^3 \\ E(a) &= a^3 - 15Ra^2 \\ F(a) &= 25R^2a - 125R^3 \\ \\ F =\ &B\pi \left( \frac{N(a)}{D(a)} \right) \exp\left[ b \left( \frac{E(a)}{F(a)} \right) \right] \end{align*} $$ 
%%

%% Better Table

%%

Given the focus of this investigation is the elastic response of the cell membrane the non contact forces are relatively small and can be ignored by reducing the fitting strictness close to the contact point. The difference between the traditional Hertzian models and the power series approximations are not significant enough to justify the increased complexity in this case.

## Literature Review

Developments in both understanding %% of the pathophysiology %% of kidney disease and the application of atomic force microscopy (AFM) technology [@liuS2024-AtomicForceMicroscopyDisease-relatedStudies; @dufreneYF2002-AtomicForceMicroscopy] may provide a valuable measure of the progression of kidney failure to inform the research and development of novel therapies [@parrishAR2016-CytoskeletonNovelTarget].

%% #### What we measure %%

%% Single cell stiffness %%
The mechanical properties of tubular cells are largely a result of their cytoskeletal structure [@jalilianI2015-CellElasticityRegulated; @radmacherM2007-StudyingMechanicsCellular] which is altered significantly with the progression of DN [@buckleyST2012-CytoskeletalRearrangementTGFv1induced]. 

%% Inter cellular adhesion %%

%% The stiffness of individual cells can be observed and correlated with the [@siamantourasE2016-QuantifyingCellularMechanics]. %%

%% #### Obstacles & limitations %%

%% Cell cultures aren't perfect representations of their in vitro counterparts. This can be improved with careful preparation. The elasticity of the substrate the culture is grown on can have a significant impact on cytoskelital arrangement [@wangD2022-KidneyProximalTubule] [loveH2018-SubstrateElasticityGoverns]  %%

%% Table with papers and a relevant summary #WIP %%

The below table lists several papers utilising atomic force microscopes to produce force displacement curves from a bead tipped cantilever fitted to a hertz contact model to find cell elasticity.

| Paper                                                               | Cell Type                                                                            | Scope                                                                                                                                                                          | Cell Elasticity                                                                           |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Siamantouras 2016 [@siamantourasE2016-QuantifyingCellularMechanics] | HK2: immortalised human kidney proximal tubule  epithelial cell culture              | Over 30 cells each indented 5 times immediately above the nucleus producing over 150 curves.                                                                                   | **control**: $320 \ \text{Pa}$ <br>cells treated with TGF-$\beta 1$: $549 \ \text{Pa}$    |
| Jafari 2024 [@jafariA2024-MechanicalPropertiesHuman]                | HEK-293: immortalised human embryonic kidney cell culture                            | did not elaborate                                                                                                                                                              | $539.8 \ \text{Pa}$                                                                       |
| Shimizu 2012 [@shimizuY2012-SimpleDisplaySystem]                    | HEK-293: immortalised human embryonic kidney cell culture                            | The median of value of over 100 cells examined at 25 points each.                                                                                                              | mode value ($x_{0}$): $410 \ \text{Pa}$ <br>variance ($w$): $0.757$                       |
| Buckley 2012 [@buckleyST2012-CytoskeletalRearrangementTGFv1induced] | A549: human lung alveolar carcinoma epithelial cell culture                          | On each cell, a $4 \times 4$ grid of force-distance curves was collected in at least 5 different positions (avoiding the nucleus and the very edge) producing over 750 curves. | On Glass: 8300 $\pm$ $1100 \ \text{Pa}$<br>On collagen I: $9100 \ \pm$ $2900 \ \text{Pa}$ |
| Wyss 2011 [@wyssHM2011-BiophysicalPropertiesNormal]                 | Sprague-Dawley rat kidney glomeruli capillary wall extracted by differential sieving | 10 different glomeruli with 10 measurements each                                                                                                                               | $2,300 \ \pm$ $160 \ \text{Pa}$                                                           |

