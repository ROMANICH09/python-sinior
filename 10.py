import telebot
from openai import OpenAI

TOKEN = '7492511272:AAGEP1z9Vn0BiJbue8gNiqw_DCJ20yFVAFU'
bot = telebot.TeleBot(TOKEN)
base_url = 'https://api.aimlapi.com/v1'
api_key = '8591373fc07d4752925b749a8f19010c'
system_prompt = 'You are not just a chat bot and you shall not introduce yourself as one. Just answer to user. You are a very good friend and you are very kind and helpful. You really hate furrys. Short casual answers.'
api = OpenAI(api_key=api_key, base_url=base_url)

def get_ai_response(prompt):
    completion = api.chat.completions.create(
        model='mistralai/Mistral-7B-Instruct-v0.2',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.7,
        max_tokens=256,
    )
    response = completion.choices[0].message.content
    return response

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello! Send me a message, and I'll respond")

@bot.message_handler(func=lambda message: True)  # Handle all other messages
def handle_message(message):
    response = get_ai_response(message.text)
    bot.send_message(message.chat.id, response)

if __name__ == "__main__":
    print("Bot started")
    bot.polling()
