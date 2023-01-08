import math
import numpy as np
import control as ct
import control
import matplotlib.pyplot as plt

s = control.tf('s')
Gs = 25/(s*s+4*s+25)
response = ct.step_response(Gs)
plt.plot(response.time, response.outputs)
plt.show()
plt.clf()


mag,phase,omege = control.bode(Gs)

#plt.semilogx(omege, mag)
#plt.subplot(2,1,1)
#plt.semilogx(omege, phase)    # Bode magnitude plot
#plt.subplot(2,1,2)
  # Bode phase plot
plt.show()
ny = control.nyquist_plot(Gs)
plt.show()