def gcd(a,b):
    listNUM = []                        # 創建一個list暫存除數a與被除數b
    listNUM.append(a)                   # 變數暫存在list，令listNUM=[a,b]
    listNUM.append(b)

    if listNUM[0] * listNUM[1] == 0:    # 用a*b==0來剔除a=0或b=0的可能性
        print("0沒有gcd")
    else:                               # 當a或b都不為0,才進入求公因數的過程
        while listNUM[1] != 0:
            i = listNUM[0] % listNUM[1]  # 輾轉相除法：將0號位(a)作為被除數，1號位(b)作為除數，將餘數暫存在變數i
            del listNUM[0]  # 將0號位的數據刪掉
            listNUM.append(i)  # 將餘數i添加進list，重回loop直到0號位為0
        '''簡言之，以上loop實現輾轉相除的方式為：[a,b]-->[b,餘數1]-->[餘數1,餘數2]----->[最大公因數,0]，此時listNUM[0]為最大公因數'''
        if listNUM[0] == 1:  # 如果最大公因數為1，此時為互質
            print(a, "和", b, "互質")
        else:
            print(a, "和", b, "的gcd=", listNUM[0])  # 如果最大公因數不為0也不為1，此時正常輸出
    return (a,b)

ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)