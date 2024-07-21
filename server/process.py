from flask import request

import sys
sys.path.append("/Users/yuya/Desktop/MyWork/false_stock_price")

from Stock import chart

class FirstUpDown():
    pass

class Main():
    def __init__(self):
        self.initial_price_instance = chart.InitialPrice()
        self.first_up_down_instance = chart.FirstUpDown()

        self.mode = request.form.get("mode")
        self.initial_price = request.form.get("text")
        self.plus_minus_value = 0
        self.price = 0

        self.price_history = []
        self.plus_minus_history_list = []
    
    def run(self):
        # 初期値
        self.initial_price = self.initial_price_instance.initial_price(self.mode, self.price_history, self.initial_price)

        # 最初の上がり値(下がり値)
        self.plus_minus_value = self.first_up_down_instance.up_down_value(self.initial_price, self.plus_minus_history_list)