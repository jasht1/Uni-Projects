# Signal Processing In Theory And In Practice
##### By Joseph Ashton, SID 27047440

<br/>
<br/>
<br/>
<br/>
<br/>

![UoL_logo|500](UoL_logo.png)

<br/>
<br/>
<br/>
<br/>
<br/>

A report for the "Signal Processing and System Identification" module "IIR Filter Design Assignment and Image processing" coursework.

%% Page Break %% <div style="page-break-after: always;"></div>

## Introduction

![Introduction](Introduction.md)

### Symbols

Below is a list of the symbols used throughout this report accompanied by their common names and definitions where relevant.

![Symbols](Symbols.md) 

# Butterworth Low Pass Filter
## Theoretical Background

![Theoretical Background](Theoretical%20Background.md)

## Model

![Model](Model.md)

## Simulation

![Simulation](Simulation.md)

## Implementation

![Implementation](Implementation.md)

# Digital Signal Processing Principles


## The use of Convolutions

A convolution is a fundamental mathematical operation utilised extensively in digital systems especially in image processing. Abstractly it can refer to any operation that combines 2 functions or sets to produce a third, but in digital signal processing applications the first function/set is typically some kind of dataset while the second is often some kind of filter to be applied, in these cases the second "filter" function/set is referred to as a **kernel** often referred to as $f \ \& \ g$ respectively. The operation flips one of the inputs $g^{\circlearrowleft}$ then from the start of $f$ and $g^{\circlearrowleft}$ the output is the sum of the element-wise product of all opposing members of $f$ and $g^{\circlearrowleft}$, incrementing the overlap by one each time until the final element of each array meet.

### Sharpening

![Q2](Q2.md)

### Edge Detection

In applications such as computer vision systems it is often necessary to extract details like edges, the convolution of images with specialised kernels is a computationally effective way of extracting information like this.
![Q3](Q3.md)

## Pseudo Random Binary Sequences 

![Question 4](Projects/Uni%20Projects/Signal%20Processing/Assesments/CourseWork/Answers/Question%204.md)

# Annex

> [!note] Pole Dynamics Visuals
> The pole dynamic visuals seen in the [Theoretical Background](#Theoretical%20Background) section where generated using the following function available [here on the Git repo](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Misc/poleDynamicsVisual.m) along with the `.svg` figures produced [here](https://github.com/jasht1/Uni-Projects/tree/master/Signal%20Processing/Assesments/CourseWork/Answers/attachments).
> 

> [!note] Full $z$-domain transfer function derivation walk through
> ![Q1iii - full method](Q1iii%20-%20full%20method.md)

> [!note] Sharpening Kernel Visuals
> The kernel size and centre value visuals seen in the [Sharpening](#Sharpening) section where generated using the functions available [here](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%202%20%26%203/Q2VaryKernalSize.m) and [here](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%202%20%26%203/Q2VaryKernalCentre.m) on the Git repo along with the `.svg` figures produced [here](https://github.com/jasht1/Uni-Projects/tree/master/Signal%20Processing/Assesments/CourseWork/Answers/attachments).

> [!note] Edge Detect Visuals
> The kernel size comparison visuals seen in the [Edge Detection](#Edge%20Detection) section where generated using the function available [here on the Git repo](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%202%20%26%203/Q3SobleVarySize.m) along with the `.svg` figures produced [here](https://github.com/jasht1/Uni-Projects/tree/master/Signal%20Processing/Assesments/CourseWork/Answers/attachments).
