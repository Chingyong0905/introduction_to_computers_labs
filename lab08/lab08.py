import os                                   #引入os模組
MainPath=os.getcwd()                        #用變數儲存當前路徑
ListA=MainPath.lstrip("/").split("/")       #用.lstrip把路徑最前面的/去除，然後用split把/作為分隔號，儲存成ListA
ListB=os.listdir("/home/E94117013/")        #用ListB儲存當下路徑的所有檔名

print(ListA,sep=os.linesep)                 #用sep作為分隔號，並轉至下一行(.linesep)
print(ListB)

TextPath = 'E94117013.txt'                  #建立文檔的路徑
f = open(TextPath, 'w')                     #用變數f表示對TextPath路徑寫入文檔的動作

j=0                                         #以j為計數器
for i in ListA:                             #以i對應listA的元素數量
    f.write(ListA[j]+os.linesep)            #將list里對應j的位置的元素寫入Text文檔，並轉至下一行
    j+=1
f.write(os.linesep)                         #應題目要求，空多一行

j=0                                         #同上，對listB作同等步驟
for i in ListB:
    f.write(ListB[j]+os.linesep)
    j+=1
f.close()                                   #結束寫入文檔的動作