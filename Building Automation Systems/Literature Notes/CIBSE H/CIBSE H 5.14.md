## 5.14 Natural ventilation

#### Summary
  Avoid using AC, utilise passive heat/cooling/ventilation sources. Passive sources can be actively controlled, but not as accurately, however occupants accept this.

 
 - solar shading and fenestration design to reduce solar gains  
 - use of daylighting and high efficiency lamps to reduce internal gains from lighting  
 - high thermal mass construction with exposed internal mass to give a thermal flywheel effect  
 - design features to enhance natural ventilation flow, such as atria and ventilation stacks  
 - user involvement, often by openable windows.
 
 "CIBSE Applications Manual AM10(40) sets out the principles of successful design; a summary is given in Good Practice Guide GPG 237(41)."
 
 "occupants in naturally ventilated buildings are more tolerant of temperature variations than their counterparts in air conditioned buildings, particularly if there is some form of user control in the form of openable windows."
 
 "Controlled devices for natural ventilation consist primarily of modulating inlet and outlet ventilation openings"

  In this context "controlled devices" typically refer to actuators that open/close ventilation openings.
 
 "Consideration must be given to the performance of the openings in rain and wind."
 
 "consideration must be given to any compromise of building security"

### 5.14.2 Measurement devices

#### Summary
  Basically just says read chapter 3.
  
  Sensors may monitor the following
  
  external conditions:
  - Temperature
  - Wind
  - Sun
  - Rain
  
  and/or internal conditions:
  - Temperature
  - CO_2
  - Occupancy
 
 
 - External air temperature: this forms an essential input for natural ventilation control systems. The sensor should be mounted on the north face of the building and be provided with a radiation shield against solar and sky radiation.  
 - Rain intensity sensors: these are fitted so that windows and vents may be shut automatically to prevent rain ingress. For a large building it may be advisable to mount sensors at opposite ends to detect approaching rain.  
 - Wind speed: windows and vents may be shut or partially closed at high wind speeds to avoid damage or to control over-ventilation. If combined with a rain sensor, wind speed sensors can be used to give protection against driving rain ingress.  
 - Wind direction: this can be used to select windward or leeward vents as appropriate.  
 - Solar radiation: a solar radiation sensor may be used to increase ventilation rates at times of high solar gain or to automatically control the operation of solar screens or window blinds.  
 - Slab temperature: the building fabric plays an essential part in passive temperature control and some natural ventilation control strategies use a measure of fabric temperature rather than internal air temperature. The sensor should be inserted to a depth of approximately 25 to 50 mm into the slab, packed with thermal paste and cemented in. As a less satisfactory alternative, a surface mounted sensor, covered with insulation, may be used. A 5-54 Building control systems  position should be chosen on an internal wall or ceiling remote from temperature disturbances.  
 - CO2 concentration: this can be used as a set point  for ventilation control in addition to internal air temperature and is of value in buildings with a large but variable occupancy.  
 - Occupation: the number of people in the controlled space may be used to set the target ventilation rate. This is feasible where the building has controlled entry and exit; in an integrated system it may be possible to obtain information from the security system.


### 5.14.3 Control strategies

#### Summary
  - The primary aim of a ventilation system is to regulate CO2 concentration and dissipate heat gains. These are directly associated with occupation.
  - There is a trade off between energy usage and controllability.
  - It is typical to have different control strategies for occupation period vs night period.

 "The level of occupation may be used to estimate the rate of CO2 production and hence the required ventilation."
 
 "The use of night ventilation to dissipate heat gains acquired during the heat of the day and to precool the building fabric is an important strategy in avoiding the use of mechanical cooling and it is possible to keep the internal temperature below daytime external ambient temperature by this means."
 
 "Where modulating control of natural ventilation openings is provided, it will not be possible to use fast acting control loops to try and achieve more accurate control."
 
 "The target air quality is typically a CO2  concentration below a set point of 1000 ppm."
 
 "Bringing in outside air at a higher temperature than the internal zone temperature will result in a heat gain, and there is an argument that vents should be closed to minimise the ingress of warm outside air. However, this does not allow for the effect of internal heat gains which will tend to increase the inside temperature to a level above that outside. In general it will be more effective to use warm outside air for ventilation than to allow the gains to build up inside without ventilation."

### 5.14.3.2 Night cooling

#### Summary
  Utilise thermal mass to provide cooling during the day by pre-cooling it during the night.

 "The aim of night cooling is to use ventilation during the unoccupied period to dissipate heat gains absorbed by the building during the day."
 
 "The recommended control strategy simply uses ventilation to bring the zone temperature down to the lower limit of the comfort band, i.e. as low as possible without bringing the heating system into action."

### 5.14.4 Mixed-mode

#### Summary
  Mixed mode systems use natural & mechanical ventilation.

 ![figure-131-x32-y450.png](attachments/warburtonP2009-BuildingControlSystems/figure-131-x32-y450.png)
 Key
  **Mode** : **Description**  
  Heating : Ventilation openings closed Floating Vents maintain position 
  Safe : Vents moved to safe position in wind etc. 
  Maximum : Vents fully open 
  Normal : Vents modulate to control Tz and CO2
  
  **Symbol** : **Meaning** : **Typical value**  
  $T_{oa}$ : Outside air temperature  
  $T_{z}$ : Zone temperature  
  $T_{cool}$ : Cooling set point : 22 °C  
  $T_{heat}$ : Heating set point : 19 °C  
  $T_{low}$ : Cold outside air : 12 °C  
  $CO_{2}$ : Carbon dioxide : 1000 ppm

 
 - Contingency: this describes a building that has been designed primarily for natural ventilation, with the provision for the addition of mechanical services later if found necessary.  
 - Zoned: some zones of the building are provided with mechanical services where there is a specific requirement. An example might be a building with naturally ventilated office spaces, a mechanically ventilated kitchen area and an air conditioned computer room.  
 - Complementary: both natural ventilation and mechanical services serve the same zone. The systems may be operated in either changeover or concurrent mode. Concurrent systems often provide a basic level of mechanical ventilation to ensure a permanent draught free ventilation air supply, while allowing occupants to open windows as they choose. Changeover systems operate in distinct modes to satisfy different requirements. For example, windows may be openable in mild weather, but locked shut when mechanical plant is used for either heating or cooling. Changeover systems present practical problems of producing effective control strategies and ensuring that occupants are fully conversant with the different requirements of the various modes of operation.
