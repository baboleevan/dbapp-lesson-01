from flask import Flask, render_template, request, make_response
from functools import wraps, update_wrapper
from datetime import datetime
import os

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)

@app.route('/')
@nocache
def index():
    t = datetime.now().strftime("%Y-%m-%d")
    print(t)        
    return render_template("index.html", time=t)

@app.route('/enroll', methods=['POST'])
def enroll():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    print(name, email, password)
    return 'hello world...'

if __name__ == ("__main__"):
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  # docker : run port 8080
  app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  # app.run(debug=True)
