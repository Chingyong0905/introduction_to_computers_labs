"""部分功能在sever.py已經簡述,這裏僅註釋client專用功能部分"""
import socket

HOST = "10.3.141.1" #設置和Server一樣的host和port
PORT = 8000

SocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SocketB.connect((HOST, PORT))   #與server端產生串接

while True:         ##設置while true循環,讓loop無限循環直到強制停止
    OutData = input('please input message: ')   #讓使用者輸入信息
    print('send: ' + OutData)                   #打印出來使用者發出的信息
    SocketB.send(OutData.encode())              #把信息encode後通過socket發出去
    if OutData=="EXIT":                         #設置結束串接的條件,即當使用者輸入EXIT時，宣告closed connection
        SocketB.close()
        print('server closed connection.')
        break                                   #打斷while loop

    InData = SocketB.recv(1024)                 #設變量,儲存server傳來的消息,並打印出來
    print(InData.decode())