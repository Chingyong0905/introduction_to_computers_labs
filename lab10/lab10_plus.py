"""由於大部分API基礎功能重疊，這裏不贅述基礎題的註解，只解釋與加分題有關的部分"""
from flask import Flask, request    #從flask引入Flask和request模組
from flask_cors import CORS
import os                           #引入os模組，以便讀寫文檔

app = Flask(__name__)  #初始設定
CORS(app)
DictA = {}                   #DictA用於儲存key-value pairs             
ListA=[]                     #ListA用於把txt的內容以串列的方式儲存
path = 'Lab10_NotePad.txt'   #設定txt的Path
"""txt檔的內容排列是key-空格-value-下一行-key...以此類推"""

f1 = open(path)              #設f1：負責把txt的內容放到ListA裏
lines = f1.readlines()       #readlines配合以下for loop可以一行一行操作，將txt全部行的內容append到ListA
for line in lines:
    #print(line)
    for i in line.split():   #每一行在處理時，由於key和value之間有空格，split去除它們之間的空格，分成兩個元素再往下執行
        ListA.append(i)      #把每一個元素加進ListA

#此時ListA的每一個元素排列為[key1,value1,key2,value2,...]
#此whileloop的概念是以j為計數器，把0號位的元素作為DictA的key1，而下一號位的元素作為value1
#接著再讓j+2，則接著執行第2號位元素放進key2...
j=0
while j < len(ListA):
    DictA[ListA[j]]=ListA[j+1]
    j+=2
#這行可以print(DictA)做檢查

# web server 路由設定
@app.route('/', methods=['GET'])    #API設定的部分已在基礎題解釋，這裏不贅述
def root1():
    return 'ok'

@app.route('/set', methods=['POST'])
def root2():
    KeyIn = request.form.get("key")
    ValueIn = request.form.get("value")
    if KeyIn in DictA:
        return "key exist"
    else:
        f2 = open(path, 'a')                          #設f2：負責把新輸入的key和value放到txt裏
        f2.write(KeyIn + " " + ValueIn + os.linesep)  #元素在txt裏的排列方式：key-空格-value-下一行-key...以此類推
        DictA[KeyIn] = ValueIn                        #更新DictA
        f2.close()
        return "set success"

@app.route('/key_list', methods=['GET'])
def root3():
    ListKey=[]              # ListKey用於儲存所有keys，以便操作
    for i in DictA.keys():  # 用forloop把DictA的每一個key加入ListKey
        if i in ListKey:
          continue
        else:
          ListKey.append(i)
    return str(ListKey)     # 回傳ListKey

@app.route('/get_value/<key>', methods=['GET'])
def root4(key):
    KeyFound = key
    if KeyFound in DictA:
        ValueFound = DictA[KeyFound]
        return ValueFound
    elif KeyFound not in DictA:
        return "key not found"


@app.route('/update_value', methods=['POST'])
def root5():
    KeyUpdate = request.form.get("key")
    ValueUpdate = request.form.get("value")
    if KeyUpdate in DictA:
        DictA[KeyUpdate] = ValueUpdate                #更新DictA
        f3 = open(path, 'w')                          #設f3：負責把已更新的DictA重新寫入txt中，這樣已更新的內容就會出現在txt
        for k in DictA:
            f3.write(k + " " + DictA[k] + os.linesep) #元素在txt的排列方式：key-空格-value-下一行-key...以此類推
        f3.close()
        return "update success"
    else:
        return "key does not exist"


@app.route('/delete/<key>', methods=['GET'])
def root6(key):
    KeyDelete = key
    if KeyDelete in DictA:
        del DictA[KeyDelete]
        f4 = open(path, 'w')                          #設f4：和f3類似，負責把已更新的DictA重新寫入txt中，這樣已刪除的內容就不會出現在txt
        for k in DictA:
            f4.write(k + " " + DictA[k] + os.linesep) #元素在txt的排列方式：key-空格-value-下一行-key...以此類推
        f4.close()
        return "delete success"
    elif KeyDelete not in DictA:
        return "key not found"


app.run(host="0.0.0.0", port=3000, debug=True)        #設定運行IP和PORT，且自動debug