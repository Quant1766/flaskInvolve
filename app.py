import os

from sqlalchemy.sql import func
from flask import Flask,render_template,request,redirect
from flask_wtf.csrf import CSRFProtect
import requests
import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

csrf = CSRFProtect()

# def create_app():
app = Flask(__name__)
app.config.update(

    DEBUG=True,
    WTF_CSRF_ENABLED=True,
    SECRET_KEY='9\x15\xf0\x1f\x9e*\xca\x10\xee\x92\x87\xec\xe2\xd3\x89\xb3NB\x8a\xab\xc5\x11\x9d&',
    TEMPLATES_AUTO_RELOAD=True,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    # SECRET_KEY='...'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://u67ul92dr0at2b:p5b877ed21b94c5704a2dbe0b5f00eec89c2a95fa16163d90f87d1c40810610e0@ec2-54-216-29-57.eu-west-1.compute.amazonaws.com:5432/d1a6p9ooglrk3m'

csrf.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#валюта, сумма, время отправки,
#описание, идентификатор платежа в БД или файл.
class PayInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3),default="978")
    amount = db.Column(db.String(13),default="1.00")
    desctiption = db.Column(db.String(200),default="")
    shop_id = db.Column(db.String(3),default="5")
    shop_order_id = db.Column(db.String(4),default="101")
    sign = db.Column(db.String(200),default="")
    ref_url = db.Column(db.String(400), default="")
    payway = db.Column(db.String(20),default="")
    secret_key = db.Column(db.String(20),default="SecretKey01")

    created_date = db.Column(DateTime(timezone=True), default=func.now())



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

            me = PayInfo(ref_url=url_resp,currency=currency,
                         amount=amount,shop_id=shop_id,sign=sign,
                         shop_order_id=shop_order_id,desctiption=description,
                         )
            db.session.add(me)
            db.session.commit()

            return redirect(url_resp, code=302)
        elif currency == "643":
            #usd bill
            usd_b_url = "https://core.piastrix.com/invoice/create"
            usd_b_ctype = "application/json"
            data = {
                "amount": amount,
                "currency": currency,
                "payway": "payeer_rub",
                "shop_id": shop_id,
                "shop_order_id": shop_order_id,
                "sign": sign
                }
            res = requests.post(url=usd_b_url,json=data)

            res_json = res.json()
            url_resp = res_json["data"]["data"]["referer"]

            me = PayInfo(ref_url=url_resp, currency=currency,
                         amount=amount, shop_id=shop_id, sign=sign,payway="payeer_rub",
                         shop_order_id=shop_order_id, desctiption=description,
                         )
            db.session.add(me)
            db.session.commit()

            return redirect(url_resp, code=302)


        return render_template('paypage1.html'), 200
    else:

        return render_template('paypage1.html'), 200


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)