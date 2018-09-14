from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "index"
@app.route('/templates')
def demo():
    mylist=[1,2,3]
    mystr='<h1>大标题</h1>'
    myint=1111
    # mydict={'name':'xiaoming',
    #         'age':18
    #         }

    myhtml="<script>for(var i=0;i<50;i++){alert('ok')}</script>"
    mydict={
        'id' :'1',
        'name':'laowang'
    }
    mydictlist=[
        {
            'good_name':'大白菜',
            'price':18

        },
        {
            'good_name':'bai',
            'price':20
        }
    ]

    #创建环境就可以直接获得智能提示
    return render_template('demo2.html',
                           my_list=mylist,

                           my_str=mystr,
                           my_int=myint,
                           my_html=myhtml,
                           my_dict=mydict,
                           my_dict_list =mydictlist
                           )

#自定义过滤器
#方式1：装饰器的形式
# template_filter(过滤器的名字)
@app.template_filter('lireverse')
#do_lireverse里面传一个列表
def do_lireverse(li):
    #将列表中的值传到新的列表中
    temp = list(li)
    #将新的列表反转
    temp.reverse()
    return temp
# self.jinja_env.filters[name or f.__name__] = f
#方式2：直接添加过滤器
app.add_template_filter(do_lireverse,'lireverse')
# add_template_filter(函数名,'过滤器名')

if __name__ == '__main__':
    app.run(debug=True)
