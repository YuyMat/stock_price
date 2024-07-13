import random

# 初期値の設定
# mode=rはランダムor任意の数字で指定
class InitialPrice(object):
    def __init__(self, mode):
        self.initial_price = 0

        # モード選択
        if mode == "r":
            initial_price_list = [100, 300, 500, 700, 900, 1100]
            self.choice_number = random.choice(initial_price_list)
            self.initial_price = self.decide_the_number()
        elif type(mode) == int:
            self.choice_number = mode
            self.initial_price = self.decide_the_number()
    
        print(self.initial_price)
    
    # 完全決定
    def decide_the_number(self):
        times_number = random.uniform(0.9, 1.1)
        return round(self.choice_number * times_number, 2)
    
class FirstUpDown():    
    def up_down_value(self, mode):
        self.initial_price = InitialPrice(mode).initial_price

        plus_minus_value = random.uniform(self.initial_price * 0.01, self.initial_price * 0.02)
        random_plus_minus = random.randint(0, 1)

        if random_plus_minus == 0:
            self.initial_price += round(plus_minus_value, 2)
        else:
            self.initial_price -= round(plus_minus_value, 2)
        
        print(self.initial_price)


        



if __name__ == "__main__":
    mode = input("Choose the mode, r(Random) or value：")
    first = FirstUpDown()
    first.up_down_value(mode)