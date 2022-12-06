from flask import Flask, request  # 從flask引入Flask和request模組
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
DictA = {}          #DictA用於儲存key-value pairs

@app.route('/', methods=['GET'])
def root1():
    return 'ok'  # 發送response body 為 ok

# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟

"""本題沒有用to_dict()來轉成python dict格式，而是先設一個空字典DictA，用由於key-value pair本身是str形式，配合if-else判斷元素就可直接加進去DictA"""

@app.route('/set', methods=['POST'])  # 路由/set:負責加入新key-value pair，同時判斷key-value pair是否存在
def root2():
    KeyIn = request.form.get("key")  # 用get()函數獲取html頁面中名為key所帶的數據
    ValueIn = request.form.get("value")  # 同上
    if KeyIn in DictA:  # 判斷key-value pair是否存在
        return "key exist"
    else:
        DictA[KeyIn] = ValueIn  # 把不存在DictA的key-value pair存進來
        return "set success"


@app.route('/key_list', methods=['GET'])  # 路由/key_list:負責回傳所有已知keys
def root3():
    ListKey=[]              # ListKey用於儲存所有keys，以便操作
    for i in DictA.keys():  # 用forloop把DictA的每一個key加入ListKey
        if i in ListKey:
          continue
        else:
          ListKey.append(i)
    return str(ListKey)     # 回傳ListKey


@app.route('/get_value/<key>', methods=['GET']) # 路由/get_value/<key>:負責回傳指定key的value
def root4(key):
    KeyFound = key              #設變量儲存html裏key所表示的數據
    if KeyFound in DictA:       #判斷KeryFound是否在DictA裏，若在則回傳值
        ValueFound = DictA[KeyFound]
        return ValueFound
    elif KeyFound not in DictA:
        return "key not found"


@app.route('/update_value', methods=['POST'])# 路由/update_value:負責update指定key的value
def root5():
    KeyUpdate = request.form.get("key")     #用變量儲存輸入在網頁端key和value的值
    ValueUpdate = request.form.get("value")
    if KeyUpdate in DictA:                  #判斷KeyUpdate是否在DictA裏，若在則更新其value
        DictA[KeyUpdate] = ValueUpdate
        return "update success"
    else:
        return "key does not exist"


@app.route('/delete/<key>', methods=['GET'])# 路由/delete/<key>:負責delete指定key
def root6(key):
    KeyDelete = key             #和前幾個API類似，設變數儲存html端的key
    if KeyDelete in DictA:      #判斷KeyDelete是否在DictA裏，若在則delete它
        del DictA[KeyDelete]
        return "delete success"
    elif KeyDelete not in DictA:
        return "key not found"


app.run(host="0.0.0.0", port=3000, debug=True)  #設定運行IP和PORT，且自動debug