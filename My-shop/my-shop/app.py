from flask import Flask, request, render_template

from views.products import product_app

app = Flask(__name__)

app.register_blueprint(product_app, url_prefix="/products")

@app.route("/")
def hello_index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def delivery_of_products():
    print(request.environ)
    if request.method == "GET":
        return "Доставка  продуктов"


    name = request.form.get("name")
    return f"Доставка  {name}!"


@app.route("/Delivery/")
@app.route("/Delivery/<name>/")
def delivery(name="Продуктов"):
    return f"Доставка {name}!"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
