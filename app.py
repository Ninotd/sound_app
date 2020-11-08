pfrom flask import Flask, render_template, request, jsonify, make_response
from db import db
import librosa
import wave
import io
import soundfile as sf

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/audio', methods=["POST"])
def audio():
  wav = request.files["file"].content_type
  # wav_2 = io.BytesIO(wav)
  # nchannels = 1
  # sampwidth = 1
  # framerate = 8000
  # nframes = 1
  # name = 'output.wav'
  # audio = wave.open(name, 'wb')
  # audio.setnchannels(nchannels)
  # audio.setsampwidth(sampwidth)
  # audio.setframerate(framerate)
  # audio.setnframes(nframes)
  # blob = open(wav.stream).read()
  # final_wav = audio.writeframes(blob)

  print(wav)
  # print(wav_2)
  return "hello"

# def get_mfcc(path):
#   b, sr = librosa.core.load(path)
#   print(b)
#   print(sr)

# get_mfcc(wav)



# app.config('SQLAlCHEMY_DATABASE_URI') = "sqlite:///data.db"


if __name__ == '__main__':
  app.run(port=5000)




