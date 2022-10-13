import random as r                      #引入隨機模組，命名為r

Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}
list1 = list(Times.keys())              #將Times字典所有key組合成一個新的list

for i in range(1000000):                #for-loop循環1000000次
    KeyRandom=list1[r.randint(0,5)]     #從6個數字(0到5)裏隨機出現一個，並用這個數字對應list1裏位置的元素，並將元素暫存在變量KeyRandom
    Times[KeyRandom]=Times[KeyRandom]+1 #將KeyRandom作為檢索key，在字典找到對應的value並+1

for j in range(6):          #將字典裏的每個value換算成小數二位的%，並for-loop循環6次，分別輸出6個點數的機率
    print("The probability of",list1[j],"is",round(Times[list1[j]]/10000,2),"%")
