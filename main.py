import random

# 初期値の設定
class InitialPrice(object):
    # モード選択、mode=rはランダムor任意の数字で指定
    def select_mode(self):
        try:
            self.mode = int(input("Select the mode, r or initial pricer: "))
        except:
            self.mode = "r"
    
    # モードによって初期値分け
    def initial_price(self):
        if self.mode == "r":
            return random.randint(90, 200)
        if type(self.mode) == int:
            return self.mode
    
class FirstUpDown():    
    def up_down_value(self):
        self.initial_price = InitialPrice().initial_price

        print(self.initial_price)
        plus_minus_value = random.uniform(self.initial_price * 0.01, self.initial_price * 0.02)
        random_plus_minus = random.randint(0, 1)

        if random_plus_minus == 0:
            self.initial_price += round(plus_minus_value, 2)
        else:
            self.initial_price -= round(plus_minus_value, 2)
        
        print(self.initial_price)


        



if __name__ == "__main__":
    a = InitialPrice()
    a.select_mode()
    print(a.initial_price())
