from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    temp =make_response(render_template('make_response.html'))
    return temp
    # response=make_response('<h2>hahah</h2>')
    # return response,404


if __name__ == '__main__':
    app.run(debug=True)
