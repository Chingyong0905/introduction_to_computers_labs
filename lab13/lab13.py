import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
result = []  # 存9年的溫度
float_result = []  # 把result轉成float
years = []  # 存年份2013-2021
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 月份列表
mon_avg = []  # 存每個月的均溫
# -------------------------------讀文檔-------------------------------
path = "Temparature.txt"  # 文檔路徑
f = open(path, 'r')  # 讀文檔

for line in f:
    result.append(list(line.strip("\n").split(",")))  # 把文檔逐行讀取存在result
f.close()  # 關閉檔案
# print(result)       #檢測
# print(len(result)) #共有10個元素-->9年溫度
del result[0]  # result的第一個元素不會用到

# -------------------------------處理result,存入不同list-------------------------------
for i in range(0, 9):
    years.append(int(result[i][0]))  # 單獨把年份拿出來做成list
    del result[i][0]                 # 去除年份

for j in result:
    float_lst = list(np.array(j, dtype="float"))  # 用np函數把每個小list的元素轉成float
    float_result.append(float_lst)                # 把每個小list存進大list
# print(years)          #檢測
# print(result)         #檢測

# -------------------------------畫圖-------------------------------
for k in range(9):
    plt.plot(months, float_result[k], label=years[k])  # 根據每一年在list裏所對應的數據，畫出線段
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Months')
plt.ylabel('Temperature in Degree C')
x_major_locator = MultipleLocator(1)  # 把x軸的刻度間隔設置為1，存在變量裏
ax = plt.gca()                        # ax為座標軸的實例
ax.xaxis.set_major_locator(x_major_locator)  # 把x軸的主刻度設置為1的倍數
plt.legend(loc="lower center")        # 把label的位置放在中下方
plt.savefig('lab13_01.png')  # 儲存圖片
plt.show()


# -------------------------------計算均溫-------------------------------
for l in range(12):
    listCon = []  # 暫存容器，用於計算月份的均溫
    for m in float_result:
        listCon.append(m[l])
    mon_avg.append(sum(listCon)/9)  # 把2013到2021的氣溫list抽出每一個月，加起來除9
mon_avg = np.round(mon_avg, 2)      # 保留二位數
# print(mon_avg)    #檢測
tem_avg = round(sum(mon_avg)/12, 2)
# print(tem_avg)    #檢測

# -------------------------------畫圖-------------------------------
plt.plot(months, mon_avg, '-bo',  c='blue', mfc='r',
         mec='r')  # 用mfc改點為紅色，mec改點的邊緣顏色為紅色
for index, data in enumerate(mon_avg):                 # 要在每個點上標上數值
    plt.text(x=index+1, y=data, s=data,
             horizontalalignment='left', fontsize=10)  # 這裏讓index+1是因為要讓index對到月份

plt.axhline(tem_avg, linestyle="--",
            color='r', label='Mean of 9 Years')        # 設定均溫水平線的規格
plt.text(x=1, y=tem_avg, s=tem_avg, fontsize=10)       # 標上字體
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')

x_major_locator = MultipleLocator(1)  # 把x軸的刻度間隔設置為1，存在變量裏
y_major_locator = MultipleLocator(2)  # 把y軸的刻度間隔設置為2，存在變量裏
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)  # 把x軸的主刻度設置為1的倍數
ax.yaxis.set_major_locator(y_major_locator)  # 把x軸的主刻度設置為2的倍數
plt.ylim(16, 32)  # 配合lab要求，把y的刻度範圍設在16到32
plt.legend()
plt.savefig('lab13_02.png')  # 儲存圖片
plt.show()


# -------------------------------畫1x2圖-------------------------------
fig = plt.figure(figsize=(15, 6))
fig.add_subplot(1, 2, 1)  # 設定為1x2的圖
plt.subplot(1, 2, 1)
for k in range(9):
    plt.plot(months, float_result[k], label=years[k])  # 根據每一年在list裏所對應的數據，畫出線段
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Months')
plt.ylabel('Temperature in Degree C')
x_major_locator = MultipleLocator(1)         # 把x軸的刻度間隔設置為1，存在變量裏
ax = plt.gca()                               # ax為座標軸的實例
ax.xaxis.set_major_locator(x_major_locator)  # 把x軸的主刻度設置為1的倍數
plt.legend(loc="lower center")               # 把label的位置放在中下方


plt.subplot(1, 2, 2)
plt.plot(months, mon_avg, '-bo',  c='blue', mfc='r',
         mec='r')  # 用mfc改點為紅色，mec改點的邊緣顏色為紅色
for index, data in enumerate(mon_avg):                 # 要在每個點上標上數值
    plt.text(x=index+1, y=data, s=data,
             horizontalalignment='left', fontsize=10)  # 這裏讓index+1是因為要讓index對到月份

plt.axhline(tem_avg, linestyle="--",
            color='r', label='Mean of 9 Years')  # 設定均溫水平線的規格
plt.text(x=1, y=tem_avg, s=tem_avg, fontsize=10)  # 標上字體
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')

x_major_locator = MultipleLocator(1)  # 把x軸的刻度間隔設置為1，存在變量裏
y_major_locator = MultipleLocator(2)  # 把y軸的刻度間隔設置為2，存在變量裏
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)  # 把x軸的主刻度設置為1的倍數
ax.yaxis.set_major_locator(y_major_locator)  # 把x軸的主刻度設置為2的倍數
plt.ylim(16, 32)  # 配合lab要求，把y的刻度範圍設在16到32
plt.legend()

plt.tight_layout()  # 讓子圖之間適當排列不重疊
fig.savefig('lab13_03.png')
plt.show()
