# State Space Control Coursework

## Abstract
%%[[2024-12-19]] @ 14:18%%

This study investigates the implementation of an active suspension system using state-space control to improve vehicle ride quality and passenger comfort. The performance of the active suspension was evaluated through stability analysis, bump response tests, and initial condition simulations. Compared to the passive suspension, the active system effectively eliminates a key resonance mode at 6 Hz and reduces the damping of a higher-frequency mode while maintaining system stability.

The active suspension demonstrates substantial improvements in ride dynamics, reducing body displacement and acceleration during road disturbances. In bump response tests, the system minimizes passenger-perceived displacement to less than 20% of the actual road disturbance. Similarly, initial condition simulations show a significant reduction in root mean squared (RMS) acceleration—over 70% for body disturbances and 96% for wheel disturbances—indicating enhanced disturbance recovery.

## Introduction
%%[[2024-12-14]] @ 18:29%%

The performance of vehicle suspension systems plays a critical role in ensuring passenger comfort, ride quality, and vehicle stability. Traditional passive suspension systems rely on fixed mechanical components, such as springs and dampers. While effective in many cases, these systems face inherent limitations, as their behaviour cannot adapt dynamically. An Active suspension incorporating sensors, actuators, and control algorithms to actively modify the suspension response in real time provide an opportunity to improve performance but also introduce additional complexity. This study investigates the applicability of an active suspension utilising a proportional derivative controller that would take in ride height data from a suitable sensor to dynamically adjust the system response with an actuator in parallel with a conventional passive shock system.

### Aims
%%[[2024-12-14]] @ 18:34%%

The aim of this project is to tune an active vehicle suspension using a mathematical model to improve ride quality and control. The vehicle will have independent suspension utilising an actuator in addition to the passive linear spring and damper at each wheel.

### Background
%%[[2024-11-01]] @ 00:08%%

![[State Space Background]]

## Constructing a model
%%[[2024-12-19]] @ 14:38%%

As the vehicle uses an independent suspension the behaviour will be simulated for a single wheel and a quarter of the cars mass, and will be referred to as a QC or quarter car. 
The quarter car suspension model considers two masses; the body mass ($m_\text{b}$​) and the wheel mass ($m_\text{w}$). 
The wheel is connected to the ground via a spring ($k_t$) representing tire stiffness, while the body is supported by a passive spring-damper combination ($k_s$​, $b_s$​). The system is extended with an active suspension component, which includes an actuator ($f_{s}$) that applies a control force between the wheel and the body.

![[Free Body Diagrams]]

![[Designing State Space Model]]

## System Dynamics

A state space representation will be used to model the behaviour of the system where the state variables will be the displacement and velocity of the car body and wheel.

## Implementation

![[Comparison of Methods#Comparison of Simulink and Matlab implementation]]

![[Matlab Active Suspension Implementation#Active Suspension Implementation]]


![[Passive Suspension Testing]]

![[Active Suspension Testing]]

![[Conclusions]]

