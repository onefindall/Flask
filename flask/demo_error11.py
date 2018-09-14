from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    #主动抛出HTTP指定错误状态码
    # abort(404)
    a = 0
    b = 1/a
    return 'demo1'

#使用装饰器的形式去捕获指定的错误码和异常
@app.errorhandler(404)
def page_not_found(error):
    return '页面不见了'

#错误捕获
@app.errorhandler(ZeroDivisionError)
def zero_divsion_error(error):
    return '除数不能为0'

if __name__ =='__main__':
    app.run(debug=True)