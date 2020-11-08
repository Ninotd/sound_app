from flask import Flask, render_template, request, jsonify, make_response
from db import db
import librosa
import wave
import io
import soundfile as sf
import pickle
import xgboost

app = Flask(__name__)
model = pickle.load(open("xgb.pickle.dat", "rb"))

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/audio', methods=["POST"])
def audio():
  wav = request.files["file"]
  print(wav)
  return "hello"

# def get_mfcc(path):
#   b, sr = librosa.core.load(path)
#   print(b)
#   print(sr)

# get_mfcc(wav)



# app.config('SQLAlCHEMY_DATABASE_URI') = "sqlite:///data.db"

@app.route('/predict',methods=['POST'])
def predict():

    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    print(prediction)

if __name__ == '__main__':
  app.run(port=5000)




