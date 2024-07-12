import random

# 初期値の設定
# mode=rはランダムor任意の数字で指定
class InitialPrice():
    def __init__(self, mode):
        self.mode = mode
        self.initial_price = 0

        if mode == "r":
            initial_price_list = [100, 300, 500, 700, 900, 1100]
            self.choice_number = self.choice_the_number_from_initial_price_list(initial_price_list)
            self.initial_price = self.decide_the_number()
        if type(self.mode) == int:
            self.choice_number = self.mode
            self.initial_price = self.decide_the_number()
    
        print(self.initial_price)
    
    # mode=rのprice_listからaboutな数字をランダム選択
    def choice_the_number_from_initial_price_list(self, initial_price_list):
        return random.choice(initial_price_list)
    
    # 完全決定
    def decide_the_number(self):
        times_number = random.uniform(0.9, 1.1)
        return round(self.choice_number * times_number, 2)

if __name__ == "__main__":
    InitialPrice(mode="r")