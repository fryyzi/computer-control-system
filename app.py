from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')  # Змінено маршрут, щоб передавати ім'я користувача
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    conn.close()

    if user:
        return redirect(url_for('profile', username=username))
    else:
        return "Невірний логін або пароль"

if __name__ == '__main__':
    app.run(debug=True)
