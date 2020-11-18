from flask import Flask, request, render_template
from views import product_app



app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", methods=["GET", "POST"])
def index():
    name = "Magazine"
    if request.method == "POST":
        name = request.form.get('name', 'Magazine')
    return render_template("index.html", name=name)


@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    if name is None:
        name = "Magazine"
    return f"<h1>This is {name}!</h1>"



@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'Post int %d' % post_id