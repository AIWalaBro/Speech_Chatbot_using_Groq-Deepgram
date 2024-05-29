import os
from dotenv import load_dotenv
load_dotenv()

from deepgram import (DeepgramClient, 
                      PrerecordedOptions, 
                      FileSource)



API_KEY= os.getenv("DEEPGRAM_API_KEY")

def speech2text(audio_input):
    try:
        # STEP 1 Create a Deepgram client using the AP
        deepgram = DeepgramClient(API_KEY)

        with open(audio_input, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
            }

        # STEP 2: Configure Deepgram options for audio
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            )
        
        # STEP 3: Call the transcribe file method with
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        
        # STEP 4: Print the response
        # print(response.to_json(indent=4))
        print(response["results"]["channels"][0]["alternatives"][0]["transcript"])
        return response["results"]["channels"][0]["alternatives"][0]["transcript"]

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    speech2text("myspeech.oga")
        

