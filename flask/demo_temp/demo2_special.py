from flask import flash

from flask import Flask
from flask import g
from flask import render_template
from flask import session

app = Flask(__name__)
app.secret_key ='ddfff'


@app.route('/')
def index():
    return "index"


@app.route('/demo')
def demo():
    g.name='123'
    session['name']='laowang'
    session['password']='11225'
    flash('我是闪现的消息','我是闪现的消息')
    return render_template('special.html')

if __name__ == '__main__':
    app.run(debug=True)
