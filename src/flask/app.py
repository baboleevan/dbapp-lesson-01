from flask import Flask, render_template, request, jsonify
from pypg.helper import read_tables, insert, read_students
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    tables = read_tables()
    return render_template("index.html", table=tables[0][0])

@app.route("/register", methods=["GET", "POST"])
def register():
    print("JSON: ", request.is_json)
    if request.method == 'POST':
        sid = request.form.get("id")
        name = request.form.get('name')
        email = request.form.get("email")

        print(f"{name}이 {email}로 가입함. {sid}")
        print(insert("student", sid, name, email))
    
    return render_template("list.html", students=read_students())

@app.route("/register-json", methods=["POST"])
def register_json():
     print("JSON: ", request.is_json)
     print(json.dumps(request.get_json()))
     pprint(request.__dict__)
     return "OK"

@app.route("/students")
def students():    
    students = json.dumps(read_students())
    print(type(students), students)
    return students


if __name__ == ("__main__"):
  # docker
  app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  # app.run(debug=True)
