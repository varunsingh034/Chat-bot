from math import e
import openai

# Initialize the OpenAI client
client = openai.OpenAI(api_key='')

print("Chatbot: Hello! I'm ChatGPT. Type 'exit' to end the chat.")
messages = [{"role": "system", "content": "You are a helpful assistant."}]
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    
    messages.append({"role": "user", "content": user_input})
        
    try:
        # Send the user input to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= [{"role": "user", "content": user_input}]
        )
        
        reply = response.choices[0].message.content
        print("Chatbot:", reply)

        messages.append({"role": "assistant", "content": reply})
        
         # Generate image prompt from user input (or model-generated prompt)
        print("\nChatbot: Generating an image for you...")

        image_response = client.images.generate(
            model="dall-e-3",
            prompt=user_input,
            size="1024x1024",
            quality="standard",
            n=1
            )
        
        image_url = image_response.data[0].url
        print("Image URL:", image_url)
        
    except Exception as error:
            print("Error:", error)
        
  