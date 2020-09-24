from flask import Flask,render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

# def create_app():
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    WTF_CSRF_ENABLED=True,
    SECRET_KEY='9\x15\xf0\x1f\x9e*\xca\x10\xee\x92\x87\xec\xe2\xd3\x89\xb3NB\x8a\xab\xc5\x11\x9d&',
    TEMPLATES_AUTO_RELOAD=True,
    # SECRET_KEY='...'
)
csrf.init_app(app)


# app = Flask(__name__)
# app.config.update(
#     DEBUG=True,
#     TEMPLATES_AUTO_RELOAD=True,
#     # SECRET_KEY='...'
# )

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/pay/",methods=('GET', 'POST'))
@csrf.exempt
def pay_page():
    return render_template('paypage1.html'), 200


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)