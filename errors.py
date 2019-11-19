from app import app
from flask import render_template


@app.errorhandler()
def not_found_error(error):
    return render_template('404.html'), 404
