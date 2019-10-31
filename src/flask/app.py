from flask import Flask, render_template, request, redirect
from pypg import helper
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    result = helper.students_list()
    return render_template("index.html", students=result)

@app.route("/register", methods=["POST"])
def register():
    sid = request.form.get("id")
    name = request.form.get('name')
    email = request.form.get("email")

    print(f"{name}이 {email}로 가입함. {sid}")
    print(helper.insert("student", sid, name, email))

    return redirect("/")
  
@app.route("/register-rest", methods=["POST"])
def register_rest():
    sid = request.form.get("id")
    name = request.form.get('name')
    email = request.form.get("email")
    print(f"{name}이 {email}로 가입함. {sid}")
    print(helper.insert("student", sid, name, email))

    return "OK"

@app.route("/list")
def students_list():
    # TODO: GET student data from 'student' table
    result = helper.students_list()
    return render_template("list.html", students=result)

@app.route("/list-rest")
def students_list_rest():
    # TODO: GET student data from 'student' table
    result = helper.students_list()
    pprint(result)
    result = json.dumps(result)
    return result

if __name__ == ("__main__"):
  # docker
  # app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  app.run(debug=True)
