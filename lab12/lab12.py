# https://data.gov.tw/dataset/6832
#111年臺南市醫院一覽表
import pymysql    #引入模組
import requests
import json

html = requests.get("https://soa.tainan.gov.tw/Api/Service/Get/a31f9af7-a9ef-4004-a448-a3f2e9415e92")  #從網站get資料
html.encoding = "UTF-8"
DictA = json.loads(html.text)      #把獲取的資料，轉為Dict儲存
Data = DictA["data"]               #取DictA中key為Data的value，此時形態為list，但每個元素形態都為dict
    
for dict in Data:                  #用dict逐個暫存Data裏每個元素(type:dict)
    listV = list(dict.values())    #用listV把資訊儲存起來，每一個元素都對應資料表的每一行
    #print(listV)
  
    connect_db = pymysql.connect(host='localhost', port=3306, user='e94117013',
                                 passwd='147369159357', db='wordpress', charset='utf8')  #設置連線環境
    
    with connect_db.cursor() as cursor:
        cursor.execute("""INSERT INTO 111年臺南市醫院一覽表 VALUES(%s,%s,%s,%s,%s)""",(listV[2],listV[3],listV[4],listV[5],listV[6]))
#連線後，在mysql遊標中輸入INSERT指令以及把listV的每一個元素讀進去
        
        connect_db.commit()      #提交請求
#        cursor.execute("""DELETE FROM 111年臺南市醫院一覽表""")    #這兩行只是方便編輯的時候刪除整個資料表的數據
#        connect_db.commit()
    connect_db.close()            #關閉SQL連線
    listV.clear()
