from flask import Flask,render_template,request,redirect
from flask_wtf.csrf import CSRFProtect
import requests
import hashlib
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

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/",methods=('GET', 'POST'))
@csrf.exempt
def pay_page():
    if request.method=="POST":
        amount = str(request.form['amount'])
        currency = str(request.form['currency'])
        description = str(request.form['description'])
        sign = str(request.form['sign'])
        shop_id = str(request.form['shop_id'])
        shop_order_id = str(request.form['shop_order_id'])

        if currency == "840":
            #usd bill
            usd_b_url = "https://core.piastrix.com/bill/create"
            usd_b_ctype = "application/json"
            data = {
                "payer_currency": currency,
                 "shop_amount": amount,
                 "shop_currency": currency,
                 "shop_id": shop_id,
                 "shop_order_id": shop_order_id,
                 "sign": sign
             }

            res = requests.post(url=usd_b_url,json=data)
            res_json = res.json()
            url_resp = res_json["data"]["url"]

            return redirect(url_resp, code=302)



        return render_template('paypage1.html'), 200
    else:

        return render_template('paypage1.html'), 200


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)