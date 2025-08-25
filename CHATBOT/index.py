def simple_Vchatbot():
    print("VChatbot: Hello! I'm a simple chatbot. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'bye':
            print("VChatbot: Goodbye! Have a nice day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("VChatbot: Hi there!")
        elif 'how are you' in user_input:
            print("VChatbot: I'm fine, thanks for asking!")
        elif 'your name' in user_input:
            print("VChatbot: I'm just a simple chatbot!")
        elif 'help' in user_input:
            print("VChatbot: I can respond to greetings like hello, how are you, etc.")
        elif 'weather' in user_input:
            print("VChatbot: I don't know the weather, but it's nice to chat!")
        elif 'joke' in user_input:
            print("VChatbot: Why don't scientists trust atoms? Because they make up everything!")
        else:
            print("VChatbot: Sorry, I didn't understand that. Try saying hello or asking how I am.")

if __name__ == "__main__":
    simple_Vchatbot()