
from flask import Flask, request,render_template
import numpy as np
import matplotlib.pyplot as plt
import os
import random

app=Flask(__name__)
@app.route('/')

def poly_fit(l1,l2,d):
    x=np.array(l1)
    y=np.array(l2)
    f=np.polyfit(x,y,d).round(decimals=2)
    return x,y,f

def process_input(s):
    return eval(s)

def index():
    return render_template('app.html')

@app.route('/',methods=['POST'])
def request_data():
    x=process_input(request.form['text1'])
    y=process_input(request.form['text2'])
    d=process_input(request.form['text3'])
    P,x,y,f=polynomial_fit(x,y,d)
    
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)
