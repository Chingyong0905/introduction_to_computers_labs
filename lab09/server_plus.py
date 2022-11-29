"""部分基本的連接client、收發信息功能已經在sever.py簡述過,這裏僅註釋thread專用功能部分"""
import socket
from threading import Thread        #引入本題的關鍵：Tread模組

HOST = "10.3.141.1"
PORT = 8000

def init():                 #定義函數,讓功能集中且可以被重複使用,這裏是在設置程式初始環境
    global SocketC
    SocketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SocketC.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SocketC.bind((HOST, PORT))
    SocketC.listen(5)
    print('Server started at: %s:%s' % (HOST, PORT))

def accept_client():        #定義函數：與client產生串接
    while True:             #這裏用while true loop讓以下功能重複執行
        print('Waiting for connection...')
        Connection, Address = SocketC.accept()
        print('Connected by ' + str(Address))
        """#這裏設置變量t,開一條子線程,執行message_handle函數,且用到的變量為串接對象和對象IP"""
        t=Thread(target=message_handle,args=(Connection,Address))
        t.start()           #開始執行t

def message_handle(Connection,Address): #定義函數：用作處理收發信息功能,開了子線程後接下來就會執行這函數
    while True:
        InData = Connection.recv(1024)
        if InData.decode() == "EXIT":   #定義接收對象結束串接的條件
            print(str(Address) +" closed connection")
            break
        print(str(Address) +': ' + InData.decode())
        OutData = 'echo:' + InData.decode()
        Connection.send(OutData.encode())

if __name__=="__main__":    #設置程式的入口，說明以下代碼将開始被运行
    init()
    accept_client()