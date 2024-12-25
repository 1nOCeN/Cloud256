from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size: 16MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'html'}


# Check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route to upload a file
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        # If the user does not select a file
        if file.filename == '':
            return 'No selected file'

        # Check if the file is allowed and save it
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect(url_for('uploaded_files'))

    return render_template('Upload.html')


# Route to list all uploaded files
@app.route('/files')
def uploaded_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('Mainprogram.html', files=files)


# Route to serve individual files
@app.route('/uploads/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # Make sure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
