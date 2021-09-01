from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from mlmodel import MLModel

ml_model = MLModel()
#Loading model
ml_model.load_model()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "POST":
        text = request.form["text"]
        response = ''
        #Text Prediction
        prediction = ml_model.text_predict(text)
        if (prediction):
            response = response + prediction
            msg = "This text is classified as {}".format(response)
            return render_template("index.html", msg=msg)
        else:
            msg = "sorry your text cannot be treated by our model"
            return render_template("index.html", msg=msg)
    else:
        return redirect(url_for("html"))

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1') #, port=5000
