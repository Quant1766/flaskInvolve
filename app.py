from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/pay/")
def pay_page():
    return render_template('paypage.html'), 200


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)