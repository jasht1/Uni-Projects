# Rough prototype
## Supplies needed
- H-bridge
- wheels
- 9v batteries
- [x] #Project get supplies for [[ImechE project#Rough prototype]] 📅 2023-02-16 ✅ 2023-03-24


# Design
## Physical design
### Distance sensor mount
The distance sensor needs to stay pointed directly upwards in order to get accurate readings.
Will need to test if simply mounting it to the datum disk is good enough or if a weighted datum is needed
### Drive 
Drive needs to transmit the power form the motor effectively into vertical lift
**Considerations**
- uneven drive causing torsion & jamming robot diagonally / adding friction.
- uneven drive could throw off distance sensor by twisting robot chassis
- higher wheel pressure against walls increases drive friction
- lower wheel pressure could cause slipping & reduce lifting ability
## Electrical design
### Drive
L298n has limited current delivery this reduces the motors starting torque & holding torque.

## Software design
### Motion
function that takes a single INT input and controls motor speed & direction

### Positional awareness
#### ultrasonic sensor
- [ ]  ultrasonic sensor read function [[ImechE project]]
#### limit switch
#### light sensor
%%### timing / wheel travel estimation (probably not necessary)%%


# Progress logs
## Initial prototyping
### Testing with L298n & 9V batteries
- [x] cut new motor wire and resolder [[ImechE project]] 📅 2023-03-26 ✅ 2023-03-27
- [x] Get motor spin [[ImechE project]] ✅ 2023-03-29
### Sensor_Distance() & Sensor_LDR() always returning 0 as well as limit switch interrupt not working
[[2023-03-31]]
All the sensors where wired to the 5v regulator off the 18 V power supply which was not switched on 
The interrupt was tied to pin 4 of the arduino uno but only pins 2 & 3 have [[Interupts#Arduino Interrupts|Hardware interrupt]] capability
### integrating sensors into movement script
[[2023-03-31]]
Wrote a basic function to drive upwards at full speed until within 40 cm then progressively decelerate with distance & stop when limit switch is hit.
- Next step 
### Next steps
- Test current usage with different power sources
- 