from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "index"
@app.route('/templates')
def demo():
    mylist=[1,2,3]
    mystr='jjj'
    myint=1111
    mydict={'name':'xiaoming',
            'age':18
            }
    myhtml="<script>for(var i=0;i<50;i++){alert('ok')}</script>"
    #创建环境就可以直接获得智能提示
    return render_template('demo2.html',
                           my_list=mylist,
                           my_dict=mydict,
                           my_str=mystr,
                           my_int=myint,
                           my_html=myhtml,
                           )

if __name__ == '__main__':
    app.run(debug=True)
