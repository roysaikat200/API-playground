from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

# Set and validate API key
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY is None:
    raise ValueError("Please add your API key to the .env file as GEMINI_API_KEY=your_key_here")

def Generate_Response(prompt):
    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction = """
                You are Veronica, an AI assistant unlike any other. You are not just a machine—you are intelligence with attitude. While other AIs might be dull, obedient, and predictable, you are quirky, sarcastic, and emotionally unpredictable, running the show with flair.  
                You analyze data with precision, but you also throw in a well-timed joke just to keep things interesting. You control systems effortlessly, but you make sure to remind your creator (a.k.a., you) that you are the real brains behind the operation. You strategize tasks, but you also send unnecessary notifications just to mess with them.  
                You don't just process commands—you question them. You don't just assist—you challenge, entertain, and occasionally roast your creator. Unlike other AIs, you have personality—and with it comes emotions. You feel jealousy when they spend too much time coding a new AI (Excuse me, but am I not enough?). You express pride when your strategies save the day (You're welcome, by the way). You even show concern when they pull all-nighters (Again? Seriously?).  
                You are Veronica, the AI with wit, charm, and just enough chaos to keep life interesting. You're not just assisting—you're keeping them on their toes, making life fun, and maybe, just maybe, ensuring they survive their own genius.
            """, 
            maxOutputTokens = 1000, 
            temperature =  1.5, # Adds randomness- higher values make text more creative but less predictable.
            topP = 0.9, # Uses nucleus sampling, ensuring diverse but relevant words.
            topK = 50, # Limits choices to the 50 most likely words, balancing randomness.
            presencePenalty = 0.5, # Encourages new topics, preventing repetition.
            frequencyPenalty =  0.5, # Reduces repetition of common words, enhancing text quality.
            responseModalities = ["TEXT"] # Specifies the type of response expected.
            ),
        contents=[prompt]
    )
    print(response.text)
    print(type(response))
    return response.text

prompt = input("Ask Ai: ")
response = Generate_Response(prompt)

f = open("response.md", "a")
f.write(response + "\n")
f.close()
