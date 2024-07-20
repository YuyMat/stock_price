from flask import Flask, render_template

import sys
sys.path.append("/Users/yuya/Desktop/MyWork/false_stock_price")

from Stock import stock

chart = stock.ChartMovement()
print(chart.price)
app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello_world():
    a = "AA"
    return render_template("index.html", title=a, kk=a)

if __name__ == "__main__":
    app.run(debug=True)