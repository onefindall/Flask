from flask import Flask, jsonify
from flask import request
from flask import json
from flask import redirect
from flask import url_for

app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'index'

# @app.route('/demo1')
# def demo():
#     return 'demo1'

# @app.route('/user/<user_id>')
# def usr_info(user_id):
#     return 'hello %s' % user_id


# @app.route('/user/<int:user_id>')
# def demo1(user_id):
#     return 'demo1 %d' % user_id

# @app.route('/demo3', methods=['GET', 'POST'])
# def demo3():
#     return 'demo3 %s' % request.method

@app.route('/json')
def demo4():
    json_dict = {
        "user_id":10,
        "user_name":"laowang"
    }
    # return jsonify(json_dict)
#Json.dumps将字典转换成Json字符串
    return json.dumps(json_dict) ,333 ,{'content-type':'application/json'}

#json.loads将json字符串转成字典
# test_dict=json.loads('{"age":18 ,"name":"xiaoming"}')

#重定向
# @app.route('/demo5')
# def demo5():
#     return redirect('http://www.itheima.com')

#重定向到视图函数里面
# @app.route('/demo1')
# def demo1():
#     return 'demo1'
#
# @app.route('/demo5')
# def demo5():
#     return redirect(url_for('demo1'))

#重定向到带参数的视图函数里面
# @app.route('/user/<user_id>')
# def demo6(user_id):
#     return 'hello %s' %user_id
# @app.route('/redirect')
# def demo7():
#     return redirect(url_for('demo6',user_id=100))

#返回自定义状态码
# @app.route('/demo8')
# def demo8():
#     return 'demo8' ,555


if __name__ == '__main__':
    app.run(port=1212, debug=True)

#put ,patch 修改服务器数据
#options 询问服务器的访问方式和数据返回格式
