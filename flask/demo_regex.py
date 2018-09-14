from flask import Flask
from flask import redirect
from flask import url_for


#导入转换器基类
from werkzeug.routing import BaseConverter

#自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map , *args):
        super(RegexConverter,self).__init__(url_map)
        #将接受的第一个参数当作匹配规则进行保存
        self.regex = args[0]

class ListConverter(BaseConverter):
    regex = '(\\d+,?)+\\d$'

    def to_python(self,value):
        return value.split(',')

    def to_url(self,value):
        result = ','.join(str(v) for v in value)
        return result

app = Flask(__name__)
#添加转换器到默认的转换字典中，并指定转换器使用时名字re
app.url_map.converters['re'] = RegexConverter
app.url_map.converters['list'] = ListConverter
#实现自定义匹配
@app.route('/user/<re("[0-9]{3}"):user_id>')
def demo(user_id):
    return 'demo %s' % user_id

@app.route('/user')
def demo1():
    return 'demo1'
@app.route('/demo2/<list:user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id
@app.route('/demo3')
def demo3():
    return redirect(url_for('demo2', user_id=[1,2,3]))



if __name__ == '__main__':
    app.run(port=1212, debug=True)