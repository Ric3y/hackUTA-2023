from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
test_user = {
    "username": "testuser",
    "password": "password123"
}
test_signup_user = {
    "username": "hackuta23",
    "password": "password123"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == test_user['username'] and password == test_user['password']:
            return render_template('index.html')
        if username == test_signup_user['username'] and password == test_signup_user['password']:
            return render_template('signup.html')
        else:
            return "Login Failed. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
