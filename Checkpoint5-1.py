import math
import matplotlib.pyplot as plt
import numpy as np

"""
Calculates solution to the trajectory problem using
the Euler method, including the
velocity dependence of the drag force.
"""
def projectile(v, theta, Cd, dt):
    g = 9.81
    x=[0] # zero array
    y=[0] # zero array
    vel_x=[v*np.cos(np.radians(theta))] #initial condition
    vel_y=[v*np.sin(np.radians(theta))] #initial condition

    for i in range(0, 10000): #euler method
        velocity = np.sqrt(vel_x[i]**2 + vel_y[i]**2)
        velx = vel_x[i] - (Cd * velocity * vel_x[i] * dt) #calculating the value of horizontal components of the velocity at each point
        vel_x.append(velx)
        vely = vel_y[i] + (- g*dt - Cd * velocity * vel_y[i] * dt) #calculating the value of horizontal components of the velocity at each point
        vel_y.append(vely)
        xx = x[i] + vel_x[i] *dt #calculating the value of horizontal components of the position at each point
        x.append(xx)
        yy = y[i] + vel_y[i] *dt #calculating the value of vertical components of the position at each point
        y.append(yy)
        if yy < 0.0 or xx < 0.0: #stops the looping when the position of horizontal or vertical is zero
            break
    # print(x[-1], y[-1])
    return x,y #returning the list of horizontal position and vertical position

"""
Calculates the final velocity using
the Euler method, including the
velocity dependence of the drag force.
"""
def project(v, theta, Cd, dt):
    g = 9.81
    # xx, yy = 0.0,0.0
    x=[0] # zero array
    y=[0] # zero array
    vel_x=[v*np.cos(np.radians(theta))] #initial condition
    vel_y=[v*np.sin(np.radians(theta))] #initial condition
    for i in range(0, 100000): #euler method
        velocity = np.sqrt(vel_x[i]**2 + vel_y[i]**2)
        velx = vel_x[i] - (Cd * velocity * vel_x[i] *  dt) #calculating the value of horizontal components of the velocity at each point
        vel_x.append(velx)
        vely = vel_y[i] - (g + Cd * velocity * vel_y[i]) * dt #calculating the value of vertical components of the velocity at each point
        vel_y.append(vely)
        xx = x[i] + vel_x[i] *dt #calculating the value of horizontal components of the position at each point
        x.append(xx)
        yy = y[i] + vel_y[i] *dt #calculating the value of vertical components of the position at each point
        y.append(yy)
        if yy <= 0.0: #stops the looping when the position of horizontal or vertical is zero
            break
    velocity = np.sqrt(vel_x[-1]**2 + vel_y[-1]**2) #calculating the final velocity useing vertical and horizontal compoenets of velocity
    # print(vel_y[-1])
    return velocity #returns the final velocity

"""
Calulates the Final Kinetic Energy
"""
def energyRatio(v, Cd, dt):
    thetadata = [0.0] #Creating the List of θ from 0.0 to 90.0
    theta = 0.0
    while theta <90.0: #applying the while loop to generate the the θ
        theta = float(theta) + (0.5)
        thetadata.append(theta)
    # thetadata = np.linspace(0.0, 90.0, 180)
    finalvelocity = []
    for i in range(0, len(thetadata)): #extracting the final velocity for each θ value
        finalvelocity.append(project(v, thetadata[i] ,Cd, dt))
    finalSq = []
    for i in range(0, len(finalvelocity)): #squaring every final velocity
        finalsquare = finalvelocity[i]**2
        finalSq.append(finalsquare)
    # print(finalSq)
    KEratio = []
    for i in range(0, len(finalSq)): #calculating the energy ratio
        ratio = finalSq[i] / float(10**2)
        KEratio.append(ratio)
    return thetadata, KEratio #returning the list of θ and list of Kinetic Energy ratio

"""
Main Function,
Plotting two graphs which are
#1. Trajectory of a Projectile
#2. Ratio of final kinetic energy to initial kinetic energy against launch angle θ
"""
def main():
    #1
    velocity1, theta1, Cd1, dt1 = [float(x) for x in input("What are the values of velocity, theta, Cd, dt? : ").split(' ')] #prompt values
    velocity2, theta2, Cd2, dt2 = [float(x) for x in input("What are the values of velocity, theta, Cd, dt? : ").split(' ')] #prompt values
    x1, y1 = projectile(velocity1, theta1, Cd1, dt1) #applying the values when θ = 60.0 drag coefficent = 0.3
    x1_w2, y1_w2 =  projectile(velocity2, theta2, Cd2, dt2) #applying the values when θ = 45.0 drag coefficent = 0.0

    #plot trajectories until ball hits ground (i.e for y>=0 & x>=0)
    fig = plt.figure()
    plt.plot(x1,y1, x1_w2, y1_w2)
    ax = fig.add_subplot(111)
    ax.set_title("Trajectory of a projectile", family='monospace',size=14, weight='bold')
    ax.set_xlabel("x (m)") #labelling x axis
    ax.set_ylabel("y (m)") #labelling y axis
    ax.set_ylim(bottom=0)
    ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
    ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)
    ax.legend(("Drag Constant = 0.3, θ = 60.0", "Drag Constant = 0.0, θ = 45.0" ),fontsize=12)
    ax.annotate("Local Maximum", xy= (x1[y1.index(max(y1))], max(y1)), xytext = (x1[y1.index(max(y1))], max(y1) + 0.3), arrowprops=dict(facecolor='black', shrink=0.05))
    # ax.annotate("Local Maximum", xy= (x2[y2.index(max(y2))], max(y2)), xytext = (x2Onod, gamma, n_point = [float(x) for x in input("What are the values of OmegaZero, Gamma & Number of Points? : ").split(' ')][y2.index(max(y2))], max(y2) + 0.3), arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate("Local Maximum", xy= (x1_w2[y1_w2.index(max(y1_w2))], max(y1_w2)), xytext = (x1_w2[y1_w2.index(max(y1_w2))], max(y1_w2) + 0.1))
    plt.show()

    #2
    print("Now we Calculate the Energy Ratio against launch angle" )
    velo1, Cd21, dt21 = [float(x) for x in input("What are the values of velocity, Cd, dt? : ").split(' ')] #prompt values
    velo2, Cd22, dt22 = [float(x) for x in input("What are the values of velocity, Cd, dt? : ").split(' ')] #prompt values
    xe1, ye1 = energyRatio(velo1, Cd21, dt21) #applying the values when drag coefficent = 0.02
    xe2, ye2 = energyRatio(velo2, Cd22, dt22) #applying the values when drag coefficent = 0.3
    #plot the Kinetic energy ratio against launch angle
    plt.plot(xe1, ye1, xe2, ye2)
    plt.xlabel("theta/θ") #labelling x axis
    plt.ylabel("KEf/KEi") #labelling y axis
    plt.grid(True)
    # plt.legend(("Drag Constant = 0.02", "Drag Constant = 0.3" ),fontsize=12)
    plt.title("Ratio of final kinetic energy to initial kinetic energy against lauch angle θ") #assigning title for the plot
    # plt.autoscale(enable = True, axis = "both", tight = None)
    # plt.axhline(y=0, color = "r") #drawing y axis
    # plt.axvline(x=0, color = "b") #drawing x axis
    plt.show()

main() #running main function
