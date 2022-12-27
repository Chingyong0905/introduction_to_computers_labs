import numpy as np
import matplotlib.pyplot as plt
result = []  # 作為容器暫存數據
y = []  # 存y座標
x = []  # 存x座標

# -------------------------------讀文檔-------------------------------
path = "oddExperiment.txt"  # 文檔路徑
f = open(path, 'r')  # 讀文檔

# -------------------------------處理result,存入不同list-------------------------------
for line in f:
    result.append(list(line.strip("\n").split(",")))  # 把文檔逐行讀取存在result
f.close()  # 關閉檔案
del result[0]  # result的第一個元素不會用到
# print(result)  #檢測

for i in result:  # 把暫存在result的數據分到x和y的list
    k = i[0].split()
    print(k)
    y.append(float(k[0]))  # 轉成浮點數
    x.append(int(k[1]))  # 轉成數字

# print(y)    #檢測
# print(x)    #檢測

# -------------------------------畫圖-------------------------------
plt.scatter(x, y, label="Data")  # 繪製散點圖
plt.title('oddExperiment Data')
x = np.array(x)  # 先換成array，等下才可以直接互相加減
y = np.array(y)  # 先換成array，等下才可以直接互相加減

parameter1 = np.polyfit(x, y, 1)  # 對散點圖進行一階擬合
y2 = parameter1[0]*x+parameter1[1]

parameter2 = np.polyfit(x, y, 2)  # 對散點圖進行二階擬合
y3 = parameter2[0] * x**2+parameter2[1]*x+parameter2[2]

MSE1 = round(np.mean(np.square(y2 - y)), 5)  # 計算一階的LSE，並近似至5位數
# print(MSE1) #檢測

MSE2 = round(np.mean(np.square(y3 - y)), 5)  # 計算二階的LSE，並近似至5位數
# print(MSE2) #檢測

corr_matrix = np.corrcoef(y, y2)  # 計算一階的R2
corr1 = corr_matrix[0, 1]
R_sq1 = round(corr1**2, 5)
# print(R_sq1)    #檢測

corr_matrix = np.corrcoef(y, y3)  # 計算二階的R2
corr2 = corr_matrix[0, 1]
R_sq2 = round(corr2**2, 5)
# print(R_sq2)   #檢測

plt.plot(x, y2, color="y", label="Fit of degree 1, LSE = "+str(MSE1))
plt.plot(x, y3, color="g", label="Fit of degree 2, LSE = "+str(MSE2))
plt.plot(x, y2, color="r", label="Fit of degree 1, R2 = "+str(R_sq1))
plt.plot(x, y3, color="m", label="Fit of degree 2, R2 = "+str(R_sq2))

plt.legend()
plt.savefig('lab13_plus.png')  # 儲存圖片
plt.show()
