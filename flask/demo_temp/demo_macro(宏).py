#jinjia2的一个函数，返回一个模板
#避免重复写模板，写成函数是为了重复使用
#重复使用模板代码片段写入单个文件，避免重复使用
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "index"
#宏(灵活的模板)
@app.route('/demo1')
def demo1():
    return render_template('macro(宏).html')
#继承
@app.route('/demo2')
def demo2():
    return render_template('extend.html')

@app.route('/news_index')
def demo3():
    return render_template('index.html')

@app.route('/news_detail')
def demo4():
    return render_template('detail.html')
#包含(固定内容)
@app.route('/demo5')
def demo5():
    return render_template('include.html')
if __name__ == '__main__':
    app.run(debug=True)
