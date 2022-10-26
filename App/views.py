# from flask_blueprint import Blueprint

from flask import Blueprint, request, render_template, Response, session
from flask_mail import Message

from App.ext import mail

blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return "index"


@blue.route("/sendrequest/", methods=["GET", "POST", "DELETE", "PUT", "PATCH"])
def sendrequest():
    print(request.args)
    print(type(request.args))
    print(request.form)
    print(type(request.form))
    return "ok"


@blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get("username")

        response = Response("登录成共：%s" % username)
        response.set_cookie('username', username)

        session['username'] = username
        session['pwd'] = "123"
        return response


@blue.route('/mine/')
def mine():
    # 获取cookies 中指定键值对
    username = request.cookies.get('username')
    return "回来啦：%s" % username

    # 获取session
    # username = request.session.get('username')
    # uid = request.session.get('uid')
    # print(uid)
    # return render(request, 'app03/index.html', locals())


@blue.route('/sendmail/')
def send_mail():
    msg = Message("llll email", recipients=["2875052902@qq.com"])
    msg.body = "hahah 不过如此"
    msg.html = "<h2>wjm</h2>"
    mail.send(message=msg)
    return '邮件发生层高'
