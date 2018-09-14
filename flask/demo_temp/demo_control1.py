from flask import Flask
from flask import render_template
from flask import json

app = Flask(__name__)


@app.route('/')
def index():
    return "index"

@app.route('/template')

def demo1():

    my_list= [
        {
             "id" : 1,
            "value" :"我爱工作"
        },
        {
             "id": 2,
            "value": "工作使我快乐"
        },
        {
             "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
             "id": 5,
            "value": "以梦为马，越骑越傻"
        },
    ]

    return render_template('control.html', mylist=my_list)

if __name__ == '__main__':
    app.run(debug=True)
