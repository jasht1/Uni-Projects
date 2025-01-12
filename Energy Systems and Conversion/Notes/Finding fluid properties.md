
# Finding Thermodynamic Properties

## Motivation 
There are many means of identifying fluid properties ranging in their ease and accuracy. In my university [[Energy Systems and Conversion Module]] we are taught to seek out property tables which to my 21st century mind seems an arcane practice, impractical at scale and prone to human error. As such I set out to understand the alternatives. 

## Brief
Search for means to query thermodynamic properties for fluids, that suits my preferences.
Preferably the solution would be (in order of priority):
1. Open Source / Free / Easy to pirate
2. Reasonably well documented
3. A python package
4. Simple to make queries with
5. Have a large library of material models / datasets
6. Be expandable to "custom" models


## Options

### CoolProp / PyFluids

http://www.coolprop.org/

| Condition                                              | Rating |                                                                     |
| ------------------------------------------------------ | ------ | ------------------------------------------------------------------- |
| **Open Source / Free / Easy to pirate**                | +++++  | [Source](https://github.com/CoolProp/CoolProp)                      |
| **Reasonably well documented**                         | ++++   | [Docs](http://www.coolprop.org/coolprop/wrappers/Python/index.html) |
| **A python package**                                   | +++++  | [Wrapper](https://github.com/portyanikhin/PyFluids/tree/main)       |
| **Simple to make queries with**                        | +++    |                                                                     |
| **Have a large library of material models / datasets** | +++++  |                                                                     |
| **Be expandable to "custom" models**                   | +++++  |                                                                     |

This is a FOSS C++ implementation of [[#REFPROP]] functionality both high and low level. It has wrappers for anything your likely to want to use and the documentation while a bit of nest isn't half bad. 

### Pyromat
%%[[2024-10-11]] @ 16:53%%

http://pyromat.org/

| Condition                                              | Rating |                                               |
| ------------------------------------------------------ | ------ | --------------------------------------------- |
| **Open Source / Free / Easy to pirate**                | +++++  | [Source](https://github.com/chmarti1/PYroMat) |
| **Reasonably well documented**                         | +++++  | [Docs](http://pyromat.org/documentation.html) |
| **A python package**                                   | +++++  |                                               |
| **Simple to make queries with**                        | +++++  |                                               |
| **Have a large library of material models / datasets** | ++     |                                               |
| **Be expandable to "custom" models**                   | -      |                                               |

Simple and lightweight, 90% of the time this could be my go to.

Further notes on [[PYroMat]]

### REFPROP
%%[[2024-11-18]] @ 19:37%%

https://www.nist.gov/srd/refprop

Found by reading [this excellent lecture](https://unit.aist.go.jp/riem/club/flowm/flowclub/13_2017/2017_13_4.pdf) from the NIST. Seems like the real deal, if NASA's using it.

| Condition                                              | Rating |                                                                                      |
| ------------------------------------------------------ | ------ | ------------------------------------------------------------------------------------ |
| **Open Source / Free / Easy to pirate**                | -      | [Source](https://github.com/portyanikhin/PyFluids/tree/main)                         |
| **Reasonably well documented**                         |        | [Docs](http://www.coolprop.org/coolprop/wrappers/Python/index.html)                  |
| **A python package**                                   | +++    | [Wrapper](https://github.com/usnistgov/REFPROP-wrappers/tree/master/wrappers/python) |
| **Simple to make queries with**                        |        |                                                                                      |
| **Have a large library of material models / datasets** | +++++  |                                                                                      |
| **Be expandable to "custom" models**                   |        |                                                                                      |

https://trc.nist.gov/refprop/MINIREF/MINIREF.HTM

### EES
%%[[2024-11-18]] @ 18:37%%

https://fchartsoftware.com/ees/

Is a general engineering software package with some thermodynamics property querying functionality based on [[#REFPROP]]. It comes with some materials ([List of fluid models](https://fchartsoftware.com/ees/eeshelp/fluid_property_information.htm)) and can import NISTs .fld format for thermodynamic properties. 

| Condition                                              | Rating |                                                                      |
| ------------------------------------------------------ | ------ | -------------------------------------------------------------------- |
| **Open Source / Free / Easy to pirate**                | -      | [Licence](https://fchartsoftware.com/ees/academic-site-licenses.php) |
| **Reasonably well documented**                         | -      | [Youtube](https://fchartsoftware.com/ees/youtube.php)                |
| **A python package**                                   | -      |                                                                      |
| **Simple to make queries with**                        |        |                                                                      |
| **Have a large library of material models / datasets** | -      |                                                                      |
| **Be expandable to "custom" models**                   | ++     |                                                                      |
