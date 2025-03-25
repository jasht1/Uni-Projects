
## 
%%[[2025-03-25]] @ 11:13%%

The `.jpk-force` data files can be exported as `.txt` files from the JPK Data Processing software with the following form:

> [!note] 
> I have replaced the long lists of data points with a few example rows at the start and end with the following text between:
> `..... Several thousand lines of datapoints .....`
> See [force-save-2011.03.22-18.41.44](force-save-2011.03.22-18.41.44.txt) for a full example. 

```txt
# TEXT EXPORT
# data-description.comment: no comment entry
# data-description.name: no name entry
# data-description.probe: cell 1 set point 0.5\n
# data-description.user-name: joeashton
# data-description.instrument: JPK00911-CellHesion-200
# data-description.source-software: 3.4.15
# data-description.modification-software: 6.1.198
# index: -1
# xPosition: ----
# yPosition: ----
# approachID: 2011.03.22-10.34.56-00060
# force-settings.type: relative-force-settings
# force-settings.extend-k-length: 24000
# force-settings.retract-k-length: 24000
# force-settings.extended-pause-k-length: 0
# force-settings.retracted-pause-k-length: 0
# force-settings.z-start-pause-option.type: constant-height
# force-settings.z-end-pause-option.type: constant-height
# force-settings.extend-scan-time: 11.999999999999998
# force-settings.retract-scan-time: 11.999999999999998
# force-settings.retracted-pause-time: 60.0
# force-settings.extended-pause-time: 0.0
# force-settings.data-description.comment: 
# force-settings.data-description.name: 
# force-settings.data-description.probe: 
# force-settings.data-description.user-name: 
# force-settings.data-description.instrument: 
# force-settings.data-description.source-software: 
# force-settings.data-description.modification-software: 
# force-settings.start-with-retract: false
# force-settings.control-settings-type: segment-control-settings
# force-settings.closed-loop: true
# force-settings.start-option.type: continue
# force-settings.pixel-clock.active: false
# force-settings.pixel-clock.name: 
# force-settings.ttl-outputs.pins.list: 
# force-settings.pause-before-first.type: constant-height-pause
# force-settings.pause-before-first.identifier.type: standard
# force-settings.pause-before-first.identifier.name: pause
# force-settings.pause-before-first.style: pause
# force-settings.pause-before-first.duration: 0.0
# force-settings.pause-before-first.num-points: 0
# force-settings.pause-before-first.pause-option.type: constant-height
# force-settings.pause-before-first.height-limit: NaN
# force-settings.force-baseline-adjust-settings.enabled: true
# force-settings.force-baseline-adjust-settings.interval: 1
# force-settings.force-baseline-adjust-settings.liquid: true
# force-settings.force-baseline-adjust-settings.beginOfLine: true
# force-settings.force-baseline-adjust-settings.deadtimeBeforeSamples: 100
# force-settings.force-baseline-adjust-settings.averageSamples: 100
# force-settings.line-clock.active.extend: false
# force-settings.line-clock.active.retract: false
# force-settings.relative-setpoint: 0.5550641929621267
# force-settings.relative-z-start: 5.9699999999999994E-5
# force-settings.relative-z-end: -3.0E-7
# feedbackMode: contact
# pauseBeforeFirst: 0.0
# traceScanTime: 11.999999999999998
# retraceScanTime: 11.999999999999998
# pauseAtStart: 60.0
# pauseAtEnd: 0.0
# pauseOnTipsaver: 0
# date: Tue Mar 22 17:41:56 GMT 2011
#
# segmentIndex: 0
# recorded-num-points: 24100
# segment: extend
# columns: verticalTipPosition vDeflection strainGaugeHeight height smoothedStrainGaugeHeight seriesTime time
# fancyNames: "Vertical Tip Position" "Vertical Deflection" "Head Height (measured)" "Height" "Head Height (measured & smoothed)" "Series Time" "Segment Time"
# heightMultiplier: 0.6
# heightOffset: 0.0
# sensitivity: 7.363581843930989E-8
# springConstant: 0.012233132341672661
# calibrationSlots: nominal force nominal nominal nominal elapsed elapsed
# units: m N m m m s s
#
6.97844E-5 -2.1227542E-11 6.9782254E-5 6.0452272E-5 6.978614E-5 2.5E-4 2.5E-4
6.9781156E-5 -3.0425995E-11 6.977914E-5 6.0452272E-5 6.978364E-5 7.5E-4 7.5E-4
6.9778675E-5 -3.0147256E-11 6.977914E-5 6.045074E-5 6.978114E-5 0.00125 0.00125
6.977718E-5 -1.788265E-11 6.9776026E-5 6.044922E-5 6.977864E-5 0.00175 0.00175
6.977456E-5 -1.9276357E-11 6.9776026E-5 6.044769E-5 6.977614E-5 0.00225 0.00225
..... Several thousand lines of datapoints .....
9.630276E-6 7.455889E-10 9.569021E-6 1.3861084E-5 9.569328E-6 12.04775 12.04775
9.626933E-6 7.352755E-10 9.5659125E-6 1.3859558E-5 9.566828E-6 12.04825 12.04825
9.622885E-6 7.163211E-10 9.5659125E-6 1.3858033E-5 9.564329E-6 12.04875 12.04875
9.621138E-6 7.255196E-10 9.562798E-6 1.385498E-5 9.561831E-6 12.04925 12.04925
9.62053E-6 7.486551E-10 9.559685E-6 1.3853454E-5 9.559331E-6 12.04975 12.04975

# index: -1
# xPosition: ----
# yPosition: ----
# approachID: 2011.03.22-10.34.56-00060
# force-settings.type: relative-force-settings
# force-settings.extend-k-length: 24000
# force-settings.retract-k-length: 24000
# force-settings.extended-pause-k-length: 0
# force-settings.retracted-pause-k-length: 0
# force-settings.z-start-pause-option.type: constant-height
# force-settings.z-end-pause-option.type: constant-height
# force-settings.extend-scan-time: 11.999999999999998
# force-settings.retract-scan-time: 11.999999999999998
# force-settings.retracted-pause-time: 60.0
# force-settings.extended-pause-time: 0.0
# force-settings.data-description.comment: 
# force-settings.data-description.name: 
# force-settings.data-description.probe: 
# force-settings.data-description.user-name: 
# force-settings.data-description.instrument: 
# force-settings.data-description.source-software: 
# force-settings.data-description.modification-software: 
# force-settings.start-with-retract: false
# force-settings.control-settings-type: segment-control-settings
# force-settings.closed-loop: true
# force-settings.start-option.type: continue
# force-settings.pixel-clock.active: false
# force-settings.pixel-clock.name: 
# force-settings.ttl-outputs.pins.list: 
# force-settings.pause-before-first.type: constant-height-pause
# force-settings.pause-before-first.identifier.type: standard
# force-settings.pause-before-first.identifier.name: pause
# force-settings.pause-before-first.style: pause
# force-settings.pause-before-first.duration: 0.0
# force-settings.pause-before-first.num-points: 0
# force-settings.pause-before-first.pause-option.type: constant-height
# force-settings.pause-before-first.height-limit: NaN
# force-settings.force-baseline-adjust-settings.enabled: true
# force-settings.force-baseline-adjust-settings.interval: 1
# force-settings.force-baseline-adjust-settings.liquid: true
# force-settings.force-baseline-adjust-settings.beginOfLine: true
# force-settings.force-baseline-adjust-settings.deadtimeBeforeSamples: 100
# force-settings.force-baseline-adjust-settings.averageSamples: 100
# force-settings.line-clock.active.extend: false
# force-settings.line-clock.active.retract: false
# force-settings.relative-setpoint: 0.5550641929621267
# force-settings.relative-z-start: 5.9699999999999994E-5
# force-settings.relative-z-end: -3.0E-7
# feedbackMode: contact
# pauseBeforeFirst: 0.0
# traceScanTime: 11.999999999999998
# retraceScanTime: 11.999999999999998
# pauseAtStart: 60.0
# pauseAtEnd: 0.0
# pauseOnTipsaver: 0
# date: Tue Mar 22 17:42:08 GMT 2011
#
# segmentIndex: 1
# recorded-num-points: 24000
# segment: retract
# columns: verticalTipPosition vDeflection strainGaugeHeight height smoothedStrainGaugeHeight seriesTime time
# fancyNames: "Vertical Tip Position" "Vertical Deflection" "Head Height (measured)" "Height" "Head Height (measured & smoothed)" "Series Time" "Segment Time"
# heightMultiplier: 0.6
# heightOffset: 0.0
# sensitivity: 7.363581843930989E-8
# springConstant: 0.012233132341672661
# calibrationSlots: nominal force nominal nominal nominal elapsed elapsed
# units: m N m m m s s
#
9.600273E-6 7.600835E-10 9.556576E-6 1.3850403E-5 9.53814E-6 12.05025 2.5E-4
9.60118E-6 7.405716E-10 9.553462E-6 1.3850403E-5 9.540641E-6 12.05075 7.5E-4
9.603294E-6 7.35833E-10 9.553462E-6 1.3851929E-5 9.543143E-6 12.05125 0.00125
9.60739E-6 7.553449E-10 9.553462E-6 1.3853454E-5 9.545644E-6 12.05175 0.00175
9.609459E-6 7.500488E-10 9.550348E-6 1.38565065E-5 9.548146E-6 12.05225 0.00225
..... Several thousand lines of datapoints .....
6.951171E-5 -2.903229E-11 6.951149E-5 7.1740724E-5 6.9514084E-5 24.04775 11.99775
6.951382E-5 -3.377089E-11 6.951459E-5 7.1742244E-5 6.951659E-5 24.04825 11.99825
6.9516806E-5 -2.7917326E-11 6.952082E-5 7.174377E-5 6.951908E-5 24.04875 11.99875
6.952021E-5 -1.6767686E-11 6.9523936E-5 7.17453E-5 6.9521586E-5 24.04925 11.99925
6.9521986E-5 -2.5687398E-11 6.9523936E-5 7.174682E-5 6.952408E-5 24.04975 11.99975

# index: -1
# xPosition: ----
# yPosition: ----
# approachID: 2011.03.22-10.34.56-00060
# force-settings.type: relative-force-settings
# force-settings.extend-k-length: 24000
# force-settings.retract-k-length: 24000
# force-settings.extended-pause-k-length: 0
# force-settings.retracted-pause-k-length: 0
# force-settings.z-start-pause-option.type: constant-height
# force-settings.z-end-pause-option.type: constant-height
# force-settings.extend-scan-time: 11.999999999999998
# force-settings.retract-scan-time: 11.999999999999998
# force-settings.retracted-pause-time: 60.0
# force-settings.extended-pause-time: 0.0
# force-settings.data-description.comment: 
# force-settings.data-description.name: 
# force-settings.data-description.probe: 
# force-settings.data-description.user-name: 
# force-settings.data-description.instrument: 
# force-settings.data-description.source-software: 
# force-settings.data-description.modification-software: 
# force-settings.start-with-retract: false
# force-settings.control-settings-type: segment-control-settings
# force-settings.closed-loop: true
# force-settings.start-option.type: continue
# force-settings.pixel-clock.active: false
# force-settings.pixel-clock.name: 
# force-settings.ttl-outputs.pins.list: 
# force-settings.pause-before-first.type: constant-height-pause
# force-settings.pause-before-first.identifier.type: standard
# force-settings.pause-before-first.identifier.name: pause
# force-settings.pause-before-first.style: pause
# force-settings.pause-before-first.duration: 0.0
# force-settings.pause-before-first.num-points: 0
# force-settings.pause-before-first.pause-option.type: constant-height
# force-settings.pause-before-first.height-limit: NaN
# force-settings.force-baseline-adjust-settings.enabled: true
# force-settings.force-baseline-adjust-settings.interval: 1
# force-settings.force-baseline-adjust-settings.liquid: true
# force-settings.force-baseline-adjust-settings.beginOfLine: true
# force-settings.force-baseline-adjust-settings.deadtimeBeforeSamples: 100
# force-settings.force-baseline-adjust-settings.averageSamples: 100
# force-settings.line-clock.active.extend: false
# force-settings.line-clock.active.retract: false
# force-settings.relative-setpoint: 0.5550641929621267
# force-settings.relative-z-start: 5.9699999999999994E-5
# force-settings.relative-z-end: -3.0E-7
# feedbackMode: contact
# pauseBeforeFirst: 0.0
# traceScanTime: 11.999999999999998
# retraceScanTime: 11.999999999999998
# pauseAtStart: 60.0
# pauseAtEnd: 0.0
# pauseOnTipsaver: 0
# date: Tue Mar 22 17:43:08 GMT 2011
#
# segmentIndex: 2
# recorded-num-points: 2
# segment: pause
# columns: verticalTipPosition vDeflection strainGaugeHeight height smoothedStrainGaugeHeight seriesTime time
# fancyNames: "Vertical Tip Position" "Vertical Deflection" "Head Height (measured)" "Height" "Head Height (measured & smoothed)" "Series Time" "Segment Time"
# heightMultiplier: 0.6
# heightOffset: 0.0
# sensitivity: 7.363581843930989E-8
# springConstant: 0.012233132341672661
# calibrationSlots: nominal force nominal nominal nominal elapsed elapsed
# units: m N m m m s s
#
8.734964E-5 -1.7325169E-11 8.735106E-5 4.8846436E-5 8.735106E-5 39.05 15.0
8.734948E-5 -1.9276357E-11 8.735106E-5 4.8571776E-5 8.735106E-5 69.05 45.0
```

As you can see each file contains a preamble:

```txt
# TEXT EXPORT
# data-description.comment: no comment entry
# data-description.name: no name entry
# data-description.probe: cell 1 set point 0.5\n
# data-description.user-name: joeashton
# data-description.instrument: JPK00911-CellHesion-200
# data-description.source-software: 3.4.15
# data-description.modification-software: 6.1.198
```

Followed by the indentation, indicated by `# index: -1` 