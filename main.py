import qrcode

import random
random = random.Random()
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
app = Flask(__name__)
li= []
@app.route('/', methods=["GET", "POST"])
def home():
    co = "orange"
    list = []
    lis = []
    bb = "white"
    mes = False
    if request.method == "POST":
        data = ""
        data = request.form.get("name")
        co = request.form.get("siz")
        bb = request.form.get("bb")
        list.append(co)
        lis.append(data)
        if co == "":
            co = "black"
        if bb == "":
            bb = "white"
        # else:
        qr = qrcode.QRCode(version=1,box_size=15, border=4, )
        qr.add_data(data)
        qr.make(fit=True)
        rand = random.randint(9,99)
        img = qr.make_image(fill_color=co, back_color=bb)
        img.save(f"static/xy{rand}.png")
        im = f"static/xy{rand}.png"
        li.append(im)
        if co == bb:
            mes = True
            li.remove(im)
        print(li)
        return render_template("app.html",imp=im, list=list, lis=lis, li=li, mes=mes)
    return render_template("app.html", li=li)
if __name__ == "__main__":
    app.run(debug=True)
