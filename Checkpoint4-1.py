import matplotlib.pyplot as plt
import math
import numpy as np

"""
Reading Text File
"""
def callfile(): #takes no argument
    filename = input("Input file name : ")
    filein = open(filename, "r") # Open file for reading
    input_data = filein.readlines() # Read in data as list of strings
    return input_data

"""
Calculating logPower
"""
def logPower(V, I): #takes two arguments Voltage and Current
    P = float(V) * float(I) #applying the formula P=VI
    logP = math.log(P)
    return logP

"""
Main function
"""
def main():
    VIlist = [] #an empty list that will contain list of strings that each strings contain the values of V and I together as one string
    for line in callfile(): #forming a for loop while applying the function, callfile()
        line[:-1] # This removes the last character which is "\n"
        VIlist.append(line[:-1]) #adding each String values into the empty list VIlist
    # print(VIlist)
    newVI = [] #an empty list that will contain a new list of strings but values of V and I being splited hence returning two seperate strings of V & I
    for j in range(0, len(VIlist)):
        split = VIlist[j].split(' , ') #spliting the strings by the string of ' , '
        newVI.append(split) #adding each String values into the empty list newVI
    # print(newVI)
    logPdata = [] #an empty list that will contain list of values of logPower
    for i in range(0, int(len(VIlist))):
        if("." in newVI[i][0]): #to ignore the comment in sample.txt file
            logP = logPower(newVI[i][0], newVI[i][1]) #applying the function logPower(V, I)
            logPdata.append(logP) #adding each logPower values into the empty list logPdata
    lengthP = len(logPdata) #number of plots = length of logPdata
    # print(logPdata)
    # print(lengthP)
    tdata = np.linspace(0.0, (1/(25*(10**3)))*lengthP, lengthP) #A list that will contain the range of time which is at a rate of 25kHz
    print(tdata)
    plt.plot(tdata, logPdata, "y") #plotting graph P(t) against t
    plt.xlabel("t/s") #labelling x axis
    plt.ylabel("log of Power") #labelling y axis
    plt.grid(True)
    plt.title("p(t) over the supplied range of t") #assigning title for the plot
    # plt.autoscale(enable = True, axis = "both", tight = None)
    plt.axhline(y=0, color = "r") #drawing y axis
    plt.axvline(x=0, color = "b") #drawing x axis
    plt.show()

main() #running the Main Function
