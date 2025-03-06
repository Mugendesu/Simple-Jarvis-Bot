from openai import OpenAI

API_KEY = open('API_KEY' , 'r').read() #<-- Your Api Key Here

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

chat_log = [{"role" : "user" , "content" : "Act as You are an AI bot known as Jarvis , Powered by DeepSeek-R1."},
            {"role" : "assistant" , "content" : "Greetings! I am Jarvis, an AI assistant powered by DeepSeek-R1. How may I assist you today?"}]

def bot_init(command):
  user_message = command
  chat_log.append({'role' : 'user' , "content" : user_message})
  response = client.chat.completions.create(
      model="deepseek/deepseek-r1:free", #<-- Your Model name here
      messages= chat_log
  )
  bot_response = response.choices[0].message.content
  print(f'Jarvis : {bot_response.strip('\n').strip()}\n' , flush=True)
  chat_log.append({"role" : "assistant" , "content" : bot_response.strip('\n').strip()})
  return chat_log[-1]["content"]
  
  








def main():
  'This Function is just for Development purposes'
  bot_init('2+2')
  print('This Function is just for Development purposes')
  # while True:
  #     user_message = input('You: ')
  #     if user_message.lower() == 'quit': break
  #     else: 
  #         chat_log.append({'role' : 'user' , "content" : user_message})
  #         response = client.chat.completions.create(
  #             model="deepseek/deepseek-r1:free",
  #             messages= chat_log
  #         )
  #         bot_response = response.choices[0].message.content
  #         print(f'Jarvis : {bot_response.strip('\n').strip()}\n')
  #         chat_log.append({"role" : "assistant" , "content" : bot_response.strip('\n').strip()})
  
if __name__ == '__main__':
  main()















# print(response.choices[0].message.content)