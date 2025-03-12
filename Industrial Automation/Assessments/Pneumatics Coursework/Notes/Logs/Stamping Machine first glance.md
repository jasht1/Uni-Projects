
## First glance at Appendix 1
%%[[2025-02-27]] @ 00:05%%

> [!quote] [Appendix 1](Appendix%201.md)
> ![Appendix 1](Appendix%201.md)

### Actuators

1A, 2A & 3A are all clearly pneumatic cylinders / pistons.

**1A**: A single acting spring return cylinder would be sufficient for the task as described. It wouldn't need to be particularly large as it only needs force sufficient eject a block from the magazine and clamp it against the opposing wall.

**2A**: Again A single acting spring return cylinder would be sufficient for the task as described. This would however have to have a high out-stroke force sufficient to stamp the block.

**3A**: Again A single acting spring return cylinder would be sufficient for the task as described. This could be pretty small so as to be fast acting as little force would be required.

### Sensors

The activation of **1A** & **2A** need to be known, 
- this could be sensed by position sensors.
	One on **1A** to detect when it is in clamped position, and one on **2A** to detect when it is retracted.

Detecting Stamping
- A pressure trip valve could be used to detect stamping

### Control 

Actuating **3A**
- A Pneumatic delay valve would be useful to allow **2A** time to retract the stamp before **3A** is actuated.
	https://tameson.co.uk/pages/pneumatic-time-delay-valve

### Process

At the beginning of a cycle:
1. **1A** is actuated, 
2. Once **1A** as reached clamping position,
3. **2A** is actuated,
4. Once **2A** has reached stamping position,
5. **2A** is retracted,
6. **1A** is retracted,
7. Once **1A** & **2A** are clear,
8. **3A** is actuated 
9. Once block is clear,
10. **3A** is retracted
End of cycle

### Logic
%%[[2025-03-05]] @ 16:09%%

![Stamping Flow Chart](Stamping%20Flow%20Chart.md)