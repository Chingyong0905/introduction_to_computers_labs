subject=["國文","英文","數學","自然","社會"]      #創建儲存不同科目的list，以便調用，這裏稱為subject
scoreA=[]                                     #創建儲存A學生成績的list，這裏稱為scoreA
print("開始輸入A學生的成績，請依照國文、英文、數學、自然、社會的順序輸入：")

#p.s:以下loop沒有自動判別成績是否在1-100內的機制，那個做在加分題的file內
for i in subject:                             #以i為計數器，for-loop需重複5次，對應subject裏要處理的5個科目
    a=input()                                 #以變數a暫存用戶輸入的成績
    scoreA.append(a)                          #將暫存在a的這個成績加入scoreA內，進行下一個循環直至5個科目處理完畢


j=0                                           #現在成績已儲存在list，用for-loop搭配range
print("A學生成績:")
for j in range(5):                            #以j為計數器，一共5，將subject內對應的五個科目，連同scoreA里對應的成績輸出
    print(subject[j]+":"+scoreA[j],end="、")
    j+=1
print("\n")                                   #空一行，整齊一點

scoreB=[]                                     #學生B的成績輸入同學生A，這裏不贅述
print("開始輸入B學生的成績，請依照國文、英文、數學、自然、社會的順序輸入：")

for i in subject:
    b=input()
    scoreB.append(b)

j=0
print("B學生成績:")
for j in range(5):
    print(subject[j]+":"+scoreB[j],end="、")
    j+=1
print("\n")

scoreC=[]                                        #學生C的成績輸入同學生A，這裏不贅述
print("開始輸入C學生的成績，請依照國文、英文、數學、自然、社會的順序輸入：")

for i in subject:
    c=input()
    scoreC.append(c)

j=0
print("C學生成績:")
for j in range(5):
    print(subject[j]+":"+scoreC[j],end="、")
    j+=1
print("\n")

sumA=0                                           #建立變量sumA，記錄學生A成績的總和
for k in scoreA:                                 #用for-loop將scoreA內對應的5個成績加起來
    sumA=(sumA+int(k))
print("A學生的平均成績：",sumA/5)                   #把sumA除以5，打印出學生A的平均成績

sumB=0                                           #學生B同上
for k in scoreB:
    sumB=(sumB+int(k))
print("B學生的平均成績：",sumB/5)

sumC=0                                            #學生C同上
for k in scoreC:
    sumC=(sumC+int(k))
print("C學生的平均成績：",sumC/5)

print("\n")                                       #空一行，整齊一點

l=0
for l in range(5):                                #以l為計數器，以for-loop搭配range
    avr_Sub=(int(scoreA[l])+int(scoreB[l])+int(scoreC[l]))/3    #同樣的l值對應著三個學生的成績list中對應位置的同樣科目，總和後除以3，得到單科平均成績
    print(subject[l],"的平均成績：",avr_Sub)                      #打印單科平均成績
    l+=1                                                       #若完成，計數器l加一，直到l=5，即5個科目都計算完畢才結束