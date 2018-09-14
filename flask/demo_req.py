from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


#netstat -antp(查看端口运行)
#sudo lsof -i 端口号
#sudo kill -s 9 pid


@app.route('/upload', methods=['POST'])
def upload():
    # request.args
    # request.data
    # request.url
    # request.method
    pic = request.files.get('pic')
    pic.save('1.jpg')
    return 'success'

@app.route('/data',methods=['POST','GET'])
def data():
    data = request.data
    print(data.decode('utf-8'))
    print('ok')

@app.route('/args')
def args():
    name = request.args.get('uesr_name')
    pwd = request.args.get('password')

    # name = request.args

    return '%s %s' % (name,pwd)

@app.route('/form',methods=['POST'])
def form():
    #需要一个返回值

    # print(request.form)
    name = request.form.get('uesr_name')
    pwd = request.form.get('password')
    print('%s %s' % (name,pwd))
    return 'ok'








if __name__ =='__main__':
    app.run(debug=True)