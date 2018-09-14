# session依赖于cookie
#如果把cookie和session关闭可以把数据存储在URL里面
from flask import Flask
from flask import session

app = Flask(__name__)
#需要设置配置secert_key值可以自己定义（加密使用，如果没有就报错）
app.config['SECRET_KEY']='88555'

#获得session
@app.route('/')
def index():
    user_id=session.get('user_id','')
    user_name=session.get('user_id','')
    return "%s %s"%(user_id,user_name)

#设置
@app.route('/login')
def login():
    session['user_id'] ='1'
    session['user_name'] = 'xm'
    return 'success'

#如果有变量接收pop里面有返回值
@app.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('user_name',None)
    return 'success'
if __name__ == '__main__':
    app.run(debug=True)
