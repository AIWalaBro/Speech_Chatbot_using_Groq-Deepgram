from flask import Flask, request, send_file, render_template
import tempfile

from groq_serve import execute
from text2speech import text2speech
from speech2text import speech2text

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process-audio", methods=["POST"])
def process_audio_data():
audio_data = request.files["audio"].read()

with tempfile.NamedTemporaryFile(delete=False,
suffix=".wav") as temp_audio:
temp_audio.write(audio_data)
temp_audio.flush()

tekt = speech2text(temp_audio. name)
generated_answer = execute(f"Please answer to
the question: {text}")
# generated_answer = text
generated_speech = text2speech(generated_answer)