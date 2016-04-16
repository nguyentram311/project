from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#bài 1
# @app.route('/index')
# def index():
#     return render_template('index.html',article=List_object[0])

#bài 2
#dùng for list ở html ko cần dùng ở hàm def nữa
@app.route('/index')
def index():
    return render_template('index2.html',htmt_list=List_object)
if __name__ == '__main__':
    app.run()


#dùng for list ở html ko cần dùng ở hàm def nữa
