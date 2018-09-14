from flask import Flask
from flask import request
app = Flask(__name__)

@app.before_first_request
def before_first_request():
    # 在第一次请求之前访问函数
    #只打印一次
    # 当有请求可以向数据库请求数据
    print('before_first_request')

@app.before_request
def before_request():
    # 每次访问函数都会被调用
    #每调用一次就打印一次
    print('before_request')
    #可以对非法请求进行阻止
    #可以查出ip黑名单，
    # 如果这里写了return就不会调用下面的index里面的return
    #获取ip信息
    if request.remote_addr:
        return 'hhh'

@app.after_request
def after_request(response):
    #在请求之后会调用，并且函数里面接受一个参数：响应
    #还需把响应进行返回
    #报错就不执行
    print('after_request')
    return response
@app.teardown_request
def teardown_request(error):
    #不管报错不报错都要执行
    #在请求之后执行，如果请求有异常，可以传入异常函数
    print(teardown_request)


@app.route('/')
def index():
    return 'index'



if __name__ =='__main__':
    app.run(debug=True)