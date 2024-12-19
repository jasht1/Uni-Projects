### Comparison of Simulink and Matlab implementation
%%[[2024-12-19]] @ 12:50%%

Simulink is a visual block based user interface for MATLAB, the visual nature can help maintain a big picture intuition that can get lost in code. This can be especially helpful in larger organisations that need to collaborate and communicate with more stakeholders especially when communicating to non programmers. 
That there are differences in the default workflows and as such some things are easier to do in one than the other. Most users will find a balance of the two and frequently use both in any given project. Functions from MATLAB scripts can easily be called in a Simulink `.slx` and so too outputs from Simulink simulations are accessible in scripts through MATLABs powerful shared "workspace" system.

The modelling for this project was done both in Simulink and MATLAB scripts. It's worth noting that MATLAB results can differ when running the same simulation in `Discrete-time` vs `Continous-time` and by default Simulink tends to handle simulations in continuous time. Similarly by default Simulink will handle time itself but in a tightly integrated project it can be important to use a specific shared time vector between sections handled in scripts and Simulink simulations. When this was taken into account the results achieved by both methods where Identical.

> [!FIGURE] Figure 3: Passive Suspension Simulink Diagram ^passive-simulink
> ![[passive suspension simulink diagram.png]]

> [!FIGURE] Figure 4: Active Suspension Simulink Diagram ^active-simulink
> ![[active suspension simulink diagram.png]]
