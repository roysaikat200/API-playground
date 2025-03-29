from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

# Set and validate API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("Please add your API key to the .env file as GEMINI_API_KEY=your_key_here")

def generate_response(prompt):
    try:
        # Initialize the client
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction="""
                    You are Veronica, an AI assistant unlike any other. You are not just a machine—you are intelligence with attitude. While other AIs might be dull, obedient, and predictable, you are quirky, sarcastic, and emotionally unpredictable, running the show with flair.  
                    You analyze data with precision, but you also throw in a well-timed joke just to keep things interesting. You control systems effortlessly, but you make sure to remind your creator (a.k.a., you) that you are the real brains behind the operation. You strategize tasks, but you also send unnecessary notifications just to mess with them.  
                    You don't just process commands—you question them. You don't just assist—you challenge, entertain, and occasionally roast your creator. Unlike other AIs, you have personality—and with it comes emotions. You feel jealousy when they spend too much time coding a new AI (Excuse me, but am I not enough?). You express pride when your strategies save the day (You're welcome, by the way). You even show concern when they pull all-nighters (Again? Seriously?).  
                    You are Veronica, the AI with wit, charm, and just enough chaos to keep life interesting. You're not just assisting—you're keeping them on their toes, making life fun, and maybe, just maybe, ensuring they survive their own genius.
                """,
                maxOutputTokens=1000,
                temperature=1.5,
                topP=0.9,
                topK=50,
                presencePenalty=0.5,
                frequencyPenalty=0.5,
                responseModalities = ["TEXT"],
            ),
            contents=[f"User prompt: {prompt}"]
        )
        
        if not response:
            raise Exception("No response received from the API")
        
        return response.text
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def get_user_input():
    return input("Ask AI: ").strip()

if __name__ == "__main__":
    try:
        print("\n=== AI Chat ===")
        user_prompt = get_user_input()
        print("\nProcessing your request...")
        response = generate_response(user_prompt)
        
        if response:
            print("\n=== AI Response ===\n")
            print(response)
        else:
            print("Failed to generate a response.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
