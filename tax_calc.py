# -*- coding: utf-8 -*-

import sys
from flask import Flask, render_template, request, url_for

DEBUG = True
app = Flask(__name__)

def tax_calc(deduct_insurance):
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

    after_tax = deduct_insurance - tax
    return tax, after_tax

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        deduct_insurance = eval(request.form['money'])
        tax, result = tax_calc(deduct_insurance)
        return render_template('index.html', TAX = tax, RESULT = result)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
    