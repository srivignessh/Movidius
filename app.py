import os
import uuid
from flask import Flask, jsonify, json, request

UPLOAD_FOLDER = '/root/movidius/uploads'
ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        name=os.path.splitext(file.filename)[0]
        if extension in ALLOWED_EXTENSIONS:
            image_id = str(uuid.uuid4())
            f_name = image_id + extension
            match_pct=os.listdir(UPLOAD_FOLDER)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
            return json.dumps({'name':name,'image_id':image_id, 'match_pct':match_pct})
        else:
            return "Invalid Image Format"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
