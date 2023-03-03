# For calculate the VNAV transition phase
# 计算VNAV transition phase数值
# author: Hanavi

import math

# import matplotlib.pyplot as plt

g = 9.8 #m/s2
kt2mps = 1.944
m2ft = 3.281
rad2deg = 57.3
nm2m = 1852
normAcc = 0.05 #normal acceleration factor

def calcT(v):
    t0 = v/(2*normAcc*g)*math.tan(3/rad2deg)
    return t0

def calcD0(v):
    d0 = v**2/(2*normAcc*g)*math.tan(3/rad2deg)
    return d0

def calcH0(v):
    h0 = v**2/(2*normAcc*g)*math.tan(3/rad2deg)**2
    return h0


for i in range(150, 551, 50):
    print(i,"\t",
          # round(calcT(i/kt2mps),2),"\t",
          round(calcD0(i / kt2mps) / nm2m,2),"\t",
          round(calcH0(i / kt2mps) * m2ft / 4),"\t",
          round(calcH0(i / kt2mps) * m2ft),"\t",
          # round(math.sqrt((i * 1.688 * 60) ** 2 + (0.03 * g * calcT(i/kt2mps) * m2ft *60)**2)),"\t",
          round(calcT(i/kt2mps) * normAcc * g * m2ft * 60)*2) # Delta VS

    # plt.plot(calcT(i/kt2mps), calcH0(i/kt2mps)*m2kt)
    # print(calcD0(i/kt2mps) / nm2m)
    # print(calcH0(150/kt2mps) * m2ft)
