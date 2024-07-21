from flask import Flask, render_template, request

import process

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def hello_world():
    chart_value = None  # 初期化
    if request.method == "POST":
        chart_value = process.Main()
        chart_value.run()
    return render_template("index.html", kk=chart_value.initial_price if chart_value else None)

if __name__ == "__main__":
    app.run(debug=True)