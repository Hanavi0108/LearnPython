"""
-------------------------------------------------
   File Name：     TempComp
   Description :    Calculate Temperature Compensation Correction
   Author :       Hanavi
   date：          2023/2/11
-------------------------------------------------
   Change Activity:
                   2023/2/11: New
-------------------------------------------------
"""
import math
import matplotlib.pyplot as plt
import numpy as np


ISA = 15  # 摄氏度
Lo = 0.00198  # -0.0065  # 摄氏度/米
To = 288.15  # K

h_list = []

def SimCrt(H, Hss, t_ad): #飞机相对机场的高度，机场标高，机场温度
    t0 = t_ad + Lo * Hss
    Crt = H * (ISA - t0) / (273 + t0 - 0.5 * Lo * (H + Hss))
    return Crt

def AcCrt(Elevation, Hp_ad, Hp_ac, t_ad):  # 机场标高，跑道入口标高，飞机相对机场的高度，机场温度
    Tdiff = t_ad - (ISA - Lo * Elevation) # 机场温度相对于ISA的偏差
    Crt = (-Tdiff / Lo) * math.log(1 + Lo * Hp_ac / (To + Lo * Hp_ad))
    return (Crt)

# while True:
#     MA = int(input('请输入最低高度(ft)：') )# 最低高度
#     airportAltitude = int(input('请输入机场标高(ft)：') )# 机场标高
#     airportTemp = int(input('请输入机场温度（℃）：')) # 机场温度
#
#     print('\n')
#     print('简单公式结果为：' + str(SimCrt(MA - airportAltitude, airportAltitude, airportTemp)))
#     print('复杂公式结果为：' + str(AcCrt(airportAltitude, airportAltitude, MA - airportAltitude, airportTemp)) )
#     print('----------------------------------------------'+ '\n')

#相对高度比较
h_acrt = [0] * 20
h_scrt =  [0] * 20
hcount = 0
Altitude = range(200, 2200, 100)
for i in range(200, 2200, 100):
    h_scrt[hcount] = SimCrt(i, 10, -10)
    h_acrt[hcount] = AcCrt(10, 10, i, -10)
    hcount += 1
#
#
# 温度比较
# t_acrt = [0] * 15
# t_scrt =  [0] * 15
# tcount = 0
# Temps = range(-40, 35, 5)
# for i in Temps:
#     t_scrt[tcount] = SimCrt(1500, 10, i)
#     t_acrt[tcount] = AcCrt(10, 10, 1500, i)
#     tcount += 1


# 机场标高比较
# ad_scrt = [0] * 21
# ad_acrt =  [0] * 21
# adcount = 0
# ad_altitude = range(0, 10500, 500)
# for i in ad_altitude:
#     ad_scrt[adcount] = SimCrt(1500, i, -30)
#     ad_acrt[adcount] = AcCrt(i, i, 1500, -30)
#     adcount += 1

#作图
plt.rcParams["font.sans-serif"]=["STZhongsong"]

# fig = plt.figure(figsize=(12,4))
# fig1 = fig.add_subplot(121)
# fig2 = fig.add_subplot(122)
#
# fig1.plot(Altitude, h_scrt, label='简单算法')
# fig1.plot(Altitude, h_acrt, label='精确算法')
# fig1.scatter(1500, 82.8, c='r', marker='p')
# fig1.legend()
# fig1.grid()
# fig1.set(xlabel='飞机高度(ft)',ylabel='补偿量(ft)',title='补偿量随高度变化值（机场标高为0ft，机场温度为0℃）')
#
# fig2.plot(Temps, t_scrt, label='简单算法')
# fig2.plot(Temps, t_acrt, label='精确算法')
# fig2.legend()
# fig2.grid()
# fig2.set(xlabel='温度(℃)',ylabel='补偿量(ft)',title='补偿量随温度变化值（机场标高0ft，飞机高度1500ft）')
#----
def mystep(x, y, ax=None, where='pre', **kwargs):
    assert where in ['post', 'pre']
    x = np.array(x)
    y = np.array(y)
    if where == 'post': y_slice = y[:-1]
    if where == 'pre': y_slice = y[1:]
    X = np.c_[x[:-1], x[1:], x[1:]]
    Y = np.c_[y_slice, y_slice, np.zeros_like(x[:-1]) * np.nan]
    if not ax: ax = plt.gca()
    return ax.plot(X.flatten(), Y.flatten(), **kwargs)


x = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000]
y = [30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 290]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.step(x, y, color="w", linestyle='--',
         lw=1, where='post')
mystep(x, y, color="k", lw=1.5, where='post')


for i, j in zip(x[:-1], y):
    ax.text(x=i + 0.5, y=j + 3, s=j)
#----
# plt.show()

plt.plot(Altitude, h_scrt, label='简化公式结果')
plt.plot(Altitude, h_acrt, label='精确公式结果')
plt.legend()
plt.grid()
plt.xlabel('飞机相对机场的高度(ft)')
plt.ylabel('修正量(ft)')
plt.title('修正量随飞机相对机场高度变化图' + '\n' + '（机场标高为10ft，机场温度为-10℃）')
plt.show()

# plt.plot(ad_altitude, ad_scrt, label='简化公式结果')
# plt.plot(ad_altitude, ad_acrt, label='精确公式结果')
# # table_value = [280] * 21
# # plt.plot(ad_altitude, table_value, label='查表结果', c='k')
# plt.legend()
# plt.grid()
# plt.xlabel('机场标高(ft)')
# plt.ylabel('修正量(ft)')
# plt.title('修正量随机场标高变化图' + '\n' + '（飞机相对机场高度为1500ft，机场温度为-30℃）')
# plt.show()