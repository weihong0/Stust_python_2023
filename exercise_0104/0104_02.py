class emploter:
    def __init__(self,name,workyear,worktime): #建立屬性 名子 年資 工時
        self.name = name
        self.workyear = workyear
        self.worktime = worktime

    def display_info(self): #顯示全部的屬性
        print(f"名子: {self.name}")
        print(f"年資: {self.workyear} 年")
        print(f"工作時數: {self.wortime} 小時")

    def query_name(self): #查詢名子
        print(f"名子: {self.name}")

    def query_wrokyear(self): #查詢年資
        print(f"年資: {self.workyear} 年")

    def query_worktime(self): #查詢工作時數
        print(f"工作時數: {self.worktime} 小時")

    def salary(self): #計算該員工的工資
        salary = self.worktime * 183
        print(salary)
    
    def add_worktime(self,worktime): #增加員工的工作時數

        self.worktime = self.worktime + worktime

    def reduce_worktime(self,worktime): #減少員工的工作時數

        self.worktime = self.worktime - worktime

class drink:
    def __init__(self,name,price,hot_or_cold): #建立飲料物件
        self.name = name
        self.price = price
        self.hot_or_cold = hot_or_cold

    def display_info(self): #顯示全部的屬性
        print(f"名稱:{self.name}")
        print(f"價錢:{self.price}元")
        print(self.hot_or_cold)

    def change_name(self,new_name):#更改飲料名稱
        self.name = new_name

    def change_price(self,new_price):#更改飲料價錢
        self.price = new_price  
    def change_sugar(self,new_sugar):#更改糖度
        self.sugar = new_sugar
class colddrink(drink):#繼承drink類別
    def __init__(self,name,price,hot_or_cold,ice,sugar): #寫出所需要的屬性
        super().__init__(name, price, hot_or_cold) #父類有的類別寫在這
        self.ice = ice 
        self.sugar = sugar

    def display_info(self): #顯示全部的屬性
        super().display_info()
        print(self.ice) 
        print(self.sugar)
    
class hotdrink(drink):
    def __init__(self,name,price,hot_or_cold,sugar):#寫出所需要的屬性
        super().__init__(name, price, hot_or_cold)#父類有的類別寫在這
        self.sugar = sugar

    def display_info(self): #顯示全部的屬性
        super().display_info() 
        print(self.sugar)
    
work1 = emploter(name="小明", workyear=2, worktime=20) #建構第一個員工資料
work2 = emploter(name="小美", workyear=1.5, worktime=25)
work3 = emploter(name="阿德", workyear=0.5, worktime=15)

black_tea = colddrink(name="紅茶", price=25, hot_or_cold="冰的", ice="少冰", sugar="半糖")
milkblack_tea = hotdrink(name="紅茶牛奶",price=60,hot_or_cold="熱的",sugar="微糖")
green_tea = colddrink(name="綠茶", price=30, hot_or_cold="冰的", ice="微冰", sugar="少糖")
black_tea.change_name("綠茶")
black_tea.change_price(50)
black_tea.change_sugar("全糖")


#work1.query_name()
#work1.query_worktime()
#work1.query_wrokyear()
#work1.salary()
#work1.add_worktime(10)
#work1.salary()
#work1.reduce_worktime(5)
#work1.salary()