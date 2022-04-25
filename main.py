# importing the library
from flask import Flask , render_template , request
import joblib

app = Flask(__name__)

#loading the model
model = joblib.load("model/diabetic_80.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/data", methods = ["post"])
def data():
    preg = request.form.get("preg")
    plas = request.form.get("plas")
    pres = request.form.get("pres")
    skin = request.form.get("skin")
    test = request.form.get("test")
    mass = request.form.get("mass")
    pedi = request.form.get("pedi")
    age = request.form.get("age")

    result = model.predict([[preg , plas , pres , skin , test , mass , pedi , age]])

    if result[0] == 1:
        data = "person is diabetic"
    else:
        data = "person is not diabetic"
         

    return render_template("predict.html" , data = data)

app.run() # <-- should always be at the end