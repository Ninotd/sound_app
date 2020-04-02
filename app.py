from flask import Flask
from db import db

app = Flask(__name__)

@app.route('/')
def home():
  return "hello world"

app.config('SQLAlCHEMY_DATABASE_URI') = "sqlite:///data.db"

db.init_app():
  if __name__ == '__main__':
    app.run(port=5000)



