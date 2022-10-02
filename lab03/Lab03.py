
#不好意思助教，我上次誤會成作業是上傳程序碼截圖和結果截圖，我現在補上python原檔在github
number = input("1. Please input a number:")                      #讓使用者輸入任何數字，並設為變數number
if int(number) % 2 == 0:                                         #判斷奇偶數的規則：能被2整除為偶數，其餘(不能被2整除)則為奇數
    print("This is even number")
else:
    print("This is odd number")

FC = input("2. Please input your Student ID first character:")  #讓使用者輸入學號字母，並設為變數FC
NUM = input("3. Please input your Student ID last 8 numbers:")  #讓使用者輸入學號數字，並設為變數NUM
if int(NUM) % 2 == 0:                                           #判斷學號數字的奇偶性
    print("Your student ID number is even")
else:
    print("Your student ID number is odd")
print("Your student ID is:"+ FC + NUM)                          #將學號字母與數字合併然後輸出給使用者