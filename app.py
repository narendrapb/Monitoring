from flask import Flask,render_template,request,redirect,url_for,jsonify
import json

app = Flask(__name__)
database={
    "users":['narendra','naren'],
    "password":["12345","1234"],
    "adminusers":{
        "users":["admin"],
        "password":["admin"]
    }
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        if username in database["users"]:
            ind=database["users"].index(username)
            if database["users"][ind]==username and database["password"][ind]==password:
                return render_template('index.html')
            else:
                return render_template('fail.html'),401
        else:
            return jsonify({'message': 'User not found'}),401

    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
       
        if username in database["adminusers"]["users"]:
            ind=database["adminusers"]["users"].index(username)
            if database["adminusers"]["users"][ind]==username and database["adminusers"]["password"][ind]==password:
                return database
            else:
                return jsonify({'message': 'Invalid credentials'}),401
        else:
            return jsonify({'message': 'User not found'}),401

    return render_template('adminlogin.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        chekpass = request.form["confirm_password"]
        if password==chekpass:
            database['users'].append(username)
            database['password'].append(password)
            return render_template('login.html')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

