from flask import Flask, render_template, request
from pypg import helper

app = Flask(__name__)

@app.route('/')
def index():
    tables = helper.read_tables()
    print(type(tables), tables)
    print(type(tables[0]), tables[0])
    print(type(tables[0][0]), tables[0][0])
    return render_template("index.html", table=tables[0][0])

@app.route("/register", methods=["POST"])
def register():
    sid = request.form.get("id")
    name = request.form.get('name')
    email = request.form.get("email")

    print(f"{name}이 {email}로 가입함. {sid}")
    print(helper.insert("student", sid, name, email))

    return "register"


if __name__ == ("__main__"):
  # docker
  # app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  app.run(debug=True)
