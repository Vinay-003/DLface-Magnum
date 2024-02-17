from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Define a route to render the HTML form
@app.route('/')
def upload_form():
    return render_template('upload.html')

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