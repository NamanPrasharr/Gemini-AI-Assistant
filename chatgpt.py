
import google.generativeai as genai
import pyttsx3 
engine = pyttsx3.init()
# Replace with your actual Google API key

genai.configure(api_key="Your API key")   # your gemini api key (dont share with anyone)


model_name = "gemini-1.5-flash-latest"  

model = genai.GenerativeModel(model_name)

while True:
    engine.say("please tell me How can I Help you: ")
    engine.runAndWait()
    user_input = input("How can I Help you: ")  # Get user input
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Gemini AI: Goodbye!")
        engine.say("Gemini AI: Goodbye!")
        engine.runAndWait()
        break  # Exit loop

    try:
        response = model.generate_content(user_input)  # Send input to Gemini
        engine.say(response.text)
        engine.runAndWait()
        print("Gemini AI:", response.text)  # Print AI response

    except Exception as e:
        print("Error:", e)
AIzaSyBYTLXEvvyMlzzKwEgmrZUzU0aM74OTJSc