import openai
openai.api_key = ''
client = openai.OpenAI()
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello, how are you?"}
  ]
)
print(response.choices[0].message.content)
