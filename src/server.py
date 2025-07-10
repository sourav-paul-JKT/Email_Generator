import os
import json
import ollama

class OllamaEGchatbot:
    def __init__(self, model = "llama3.2:1b"):
        self.model = model
        self.history = "conversation_history.json"
        self.conversation_history = []
        self.load_history()
    
    def load_history(self):
        if os.path.exists(self.history):
            with open(self.history, 'r') as h:
                self.conversation_history = json.load(h)
    
    def save_history(self):
        with open(self.history, "w") as h:
            json.dump(self.conversation_history, h, indent=2)
            
    def build_prompt(self, data: dict):
        return (
            f"You are a helpful assistant that writes professional emails.\n\n"
            f"Write a {data['tone']} {data['email_type']} email to a {data['recipient_role']}.\n"
            f"The purpose of the email is: \"{data['key_points']}\"\n"
            f"Return only the email body along with the email subject and the greetings.\n"
            f"Keep the language clear, natural, and well‑structured."
        )

    def generate_email(self, user_data: dict):
        prompt = self.build_prompt(user_data)
        
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]

    def chat(self, user_data: dict):
        email_body = self.generate_email(user_data)

        prompt = self.build_prompt(user_data)
        self.conversation_history.extend(
            [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": email_body},
            ]
        )
        self.save_history()
        return email_body


if __name__ == "__main__":
    chatbot = OllamaEGchatbot()

    user_input = {}
    user_input["email_type"]      = input("Email type (e.g., apology, follow‑up): ")
    user_input["tone"]            = input("Tone (formal, casual, friendly): ")
    user_input["recipient_role"]  = input("Recipient role (manager, customer): ")
    user_input["key_points"]      = input("Key points / main message: ")

    email_body = chatbot.chat(user_input)
    print(f"Email_body: \n {email_body}")
