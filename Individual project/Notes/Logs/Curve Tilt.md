
## Investigating curve tilt operation
%%[[2024-12-08]] @ 22:53%%

The `auto subtract baseline` function includes an option to apply a tilt. I will investigate the implications of this and where this might be an appropriate correction.

### Description of the tilt function
%%[[2024-12-09]] @ 22:48%%

The tilt operation when using `Heat Height` as the X channel, and `Vertical Deflection` as the Y channel, will apply a rotational transformation by subtracting an offset to each data point. The offset is given by a linear function who's gradient is a fixed "correction coefficient" in $\text{pN}/\micro \text{m}$. 

### Implications of the tilt function
%%[[2024-12-09]] @ 23:02%%

When this gradient of the offset function is positive the curve is rotated clockwise, and when negative anti clockwise. When the curve is rotated clockwise the gradient is increased, implying a greater force per distance deflected i.e. stiffer and therefore a higher [[Young's modulus]]. When rotated anticlockwise, the gradient is reduced, implying less force per distance deflected i.e. more flexible and therefore a lower [[Young's modulus]].

### When is tilting useful?
%%[[2024-12-09]] @ 23:25%%

