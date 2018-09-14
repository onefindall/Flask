import base64
import os

from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # 取到表单中提交上来的参数
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            print('参数错误')
        else:
            print(username, password)
            if username == 'laowang' and password == '1123':
                # 状态保持,设置用户名到cookie中表示登陆成功
                response = redirect(url_for('transfer'))
                response.set_cookie('username', username)
                return response
            else:
                print('密码错误')
    return render_template('login.html')


@app.route('/transfer', methods=['POST', 'GET'])
def transfer():
    # 从cookie中取到用户名
    username = request.cookies.get('username', None)
    # 如果没有取到,代表没有登陆
    if not username:
        return redirect(url_for('index'))
    if request.method == 'POST':
        to_account = request.form.get('to_account')
        money = request.form.get('money')
        # 校验操作
        form_csrf_token = request.form.get("csrf_token")
        cookie_csrf_token = request.cookies.get("csrf_token")

        if form_csrf_token != cookie_csrf_token:
            return '非法操作'
        print('假装执行转操作，将当前登录用户的钱转账到指定账户')
        return '转账 %s 元到 %s 成功' % (money, to_account)

    # 渲染转换页面
    csrf_token = generat_csrf()
    response = make_response(render_template('transfer.html', csrf_token=csrf_token))
    # 设置csrf_token
    response.set_cookie('csrf_token', csrf_token)
    return response


def generat_csrf():
    return bytes.decode(base64.b64encode(os.urandom(45)))


if __name__ == '__main__':
    app.run(port=9000, debug=True)
