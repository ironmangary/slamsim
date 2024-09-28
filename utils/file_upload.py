# file_upload.py
# for SlamSim

import os
import uuid
from werkzeug.utils import secure_filename

# Define allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(image, upload_folder='static/images'):
    # Check if the file is allowed (based on its extension)
    if image and allowed_file(image.filename):
        # Generate a secure filename
        filename = secure_filename(image.filename)
        
        # Generate a unique filename to avoid conflicts
        unique_filename = str(uuid.uuid4()) + "_" + filename
        
        # Ensure the upload directory exists
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # Save the image to the upload folder
        image_path = os.path.join(upload_folder, unique_filename)
        image.save(image_path)
        
        return unique_filename
    return None
