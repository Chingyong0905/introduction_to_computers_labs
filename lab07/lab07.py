class Animal():                               #建立名為Animals的class
    def __init__(self, weight, mood):         #建立及定義Attribute(weight,mood)
        self.weight = weight
        self.mood = mood
    def feed(self):                           #定義feed method，但暫時沒用到，就pass
        pass
    def walk(self):                           #同上
        pass
    def bath(self,n_bath):                    #先定義bath method,因為動物們一洗澡就扣2分mood
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

class Cats(Animal):                           #建立子類別Cats，其餘基本同上
    def __init__(self, weight, mood):
        super().__init__(weight, mood)
    def feed(self,n_feed):
        self.weight = self.weight + 0.1 * n_feed
        self.mood = self.mood + 1 * n_feed
    def walk(self,n_walk):
        self.weight = self.weight - 0.1 * n_walk
        self.mood = self.mood - 1 * n_walk
    def bath(self,n_bath):
        super().bath(n_bath)
    def printf(self, n_feed, n_walk, n_bath):
        self.weight = self.weight + 0.1 * n_feed - 0.1 * n_walk
        self.mood = self.mood + 1 * n_feed - 1 * n_walk - 2 * n_bath
        print("貓貓現在的體重=",self.weight,"kg，心情",self.mood)

dog = Dogs(4.8, 65)                             #定義dog屬於Dogs類別，並附上初始的weght和mood值
dog.printf(18, 10, 4)                           #引用計算狗狗體重和心情的函式，並附上feed,walk,bath的次數
cat = Cats(8.2, 60)                             #定義cat屬於Cats類別，並附上初始的weght和mood值
cat.printf(40, 7, 1)                            #引用計算貓貓體重和心情的函式，並附上feed,walk,bath的次數