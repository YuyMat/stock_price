import random
import time

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
        self.plus_minus_value = 0
        self.new_price = 0
    
    # 1度目の上がり(下がり)値の決定
    def up_down_value(self):
        self.plus_minus_value = round(random.uniform(self.initial_price * 0.01, self.initial_price * 0.02), 2)
        random_plus_minus = random.randint(0, 1)

        # random_plus_minusが0の時は下がり値にする
        if random_plus_minus == 0:
            self.plus_minus_value = self.plus_minus_value * -1

class ChartMovement():
    def __init__(self):
        first_up_down_instance = FirstUpDown()
        first_up_down_instance.up_down_value()
        self.price = self.calc(first_up_down_instance.initial_price, first_up_down_instance.plus_minus_value)
        self.plus_minus_value = first_up_down_instance.plus_minus_value
        self.plus_counter = 0
        self.minus_counter = 0
        self.plus_minus_value_list = []

    def make_positive_negative_number(self, num, mode):
        if mode == "positive":
            return(abs(num))
        elif mode == "negative":
            return(-abs(num))
        
    def counter(self, plus_minus_value):
        # 反対が出たらカウンターリセット
        if self.plus_counter == 1:
            self.minus_counter = 0
        elif self.minus_counter == 1:
            self.plus_counter = 0
        
        # 回数のカウント
        if plus_minus_value >= 0:
            self.plus_counter += 1
        elif plus_minus_value < 0:
            self.minus_counter += 1

    def generate_random_value(self, current_price):
        self.plus_minus_value = round(random.uniform(current_price * 0.01, current_price * 0.02), 2)

    def calc(self, current_price, plus_minus_value):
        return current_price + plus_minus_value

    def five_chances(self):
        rand_num = random.randint(1, 5)
        if self.plus_counter >= 5:
            if rand_num == 5:
                self.generate_random_value(self.price)
                self.plus_minus_value = self.make_positive_negative_number(self.plus_minus_value, "negative")
                self.price += self.plus_minus_value
            else:
                self.generate_random_value(self.price)
                self.plus_minus_value = self.make_positive_negative_number(self.plus_minus_value, "positive")
                self.price += self.plus_minus_value

        elif self.minus_counter >= 5:
            if rand_num == 5:
                self.generate_random_value(self.price)
                self.plus_minus_value = self.make_positive_negative_number(self.plus_minus_value, "positive")
                self.price += self.plus_minus_value
            else:
                self.generate_random_value(self.price)
                self.plus_minus_value = self.make_positive_negative_number(self.plus_minus_value, "negative")
                self.price += self.plus_minus_value

    
    def generate_new_price(self):
        random_plus_minus = random.randint(0, 1)

        if random_plus_minus == 0:
            self.plus_minus_value = self.make_positive_negative_number(self.plus_minus_value, "negative")
        else:
            self.plus_minus_value = self.make_positive_negative_number(self.plus_minus_value, "positive")

if __name__ == "__main__":
    chart_movement = ChartMovement()
    while True:
        if chart_movement.plus_counter >= 5 or chart_movement.minus_counter >= 5:
            print(f"chart_movement.price : {chart_movement.price}")
            # chart_movement.generate_random_value(chart_movement.price)
            chart_movement.five_chances()
            chart_movement.counter(chart_movement.plus_minus_value)
            print(f"plus_counter : {chart_movement.plus_counter}\nminus_counter : {chart_movement.minus_counter}")
        else:
            print(f"chart_movement.price : {chart_movement.price}")
            chart_movement.generate_random_value(chart_movement.price)
            chart_movement.counter(chart_movement.plus_minus_value)
            print(f"plus_counter : {chart_movement.plus_counter}\nminus_counter : {chart_movement.minus_counter}")

            random_plus_minus = random.randint(0, 1)
            if random_plus_minus == 0:
                chart_movement.plus_minus_value = chart_movement.make_positive_negative_number(chart_movement.plus_minus_value, "negative")
                chart_movement.counter(chart_movement.plus_minus_value)
            else:
                chart_movement.plus_minus_value = chart_movement.make_positive_negative_number(chart_movement.plus_minus_value, "positive")


        
        chart_movement.price = chart_movement.calc(chart_movement.price, chart_movement.plus_minus_value)
        time.sleep(1)