import socket           #引入socket模組

HOST = "10.3.141.1"    #把port設成樹莓派的IP，port隨意
PORT = 8000

SocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #定義SocketA,宣告TCP
SocketA.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SocketA.bind((HOST, PORT))      #設置接入的HOST和PORT
SocketA.listen(5)               #設置最大等候數為5

print('Server started at: %s:%s' % (HOST, PORT))

while True:                                 #設置while true循環,讓loop無限循環直到強制停止
    print('Waiting for connection...')
    Connection, Address = SocketA.accept()  #從server端接收串接的對象和IP
    print('Connected by ' + str(Address))   #把串接成功的IP打印出來

    while True:
        indata = Connection.recv(1024)      #設變量,儲存串接對象傳來的資料,size為1024
        if indata.decode() == "EXIT":       #設置結束串接的條件,即當對象傳來EXIT時，宣告closed connection
            print(str(Address) +" closed connection")
            break                           #打斷循環
        print(str(Address) +': ' + indata.decode()) #收到對象傳來的信息後,先decode後在打印出來讓使用者看到
        outdata = 'echo:' + indata.decode()         #設變量,decode剛剛收到的信息,存起來
        Connection.send(outdata.encode())           #把outdata encode,在發送回去, 回饋給使用者,讓使用者知道傳到server的信息