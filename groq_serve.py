from groq import Groq
from dotenv import load_dotenv
load_dotenv()

import os

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def execute(prompt):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user",
             "content": prompt
            }
        ],
        max_tokens=1024,
        temperature=0.5,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
        stream= True,
        n = 1, # this i have noted
        stop = None
    )
    
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response

if __name__ == "__main__":
    print(execute("Tell me a joke?"))