
An [energy smart appliance (ESA)](energy%20smart%20appliance%20(ESA).md) forecasts several (3-1000) possible power profiles to indicate it's flexibility to the [customer energy manager (CEM)](customer%20energy%20manager%20(CEM).md) the CEM can then signal to the ESA which profile to adhere to.

At a minimum an ESA will have profiles for:
- intended operation (IO); 
- most delayed (MD); and 
- least delayed (LD),
but ESA's that can act as power sources are also required to produce 
- most delayed production (MD_P); and 
- least delayed production (LD_P),
and those capable of frequency response also append a `frequency response indicator value` indicating a response proportional to (N-1)th power of the frequency deviation.
[@2021-PAS1878]