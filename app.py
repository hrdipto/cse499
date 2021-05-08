from flask import Flask , render_template, request
import model


app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def hello():
    result = ""
    if request.method == "POST":
        name = request.form['username']
        result = model.inference(name)
        print(result)

    return render_template("index.html", my_mark= result)

# @app.route("/sub", methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]

#     return render_template("sub.html", name= name)



if __name__ == "__main__":
    app.run(debug=True)