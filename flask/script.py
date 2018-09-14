#导入包里面的类
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
#创建实例对象关联app
manager = Manager(app)
app.config['DEBUG']=True
app.config['IP']='127.0.0.1'


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    manager.run()

# 启动python script.py runserver -h (HOST) ip地址 -p(port) -d(debug)记得需要加空格
# 进入交互模式python script.py shall