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
        {"role": "user", "content": "你是谁"}],
    stream = True,
    stream_options={"include_usage": True},# 只返回文本内容


)
for chunk in completion:
    # print(chunk.model_dump_json())
    if chunk.choices:
        content = chunk.choices[0].delta.content
        if content:
             print(content,end="",flush=True)
