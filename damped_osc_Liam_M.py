#damped_osc.py
#code to plot damped oscillators

#imports:
import numpy as np
import matplotlib.pyplot as plt


#constants:
A_0 = .2        
k = 2.50
m = .125
nat_freq = np.sqrt(k/m)                 #natural frequency
Q_ud = np.array([8,2])
Q_cd = np.array([1/2])
#Q_od = 

#calculate natural angular frequency
 

#underdamped constant calculations
gamma_ud = np.divide(nat_freq, Q_ud)
omega_ud = np.sqrt(nat_freq**2-np.power((gamma_ud/2),2))
P_ud = np.divide((2*np.pi),omega_ud)                            #periods (the # here makes this a comment)
phi_ud =  np.arctan2(-gamma_ud,(2*omega_ud))
A_ud = A_0*nat_freq/omega_ud                           # amplitude constant of the oscillator ('C_1' in class)

#critically damped
gamma_cd = nat_freq/Q_cd
omega_cd = 0
#P_cd = # 2pi/omega_cd will go to infinity

#overdamped
#gamma_od = 
#omega_od = 
#P_od = 
#phi_od =  

#time settings for plot
tmin = 0
tmax = 2*np.min(P_ud)
nstep = 5000

#set up time array
t = np.linspace(tmin, tmax, nstep)

### oscillator eqns ###

#underdamped
A_ud_0 = A_ud[0]*np.exp(-gamma_ud[0]*t/2)*np.cos(omega_ud[0]*t + phi_ud[0])
A_ud_1 = A_ud[1]*np.exp(-gamma_ud[1]*t/2)*np.cos(omega_ud[1]*t + phi_ud[1])
#underdamped approx
A_ud_ap_0 = A_0*np.exp(-gamma_ud[0]*t/2)*np.cos(omega_ud[0]*t)    #_ud_ap_0 means underdamped approx Q_ud[0]
A_ud_ap_1 = A_0*np.exp(-gamma_ud[1]*t/2)*np.cos(omega_ud[1]*t)
#critically-damped
x_crit = A_0*np.exp(-gamma_cd[0]*t/2)*(1+gamma_cd/(2)*t)



#plot x vs t
plt.clf()
plt.plot(t, A_ud_0, linestyle = '-', color = 'black', label = 'Q = ' + str(Q_ud[0]))
plt.plot(t, A_ud_0, linestyle = '-', color = 'orange', label = 'Q = ' + str(Q_ud[0]))
plt.plot(t, x_crit, linestyle = '-', color = 'purple', label = 'Q = ' + str(Q_cd[0]))
plt.plot(t, A_ud_ap_0,  color = 'black', label = 'Approximation', linestyle = ':')
plt.plot(t, A_ud_ap_1, color = 'orange', label = 'Approximation', linestyle = ':')
plt.axhline(y=0, linestyle = ':')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.show()

#HW problem 3
# omega_0 = np.sqrt(6400/.250)
# 0.85A_0 = np.exp(gamma*t/2)
# solve for gamma gives gamma = ln(0.85)/(-5*60) to convert t into seconds
# Q = omega_0/gamma ~= 150000

# (initial E - E at 0.85A_0)/intital E
# ends up as 1-0.85**2 which equals 0.2775