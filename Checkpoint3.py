import math
import matplotlib.pyplot as plt
import numpy as np

"""
Function to Calculate the amplitude
"""
def shm(Onod, gamma, t): #fucntion to calculate the amplitue being defined & taking the arguments of OmegaZero, Gamma and time respectively
    a = 1 #given that a = 1
    if gamma > 2 * Onod: #Case 1 when over damped
        p = math.sqrt(((gamma**2)/4)-(Onod**2))
        b = gamma/(2*p)
        x = math.exp(-(gamma*t/2))*((a*math.cosh(p*t)) + (b*math.sinh(p*t)))
        return x #displacement
    elif gamma == 2 * Onod: #Case 2 when critically damped
        b = gamma / 2
        x = math.exp(-(gamma*t/2))*(a+(b*t))
        return x #displacement
    else : #Case 3 when under damped
        b = gamma / (2 * Onod)
        Omega = math.sqrt(Onod**2 - ((gamma**2)/4))
        x = math.exp(-(gamma*t/2))*((a*math.cos(Omega*t)) + (b*math.sin(Omega*t)))
        return x #displacement
"""
Main Function
"""
def main(): #main fucntion being defined
    Onod, gamma, n_point = [float(x) for x in input("What are the values of OmegaZero, Gamma & Number of Points? : ").split(' ')] #Calling the variables
    xdata = [] #Currently an empty list that will contain the values of displacement
    tdata = np.linspace(0.0, (5*math.pi/Onod), n_point) # A list containing values of t from the range of 0 to 5pi/OmegaZero divided into n_point slices
    for t in tdata:
        x = shm(Onod, gamma, t)
        xdata.append(x)
    plt.plot(tdata, xdata, "b") #plotting graph x against t
    plt.xlabel("time/s") #labelling x axis
    plt.ylabel("displacement/m") #labelling y axis
    plt.grid(True)
    plt.xlim(0.0, (5*math.pi/Onod)) #setting x limit
    plt.title("Behaviour of a dampled Simple Harmonic Motion oscillator") #assigning title for the plot
    # plt.axhline(y=0, color = "r") #drawing y-axis
    plt.show() #make the plotting visible

main() #running the main function
