import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory

from werkzeug.utils import secure_filename
import model
import fas


UPLOAD_FOLDER = './upload/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'image.png'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = fas.run_test("./upload/image.png")
            if (result >= .5):
                flag = "Real"
            else:
                flag = "Fake"
            return redirect(url_for('uploaded_file',
                                    flag=flag))
    return render_template("index.html")


@app.route('/result/<flag>', methods=['GET'])
def uploaded_file(flag):
    return render_template("result.html", flag=flag)

# @app.route("/sub", methods = ["POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form["username"]

#     return render_template("sub.html", name= name)


if __name__ == "__main__":
    app.run(debug=True)
