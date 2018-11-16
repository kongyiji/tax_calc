# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

def tax_calc():
    deduct_insurance = eval(input('请输入缴纳五险一金后的工资：'))
    threshold = 5000
    money = deduct_insurance - threshold
    tax = 0

    calc_tables = (
        (80000, 0.45, 15160),
        (55000, 0.35, 7160),
        (35000, 0.3, 4410),
        (25000, 0.25, 2660),
        (12000, 0.2, 1410),
        (3000, 0.1, 210),
        (0, 0.03, 0)
    )


    for table in calc_tables:
        if money > table[0]:
            tax = money * table[1] - table[2]


    result = f'需要缴纳个税：{tax}, 税后工资：{deduct_insurance - tax}'
    print(result)



# @app.route('/tax_calc/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':

#     return 'Hello, World!'
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000)
    