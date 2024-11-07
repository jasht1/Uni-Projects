# Observability and Controllability
%%[[2024-09-30]] @ 21:26%%

[[RE Kalman Observability and Controllability Lectures.pdf]]
# Observability and Control notes

## Introduction
%%[[2024-09-27]] @ 13:17%%

### Problem Statement


### Theorem
%%[[2024-09-27]] @ 13:21%%

For a system that is:
- real, 
- continuous time, 
- n-dimensional, 
- constant, 
- linear

A full controllable system has the property: Every set of n [[eigenvalue]]s may be produced by suitable data feedback.


## Terminology, Symbols & Notations

## Concepts
### Dynamical System
%%[[2024-11-02]] @ 17:27%%

A Dynamical System $\Sigma$ is a composite object of the transition map $\phi$, and readout map $\eta$ over the sets:
- $T$ = time set, 
- $U$ = set of input values,
- $X$ = state set,
- $Y$ = set of output values,
- $\Omega$ = input functions

%%
See:
- [[RE Kalman Observability and Controllability Lectures.pdf#page=17&selection=128,0,178,12|Observability and Controllability Lectures, page 17]]
- [[RE Kalman Observability and Controllability Lectures.pdf#page=18&selection=159,0,262,3|Observability and Controllability Lectures, page 18]]
%%

#### Transition map
%%[[2024-11-02]] @ 17:47%%

The transition map $\phi$; is a function that takes the form:
$$\phi: T \times T \times X \times \Omega \to X$$
typically expressed like so:
$$\phi(t; \tau, x, \omega) = x(t)$$

%%
see:
- [[RE Kalman Observability and Controllability Lectures.pdf#page=20&selection=19,0,67,3|Observability and Controllability Lectures, page 20]]
%%

### Controllability

An event $(\tau, x)$ is controllable iff: There exists a $t \in T$ and an $\omega \in \Omega$ (both t and $\omega$ may depend on $(\tau , x)$) such that: $$\phi (t; \tau, x, \omega) = 0$$ #definition 

%%
> [!NOTE] *iff* means *if and only if*.

See:
- [[RE Kalman Observability and Controllability Lectures.pdf#page=25&selection=33,0,90,1|Observability and Controllability Lectures, page 25]]
%%

This is to say if and only if the system $\Sigma$ can be returned to it's rest state $x = 0$ from the given event $(\tau, x)$ in a finite time ($t \in T$ where $T = \Bbb R$) given a valid input $\omega$.

### Reachability
%%[[2024-11-02]] @ 18:33%%

An event $(\tau, x)$ is reachable iff: there $s \in T$ and an  $\omega \in \Omega$ (both $s$ and $\omega$ may depend on $(\tau , x)$) such that:  such that: $$x = \phi(\tau;s,0,\omega)$$ #definition 

%%
See:
- [[RE Kalman Observability and Controllability Lectures.pdf#page=25&selection=33,0,90,0|RE Kalman Observability and Controllability Lectures, page 25]]
%%

This is to say if and only if the system $\Sigma$ can be taken from it's rest state $x = 0$ to at time $s$ to the given event $(\tau, x)$ given a valid input $\omega$.