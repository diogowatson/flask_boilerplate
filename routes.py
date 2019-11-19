from app import app
from flask import render_template, request
from werkzeug.utils import secure_filename


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Diogo'}
    # app.logger.info('% logged in',user.username)
    return render_template('index.html', title='Home', user=user)


@app.route('/upload_file', methods=['GET','POST'])
def upload_file():
    if request.method == 'GET':
        return 'GET working'

    if request.method == 'POST':
        app.logger.info('POST file requested')
        saved_file = request.files['file']
        saved_file.save(secure_filename(saved_file.filename))
        return 'file uploaded'


