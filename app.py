from flask import Flask, request, render_template ,url_for
from form import RegistrationForm , LoginForm
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd270389871942afca232a044ca2a6f35'
# Define a route to render the HTML form
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# Define a route to handle the image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the uploaded file to a designated folder
        file.save(os.path.join('uploads', file.filename))
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='10.100.201.111', debug=True, port = 6969)