from logging import error
from flask import Flask, render_template , request, redirect,  jsonify
import boto3
from flask.json import jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadimage',methods=["POST"])
def uploadimage():
    s3_bucket= 'textract-console-ap-south-1-40b485f7-03b0-4dd3-b100-af7cacd8f1d'
    s3_client = boto3.client('s3')
    file=request.files['myfile']
    s3_client.upload_fileobj(file,s3_bucket,file.filename)
    return 'Uploaded Sucessfully'
    
@app.route('/python-flask-files-upload',methods=["POST"])
def ajaxupload():
    success = False
    errors = {}
    allowed_extension=['pdf']
    s3_bucket= 'textract-console-ap-south-1-40b485f7-03b0-4dd3-b100-af7cacd8f1d'
    s3_client = boto3.client('s3')
    file=request.files.get('mydata')
    
    #printing file name
    print(file.filename)
    
    file_extension=file.filename.split('.')
    print(file_extension)

    if file_extension[1] in allowed_extension:
        s3_client.upload_fileobj(file,s3_bucket,file.filename)
        success=True
    else:
        #errors[file.filename]='File Type is not allowed'
        errors['filetype']='File Type is not allowed'
    
    if success: 
        resp = jsonify({'message' : 'File successfully uploaded'})
        resp.status_code=201
        return  resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

if __name__ == '__main__':
    app.run(debug=True)