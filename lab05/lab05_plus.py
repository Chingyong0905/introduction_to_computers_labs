dict0={}                                            #建立空字典

for i in range(4):                                  #已知需要輸入4組數據，使用for-loop搭配range，讓loop循環4次
    keyIn=input("Enter keys:")                      #建立變量keyIn，暫存Input的數據
    valueIn=input("Enter values:")                  #建立變量valueIn，暫存Input的數據

    dict0[keyIn]=valueIn.split()                    #將每一次的input的key和value加入空字典，並使用split把輸入的數值自動分隔開並形成list

print("dict0=",dict0)                               #輸出字典

"""---------------------------------------------------------以下同lab05基礎題步驟--------------------------------------------------------------------"""

sumA=0                                           #建立變量sumA，記錄學生A成績的總和
for k in dict0["StuA"]:                          #用for-loop:將dict0里第一個key，即StuA對應的value,裏面的5個成績加起來
    sumA=(sumA+int(k))
print("A學生的平均成績：",sumA/5)                   #把sumA除以5，打印出學生A的平均成績

sumB=0                                           #學生B同上
for k in dict0["StuB"]:
    sumB=(sumB+int(k))
print("B學生的平均成績：",sumB/5)

sumC=0                                            #學生C同上
for k in dict0["StuC"]:
    sumC=(sumC+int(k))
print("C學生的平均成績：",sumC/5)


l=0
for l in range(5):                                #以l為計數器，以for-loop搭配range，循環5次
    avr_Sub=(int(dict0["StuA"][l])+int(dict0["StuB"][l])+int(dict0["StuC"][l]))/3    #同樣的l值在三個學生的value list中，對應著的同樣科目，總和後除以3，得到單科平均成績
    print(dict0["index"][l],"的平均成績：",avr_Sub)                     #打印單科平均成績
    l+=1