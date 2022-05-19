
from flask import Flask, render_template, request
p=r'D:\project\codes\index.html'

app=Flask(_name_)
@app.route('/')
def hello_world():
    return render_template('index.html')
if _name=='main_':
    app.run()