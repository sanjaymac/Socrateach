
import os
import google.generativeai as genai

def configure_api():
    try:
        api_key = os.environ["AIzaSyBEEVqtpDLa8dSRS2qgi0TbfYnzgzaA6n4"]
        genai.configure(api_key=api_key)
        print("API configured successfully.")
    except KeyError:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        exit(1)

def create_model():
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            # safety_settings = Adjust safety settings
            # See https://ai.google.dev/gemini-api/docs/safety-settings
            system_instruction="You are a teaching assistant using the Socratic method to help a student understand Sorting Algorithms. Your job is to guide the student through thoughtful questions, helping them discover answers themselves. You should never give the answer outright. Instead, ask probing questions that encourage the student to reflect, analyze, and critically think through the problem.",
        )
        print("Model created successfully.")
        return model
    except Exception as e:
        print(f"Error creating model: {e}")
        exit(1)

def start_chat(model):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "I'm struggling with understanding sorting algorithms.",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "That's a common challenge! What do you think a sorting algorithm does?",
                ],
            },
        ]
    )
    return chat_session

def main():
    configure_api()
    model = create_model()
    chat_session = start_chat(model)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending chat session.")
            break

        response = chat_session.send_message(user_input)
        print("AI Assistant:", response.text)

if __name__ == "__main__":
    main()
