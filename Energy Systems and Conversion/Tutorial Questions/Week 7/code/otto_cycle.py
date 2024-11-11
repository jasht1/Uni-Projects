import pyromat as pm

air = pm.get('ig.air')

## Intake
t_intake = 290.15
p_intake = 1

v_intake = air.v(t_intake, p_intake)

## Compression
compression_ratio = 8
v_tdc = v_intake/compression_ratio
pt_ratio = pow(compression_ratio ,air.gam(t_intake, p_intake)-1)

## TDC (pre ignition)
t_tdc = t_intake*pt_ratio
p_tdc = p_intake*pt_ratio

v_tdc=air.v(T=t_tdc, p=p_tdc)

## Ignition
v_ignition=v_tdc+800
u_ignition=air.e(T=t_tdc, p=p_tdc)+800
t_ignition=air.T(e=u_ignition, v=v_ignition)
