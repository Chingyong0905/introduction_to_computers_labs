import json

def Permutation(ListInput):     #建立函式，能夠產生一組數字的全排列
    M = len(ListInput)
    if M <=1:                   #如果只有一個數字時，無法排列，回傳這個數字
        return [ListInput]
    containerA = []             #設一個空list作為容器，儲存所有排列組合
    for i,Value in enumerate(ListInput):    #enumerate功能是產生list的value和對應index
        #先選定第i位固定不動，接下來要處理是第i位以外的數字排列
        n = ListInput[:i]+ListInput[i+1: ]  #list中取出從開始到第i位前，加從第i+1位到結束
        for m in Permutation(n):            #把剛剛第i位以外的數列，再遞歸回函式，固定下一位
            containerA.append([Value]+m)    #把一開始的第i位合併餘下的排列組合，加進預設的容器
    return containerA                       #回傳容器的排列

def BF(input): #建立函式，引入input的list，輸出最小cost和最佳assignment排列
    AgentNum = []
    for a in input:
        AgentNum.append(input.index(a))     #讀input，得出這個input有多少個Agent要被分配，把序號存到AgentNum
    #print(AgentNum)    #檢查
    AgentPerm=Permutation(AgentNum)         #把agent的序號list丟進函式產生所有排列組合
    #print(AgentPerm)   #檢查
    CostPerm = []
    containerB = []
    for i in AgentPerm:                     #對每一個新產生的序號組合，用loop讀取出對應的cost組合，存到containerB
        k = 0
        for j in i:
            containerB.append(input[k][j])  #往container加入input的第k行的第j號元素
            k += 1
        CostPerm.append(list(containerB))   #再把每一個cost組合append到CostPerm儲存
        #print(containerB)  #檢查
        containerB.clear()                  #這裏要記得clear containerB的元素，這樣上一個loop的數據才不會帶去下一個loop
    #print(CostPerm)    #檢查
    CostSum = []
    for i in CostPerm:                      #用loop把CostPerm裏每一個cost組合的逐一總和，append到CostSum
        # print(sum(i)) #檢查
        CostSum.append(sum(i))
    #print(min(CostSum))    #檢查
    Index = CostSum.index(min(CostSum))     #設變量儲存最小的cost的位置，等下會用到

    assignment=AgentPerm[Index]             #用Index(最小的cost的位置)，呼出對應的worker組合，存在變量assignment
    cost=min(CostSum)                       #用變量cost儲存最小的cost總和
    return assignment,cost

with open('input.json', 'r') as inputFile:  #從file讀取input的部分，僅引用助教程式，則不贅述
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input
        assignment, cost = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()