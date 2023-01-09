import math
import numpy as np
import control as ct
import control
import matplotlib.pyplot as plt


# Linear Modeling Parameter
mu0=4*math.pi*(10^(-7)) # Permeability of free space
R=7*2 #Resistance is 7 ohms
N=365*2 # Number of turns is 365
A=0.01*0.25*2 # Area of the maglev is 0.01m^2
g=9.8 # Gravity
M=50/3 # Mass of the maglev is 50kg
z0=0.005 # Gap is 5mm
i0=3.83; # Operating current is 3A
z_speed = 0 # Initial speed of the maglev
noise = 0 # Initial noise
u = 0 # Initial input
s = control.tf('s')  # Laplace variable

# PID Controller
gap_p = 1500*15
gap_i = 2500
gap_d = 125
Cs = gap_p + gap_i/s + gap_d*s

# State Space Model
Aems = np.array([[0,1],[1/M*mu0*N*N*A/2*i0*i0/(z0*z0),0]])
Bu = np.array([[0],[-1/M*mu0*N*N*A/2*i0/(z0*z0)]])
Cu =np.array([1,0])
Bw =np.array([[0],[1/M]])
z_accels = control.ss(Aems,Bu,Cu,0)

# Transfer Function Model
z_accels_tf = ct.ss2tf(z_accels)
print(z_accels_tf)
z_speeds = z_accels/s
z_pos = z_speeds/s
z_pos_feedback = z_pos/(1+z_pos)

# Step Response
response = ct.step_response(z_pos_feedback, T=np.linspace(0, 10, 1000))
plt.plot(response.time, response.outputs)
plt.show()

# Bode Plot and Nyquist Plot
mag,phase,omege = control.bode(z_pos)
plt.show()
count = control.nyquist_plot(z_pos)
plt.show()