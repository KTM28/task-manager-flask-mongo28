import os
from flask import Flask

app = Flask(__name__)
#app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def hello():
    return f'<h1>Hello world!</h1>'




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)