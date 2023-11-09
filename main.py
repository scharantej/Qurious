 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')

if __name__ == '__main__':
    app.run()


html code

html
<!DOCTYPE html>
<html>
<head>
  <title>Gaming App</title>
</head>
<body>
  <h1>Welcome to the Gaming App!</h1>
  <a href="/game">Play Game</a>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
  <title>Gaming App</title>
</head>
<body>
  <h1>Game</h1>
  <canvas width="500" height="500"></canvas>
  <div id="control-panel">
    <button>Start</button>
    <button>Pause</button>
    <button>Reset</button>
  </div>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
  <title>Gaming App</title>
</head>
<body>
  <h1>Login</h1>
  <form action="/login" method="post">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" value="Login">
  </form>
  {% if error %}
    <p>{{ error }}</p>
  {% endif %}
</body>
</html>
