import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    filename = input("Input file name : ")
    filein = open(filename, "r")
    input_data = filein.readlines()

    VIlist = []
    for line in input_data:
        line[:-1]
        VIlist.append(line[:-1])

    newVI = []
    for j in range(0, int(len(VIlist))):
        newVI.append(VIlist[j].split(' , '))

    logPdata = []
    for i in range(0, int(len(VIlist))):
        if("0." in newVI[i][0]):
            P = float(newVI[i][0]) * float(newVI[i][1])
            logP = math.log(P)
            logPdata.append(logP)
    lengthP = len(logPdata)
    print(lengthP)
    tdata = np.linspace(0.0, (1/(25*(10**3)))*lengthP, lengthP)

    plt.plot(tdata, logPdata, "y")
    plt.xlabel("t/s")
    plt.ylabel("log(P)/ log W")
    plt.grid(True)
    plt.title("p(t) over the supplied range of t")
    plt.axhline(y=0, color = "r")
    plt.axvline(x=0, color = "b")
    plt.show()

main()

# def main():
#     filename = input("Input file name : ")
#     filein = open(filename, "r")
#     input_data = filein.readlines()
#     VIlist = []
#     for line in input_data:
#         # if line[0]
#         line[:-1]
#         VIlist.append(line[:-1])
#     logPdata = []
#     # print(VIlist)
#     # print(float(VIlist[0][17:31]) * float(VIlist[0][0:13]))
#     # print(math.log(float(VIlist[0][17:31]) * float(VIlist[0][0:13])))
#     newVI = []
#     for j in range(0, int(len(VIlist))):
#         newVI.append(VIlist[j].split(' , '))
#     # print(newVI)
#     for i in range(0, int(len(VIlist))):
#         if("0." in newVI[i][0]):
#             P = float(newVI[i][0]) * float(newVI[i][1])
#             logP = math.log(P)
#             logPdata.append(logP)
#     # logPdata.sort()
#     # print(logPdata)
#     lengthP = len(logPdata)
#     print(lengthP)
#     tdata = np.linspace(0.0, (1/(25*(10**3)))*lengthP, lengthP)
#     # tdata = np.linspace(0.0, 1/(25*(10**3)), lengthP)
#     plt.plot(tdata, logPdata, "y") #plotting graph P(t) against t
#     plt.xlabel("t/s")
#     plt.ylabel("log(P)/ log W")
#     plt.grid(True)
#     # plt.xlim(0.0, 1/(25*(10**3)))
#     plt.title("p(t) over the supplied range of t")
#     plt.axhline(y=0, color = "r")
#     plt.axvline(x=0, color = "b")
#     plt.show()
#
# main()
