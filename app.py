from flask import Flask, render_template
from db import db

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

# app.config('SQLAlCHEMY_DATABASE_URI') = "sqlite:///data.db"


if __name__ == '__main__':
  app.run(port=5000)



