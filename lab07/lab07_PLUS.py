class Animal():                               #建立名為Animals的class
    def __init__(self, weight, mood):         #建立及定義Attribute(weight,mood)
        self.weight = weight
        self.mood = mood
    def feed(self):                           #定義feed method，但暫時沒用到，就pass
        pass
    def walk(self):                           #同上
        pass
    def bath(self,n_bath):                    #定義bath method,因為每個動物洗澡就扣2分mood
        self.mood = self.mood - 2 * n_bath

class Dogs(Animal):                           #建立子類別Dogs
    def __init__(self, weight, mood):         #同樣建立Attribute(weight,mood)
        super().__init__(weight, mood)        #沿用父類別的Atrribute定義
    def feed(self,n_feed):                    #定義feed method
        self.weight = self.weight + 0.2 * n_feed
        self.mood = self.mood + 1 * n_feed
    def walk(self,n_walk):                    #定義walk method
        self.weight = self.weight - 0.2 * n_walk
        self.mood = self.mood + 2 * n_walk
    def bath(self,n_bath):                    #沿用父類別的bath method
        super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath): #定義函式：Dogs類別計算weight和mood的method
        self.weight = self.weight + 0.2 * n_feed - 0.2 * n_walk
        self.mood = self.mood + 1 * n_feed + 2 * n_walk - 2 * n_bath
        print("狗狗現在的體重=",self.weight,"kg，心情",self.mood)

"""-----------------------------------以上與基礎題步驟相同---------------------------------------------------------------"""

class Shiba(Dogs):                            #建立屬於Dogs的子類別Shiba
    def __init__(self, weight, mood):         #同上，建立且定義Attribute(weight,mood)
        super().__init__(weight, mood)
    def feed(self,n_feed):                    #定義屬於Shiba的feed method
        self.weight = self.weight + 0.3 * n_feed
        self.mood = self.mood + 5 * n_feed
    def walk(self,n_walk):                    #沿用父類別的walk method
        super().walk(n_walk)
    def bath(self,n_bath):                    #沿用父類別的bath method
        super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath): #定義函式：Shiba類別計算weight和mood的method
        self.weight = self.weight + 0.3 * n_feed -  0.2 * n_walk
        self.mood = self.mood + 5 * n_feed +  2 * n_walk - 2 * n_bath
        print("柴犬現在的體重=", self.weight, "kg，心情", self.mood)
    def mood_constraint(self, constraint):     #建立函式檢查mood值的範圍，引入變量constraint作為限制值
        self.constr = constraint
        if self.mood > self.constr:            #若mood大於constraint,則令mood最大只能為constraint值
            self.mood = self.constr
            print("所以，柴犬現在的心情",self.mood)
        print("mood最高只能為=",self.constr)     #告知使用者：mood最高只能為輸入的constraint值

shiba = Shiba(5, 70)                           #定義shiba屬於Shiba類別，並附上初始的weght和mood值
shiba.printf(20, 10, 3)                        #引用計算Shiba體重和心情的函式，並附上feed,walk,bath的次數
shiba.mood_constraint(90)                      #引入一個constraint值到函式，利用函式判斷mood是否在constraint內
shiba = Shiba(5, 70)                           #多打印一次，配合題目截圖範例要求
shiba.printf(20, 10, 3)                        #多打印一次，配合題目截圖範例要求
shiba.mood_constraint(300)                     #同上，引入constraint值