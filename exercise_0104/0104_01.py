class fried_chicken:
    def __init__(self,flavor,seasoning,size,time,price):
        self.flavor = flavor #炸雞口味有沒有辣
        self.seasoning = seasoning #炸雞的調味料
        self.size = size #炸雞的大中小
        self.time = time #炸雞所需要的時間
        self.price = price #炸雞的價格
    
    def display_info(self): #印出屬性
        print(f"炸雞口味: {self.flavor}")
        print(f"炸雞大小: {self.size}")
        print(f"調味料: {self.seasoning}")
        print(f"所需時間: {self.time}")
        print(f"價格: {self.price} 元")
        print(" ")
    
    def change_size(self,new_size):
        self.size = new_size  #更改炸雞大小
    def change_flavor(self,new_flavor):
        self.flavor = new_flavor #將原本的辣度改成新的辣度
    def change_price(self,new_price):
        self.price = new_price #更改成新的價錢

red_chicken = fried_chicken(flavor="小辣",seasoning="胡椒",size="中",time ="5分鐘",price ="50") #建構第一種炸雞的物件
white_chicken = fried_chicken(flavor="不辣",seasoning="不加",size="小",time ="3分鐘",price ="70") 
black_chicken = fried_chicken(flavor="小辣",seasoning="胡椒",size="中",time ="5分鐘",price ="60") 
blue_chicken = fried_chicken(flavor="中辣",seasoning="胡椒",size="大",time ="7分鐘",price ="80") 

red_chicken.display_info() #未改
red_chicken.change_size("大")
red_chicken.change_price(100)
red_chicken.change_flavor("大辣")
red_chicken.display_info() #改完以後

white_chicken.display_info() #未改
white_chicken.change_size("中")
white_chicken.change_price(50)
white_chicken.change_flavor("小辣")
white_chicken.display_info() #改完以後

black_chicken.display_info() #未改
black_chicken.change_size("小")
black_chicken.change_price(80)
black_chicken.change_flavor("中辣")
black_chicken.display_info() #改完以後

blue_chicken.display_info() #未改
blue_chicken.change_size("中")
blue_chicken.change_price(50)
blue_chicken.change_flavor("小辣")
blue_chicken.display_info() #改完以後