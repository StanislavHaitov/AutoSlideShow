from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from pptx import Presentation

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
SLIDE_FOLDER = 'static/slides'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload and slide folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SLIDE_FOLDER, exist_ok=True)

# Convert PowerPoint slides to images (placeholder logic, adjust based on your conversion method)
def convert_ppt_to_images(ppt_file, output_dir):
    presentation = Presentation(ppt_file)
    slide_images = []
    for i, slide in enumerate(presentation.slides):
        slide_image_path = os.path.join(output_dir, f"slide{i+1}.png")
        # Add image conversion logic here (using a suitable rendering library)
        slide_images.append(slide_image_path)
    return slide_images

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            slide_images = convert_ppt_to_images(filepath, SLIDE_FOLDER)
            return render_template('slideshow.html', slide_images=slide_images)
    return render_template('upload.html')

# Serve static files
@app.route('/slides/<filename>')
def send_slide(filename):
    return send_from_directory(SLIDE_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
