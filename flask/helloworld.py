from flask import Flask
import request

# 创建实例app
app = Flask(__name__,
            # static_path='/static',#静态文件访问路径
            static_url_path='/python27',
            static_folder='static',  # 静态文件存放的目录
            template_folder='/templates'  # 模板文件
            )


# 从对象中加载配置(必须了解)
# class Config(object):
#     DEBUG = True
#     SQL_IP ='127.0.0.1'
#     SQL_PORT = 3306
# app.config.from_object(Config)
# #在文件中加载配置
# app.config.from_pyfile('config.ini')
# #从环境变量中加载配置（了解一下）
# app.config.from_envwar('ENVCONFIG')
# 一些常用的配置，可以直接通过app.的形式设置
# app.debug = True
# app.config['DEBUG'] = True

@app.route('/')
def index():
    #     # a = 0
    #     # b = 1/a
    # print(app.config['DEBUG'])
    return 'Hello World!'


# 指定路由地址
# 'demo1'是指定访问路径地址
@app.route('/demo1')
def demo():
    return 'demo1'


# TODO视图函数def 函数
# 路由传递参数

@app.route('/user/<user_id>')
def user_info(user_id):
    return 'hello %s' % user_id


@app.route('/user/<int:user_id>')
def user_info(user_id):
    return 'hello %d' % user_id


if __name__ == '__main__':
    # run 里面加参数主机ip地址，端口，是否开启调试模式
    app.run(port=5000, debug=True)


    # 客户端 DNS 向服务端请求 （post请求报文：行，头，体）
    # 服务端（服务器 WSGI web程序） 解析（url） 响应报文（response）html解析
