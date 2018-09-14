from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo,DataRequired


# strip


app = Flask(__name__)
app.secret_key='111'
#关闭CSRF验证
app.config['WTF_CSRF_ENABLED'] = False


#自定义注册表单 Equalto(用于验证的一般只用在密码的再次确认中)
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('请输入用户名')], render_kw={'placeholder':'请输入用户名'})
    password = PasswordField('密码', validators=[InputRequired('请输入密码')], render_kw={'placeholder':'请输入密码'})
    password2 = PasswordField('确认密码 ', validators=[InputRequired('请输入确认密码'), EqualTo('password','两次密码要一致')], render_kw={'placeholder':'请输入再次确认密码'})
    submit = SubmitField('注册')

@app.route('/')
def index():
    return "index"


@app.route('/register_wtf',methods=['POST','GET'])
def register_wtf():
    register_form = RegisterForm()
    #使用wtf表单做验证,相当于下面的判断表单是否为空
    if register_form.validate_on_submit():
        #执行注册逻辑
    #取到表单中三个参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        #取值方式2
        # username = register_form.username.data
        # password = register_form.password.data
        # password2 = register_form.password2.data
        # 假装成功了
        print(username, password, password2)
        return 'success'
    else:
        if request.method =='POST':
            flash('参数错误')

    return render_template('demo2_wtf.html',form=register_form)


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method =='POST':
        #获取表单中的三个参数
        username =request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username,password,password2]):
            #向前端界面弹出一个闪现消息
            #flash里面有session
            # flashes = session.get('_flashes', [])
            # session['_flashes'] = flashes
            flash('输入内容不一致')
        elif password !=password2:
            flash('输入密码不一致')
        else:
            #假装成功了
            print(username,password,password2)
            return 'success'


    return render_template('demo2_wtf.html')


if __name__ == '__main__':
    app.run(debug=True)
