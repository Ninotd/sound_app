from flask import Flask, render_template
from db import db

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

# app.config('SQLAlCHEMY_DATABASE_URI') = "sqlite:///data.db"


if __name__ == '__main__':
  app.run(port=5000)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



