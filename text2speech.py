
import os
from dotenv import load_dotenv
load_dotenv()

from deepgram import (
    DeepgramClient,
    SpeakOptions
)

filename = "speech.wav"

def text2speech(text_input):
    try:

        SPEAK_OPTIONS = {"text": text_input}

        deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))
        
        options = SpeakOptions(
                    model="aura-luna-en",
                    encoding="linear16", 
                    container="wav")

        # Directly call save - it handles the file writing
        response = deepgram.speak.v("1").save(
            filename, SPEAK_OPTIONS, options
        )

        print(f"File saved to: {filename}")
                    
        return filename
        
    except Exception as e:
        print(f"Exception:{e}")
        
if __name__ == "__main__":
    text2speech("Hello, my name is kajal kutri gu khae ")