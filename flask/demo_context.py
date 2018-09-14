from flask import Flask

#应用上下文变量
from flask import current_app
from flask import g

#请求上下文变量
from flask import request
from flask import session
#shift+alt+上下键
#alt+enter 导包
app = Flask(__name__)
#上下文就是容器，存放信息
#current_app（app实例别名）跨函数的全局变量
#g临时存放，
# print(request.method)
# print(current_app.config.get('DEBUG')

#只能在视图函数运用，请求发生时

@app.route('/')
def index():
    g.name = 'abc'
    print(request.method)
    print(current_app.config.get('DEBUG'))
    print(request.url)
    print(current_app.name)
    print(g.name)
    return "index"


if __name__ == '__main__':
    app.run(debug=True)
