from flask import Flask, render_template, request, redirect
from pypg import helper
from pprint import pprint
# from pypg.helper import read_tables

app = Flask(__name__)

@app.route('/')
def index():
    tables = helper.read_tables()
    result = helper.students_list()
    return render_template("index.html", table=tables[0][0])

@app.route('/register', methods=["POST"])
def register():
    sid = request.form.get("id")
    name = request.form.get("name")
    email = request.form.get("email")
    print(helper.insert("student", sid, name, email))
    pprint(request.__dict__)
    return "OK"

@app.route("/register-json", methods=["POST"])
def register_json():
    import json #맨 위
    req = request.get_json()
    helper.insert("student", req['id'], req['name'], req['email'])
    pprint(request.__dict__ )
    return "OK"

@app.route('/list')
def student_list():
    result = helper.students_list()
    print(result)
    return render_template("list.html", students=result)

@app.route('/list-rest')
def student_list_rest():
    import json #맨 위에
    result = helper.students_list()
    print(type(result))
    result = json.dumps(result)
    print(type(result))
    return result

if __name__ == ("__main__"):
  # docker
  # app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  app.run(debug=True)
