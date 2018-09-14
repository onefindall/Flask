#设置cookie，通过响应带给浏览器
#获得cookie,从请求中获取
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

#获得cookie
@app.route('/')
def index():
    user_id =request.cookies.get('user_id')
    user_name =request.cookies.get('user_name')
    return "%s %s" %(user_id,user_name)

#设置cookie
@app.route('/login')
def login():
    response =make_response('success')
    response.set_cookie('user_id','1',max_age=3600)
    response.set_cookie('user_name', 'laowang', max_age=3600)
    return response

#删除cookie
@app.route('/logout')
def logout():
    response =make_response('success')
    response.delete_cookie('user_id')
    response.delete_cookie('user_name')
    return response


if __name__ == '__main__':
    app.run(debug=True)
