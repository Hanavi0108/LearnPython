"""
-------------------------------------------------
   File Name：     excelPlot
   Description :
   Author :       Hanavi
   date：          2023/2/22
-------------------------------------------------
   Change Activity:
                   2023/2/22:
-------------------------------------------------
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\Train\\Desktop\\LNAVRFMVar.csv")

plt.plot(df["lon_deg"], df["lat_deg"])
plt.grid()
plt.show()