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
    # 初期値の取得
    def __init__(self):
        initial_price_instance = InitialPrice()
        initial_price_instance.select_mode()
        self.initial_price = initial_price_instance.initial_price()
        self.plus_minus_value = None
        self.new_price = None
    
    # 1度目の上がり(下がり)値の決定
    def up_down_value(self):
        self.plus_minus_value = round(random.uniform(self.initial_price * 0.01, self.initial_price * 0.02), 2)
        random_plus_minus = random.randint(0, 1)

        # random_plus_minusが0の時は下がり値にする
        if random_plus_minus == 0:
            self.plus_minus_value = self.plus_minus_value * -1

    def calc(self):
        self.new_price = self.initial_price + self.plus_minus_value

if __name__ == "__main__":
    a = FirstUpDown()
    a.up_down_value()
    a.calc()