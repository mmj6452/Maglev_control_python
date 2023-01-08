import math
import numpy as np
import control as ct
import control
import matplotlib.pyplot as plt


# Non-Linear Modeling Parameter
mu0=4*math.pi*(10^(-7))
R=7*2
N=365*2
A=0.01*0.25*2
g=9.8
M=50/3
z0=0.005 # Operating point 5 mm is the reference gir gap.
zref=0.005
dz0=0
i0=3.83; # Operating current is 3A
z_speed = 0
noise = 0
u = 0
s = control.tf('s')

gap_p = 1500*15
gap_i = 2500
gap_d = 125
Cs = gap_p + gap_i/s + gap_d*s

Aems = np.array([[0,1],[1/M*mu0*N*N*A/2*i0*i0/(z0*z0),0]])
Bu = np.array([[0],[-1/M*mu0*N*N*A/2*i0/(z0*z0)]])
Cu =np.array([1,0])
Bw =np.array([[0],[1/M]])


z_accels = control.ss(Aems,Bu,Cu,0)
z_accels_tf = ct.ss2tf(z_accels)
print(z_accels_tf)
z_speeds = z_accels/s
z_pos = z_speeds/s

z_pos_feedback = z_pos/(1+z_pos)


z = z_pos_feedback

response = ct.step_response(z)
plt.plot(response.time, response.outputs)
plt.show()

mag,phase,omege = control.bode(z_pos)
  # Bode phase plot
plt.show()
count = control.nyquist_plot(z_pos)
plt.show()