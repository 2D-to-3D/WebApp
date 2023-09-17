import os
from flask import Flask, request

UPLOAD_FOLDER = 'images'  # Relative path to the "images" folder
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to check if a file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Create the "images" directory if it doesn't exist
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            # Save the image to the "images" directory
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            return 'Image uploaded successfully'
    return 'No image uploaded', 400

if __name__ == '__main__':
    app.run( port=3002)
