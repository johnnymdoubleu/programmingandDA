import math
import matplotlib.pyplot as plt
import numpy as np


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    def magnitude(self):
        mag = math.sqrt(self.x**2 + self.y**2)

    def unitVec(self):
        if self.magnitude() != 0.0:
            self.x /= self.magnitude()
            self.y /= self.magnitude()

# def velocityVec(v, a):
#     radiany = math.cos(a*math.pi/180)
#     radianx = math.sin(a*math.pi/180)
#     vx = v * radianx
#     vy = v * radiany
#     return [vx, vy]
# def acceleration(dC, v, a):
#     ax = -1* dC * v * velocityVec(v, a)[0]
#     ay = -1 * dC * v * velocityVec(v, a)[1] - 9.81
#     return [ax, ay]
def projectile(v, theta, Cd, dt):
    """
    Calculates solution to the trajectory problem using
    the Euler method, including the
    velocity dependence of the drag force.
    """
    g = 9.81
    x=[0] # zero array
    y=[0] # zero array
    vel_x=[v*np.cos(np.radians(theta))] #initial condition
    vel_y=[v*np.sin(np.radians(theta))] #initial condition

    for i in range(0, 1499):
        velocity = np.sqrt(vel_x[i]**2 + vel_y[i]**2)
        velx = vel_x[i] - (Cd * velocity * vel_x[i] *  dt) #euler method
        vel_x.append(velx)
        vely = vel_y[i] + (- g*dt - Cd * velocity * vel_y[i] *  dt)
        vel_y.append(vely)
        xx = x[i] + vel_x[i] *dt #euler method
        x.append(xx)
        yy = y[i] + vel_y[i] *dt
        y.append(yy)
        if yy == 0.0 and xx == 0.0:
            break
    time = [0]
    for i in range(0, len(x)):
        tt = time[i] + (i+1)*dt
        time.append(tt)
    return x,y

def energyRatio(v, Cd, dt):
    thetadata = [0.0]
    theta = 0.0
    while theta <=90.0:
        theta = float(theta) + (90/1500)
        thetadata.append(theta)
    # thetadata = np.linspace(0.0, 90.0, 1500)
    velocitydata = []
    vxtheta=[]
    vytheta=[]
    initialSq = []
    finalSq = []
    for i in thetadata:
        vel_x = v * math.cos(math.radians(i))
        vxtheta.append(vel_x) #initial condition
        vel_y = v * math.sin(math.radians(i))
        vytheta.append(vel_y) #initial condition
        velocity = math.sqrt(vel_x**2 + vel_y**2)
        velocitydata.append(velocity)
        velSq = float(velocity ** 2)
        initialSq.append(velSq)
    g = 9.81
    x= [0] # zero array
    y= [0] # zero array
    for i in (0, 1499):
        for j in (0, 1499):
            velx = vxtheta[j] - (Cd * velocitydata[i] * vxtheta[j] *  dt) #euler method
            vely = vytheta[j] + (- g*dt - Cd * velocitydata[i] * vytheta[j] *  dt)
            xx = x[j] + vxtheta[j] *dt
            x.append(xx) #euler method
            yy = y[j] + vytheta[j] *dt
            y.append(yy)
            if yy == 0.0 and xx == 0.0:
                break
            return velocitydata[i]
            velSq = velocitydata[i]**2
            finalSq.append(velSq)
    # print(len(finalSq))
    print(len(initialSq))
    KEratio = []
    for i in range(0, len(initialSq)-1):
        ratio = finalSq[i] / initialSq[i]
        KEratio.append(ratio)

    return KEratio, thetadata




def main():
    # v1, theta1, Cd1, dt1 = [float(x) for x in input("Give the values of first sets of velocity, angle, darg coefficient and delta t: ").split(' ')]
    # # v2, theta2, Cd2, dt2 = [float(x) for x in input("Give the values of second sets of velocity, angle, darg coefficient and delta t: ").split(' ')]
    # x1, y1 = projectile(v1, theta1, Cd1, dt1)
    # # x1_w1, y1_w1 =  projectile(v1, theta2, Cd2, dt2)
    # # print(len(projectile(10, 45, 0.5, 0.001)[0]))
    # x2, y2 = projectile(10, 45, 0.5, 0.001)
    # x1_w2, y1_w2 =  projectile(10, 45, 0, 0.001)
    thetadata = [0.0]
    theta = 0.0
    while theta <=90:
        theta = theta + (90/1500)
        thetadata.append(theta)
    print(math.cos(math.radians(thetadata[5])))
    # print(thetadata)
    #
    # #plot trajectories until ball hits ground (i.e for y>=0)
    # fig = plt.figure()
    # plt.plot(x1,y1, x2, y2, x1_w2, y1_w2)
    # ax = fig.add_subplot(111)
    # ax.set_title("Trajectory of a projectile", family='monospace',size=14, weight='bold')
    # ax.set_xlabel("x (m)")
    # ax.set_ylabel("y (m)")
    # ax.set_ylim(bottom=0)
    # ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
    # ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)
    # ax.legend(("Drag Constant = 0.3", "Drag Constant = 0.5", "Drag Constant = 0.0" ),fontsize=12)
    # ax.annotate("Local Maximum", xy= (x1[y1.index(max(y1))], max(y1)), xytext = (x1[y1.index(max(y1))], max(y1) + 0.3), arrowprops=dict(facecolor='black', shrink=0.05))
    # ax.annotate("Local Maximum", xy= (x2[y2.index(max(y2))], max(y2)), xytext = (x2[y2.index(max(y2))], max(y2) + 0.3), arrowprops=dict(facecolor='black', shrink=0.05))
    # ax.annotate("Local Maximum", xy= (x1_w2[y1_w2.index(max(y1_w2))], max(y1_w2)), xytext = (x1_w2[y1_w2.index(max(y1_w2))], max(y1_w2) + 0.1))
    # plt.show()

    xe1, ye1 = energyRatio(10.0, 0.02, 0.001)
    # xe2, ye2 = energyRatio(10, 0.3, 0.001)
    plt.plot(xe1, ye1)
    plt.xlabel("KEf/KEi") #labelling x axis
    plt.ylabel("theta") #labelling y axis
    plt.grid(True)
    plt.title("KEf/KEi against θ") #assigning title for the plot
    # plt.autoscale(enable = True, axis = "both", tight = None)
    plt.axhline(y=0, color = "r") #drawing y axis
    plt.axvline(x=0, color = "b") #drawing x axis
    plt.show()
main()
