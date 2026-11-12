import os

from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.getenv("DASHSCOPE_API_KEY"),

)
chat_history = []
print("第一次调用")
completion = client.chat.completions.create(
    model=  "qwen-flash",
    messages=[
        {"role": "user", "content": "你是谁"},
        {"role": "system", "content": "你是ai老师"}
    ]
)
print(completion.choices[0].message.content)

chat_history.append({"role": "user", "content": "你是谁"})
chat_history.append({"role": "assistant", "content": completion.choices[0].message.content})

print(chat_history)


#第二次调用
print("第二次调用")
user_message2 = "我是谁?"
chat_history += [{"role": "user", "content": user_message2}]
completion = client.chat.completions.create(
    model=  "qwen-flash",
    messages=chat_history,

)
print(completion.choices[0].message.content)
chat_history.append({"role": "assistant", "content": completion.choices[0].message.content})

print(chat_history)

