
import os
from openai import OpenAI
from openai.resources.skills import content


class MultTurnChat:
    def __init__(self,base_url:str,model:str,system_prompt:str = None):
       self.client = OpenAI(base_url=base_url)
       self.model = model
       self.chat_history = []

       if system_prompt:
           self.chat_history.append({"role":"system","content":"system_prompt"})

    def add_user_message(self,message:str):

        self.chat_history.append({"role":"user","content":message})

    def add_assistant_message(self, reply: str):
        self.chat_history.append({"role": "assistant", "content": reply})

    def send(self,use_message:str) ->str       :
        self.add_user_message(use_message)
        completion = self.client.chat.completions.create(
            model = self.model,
            messages=self.chat_history,
            stream=True,

        )
        # reply = completion.choices[0].message.content
        # self.add_assistant_message(reply)
        # return reply
        full_replt = ""# 完整的回复
        for chunk in completion:
            if chunk.choices[0].delta.content:# 判断是否有内容
                content = chunk.choices[0].delta.content# 获取内容
                full_replt += content # 累加内容
                yield content# 返回内容


if __name__ == '__main__':
        chat = MultTurnChat(
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            model="qwen-flash",
            system_prompt="你是一个ai老师,能教学ai"
        )

        print("多轮对话已经启动,输入'exit' 或 'quit' 退出程序.\n")

        while True:
            user_input = input("用户:")
            if user_input in ["exit", "quit"]:
                print("程序已退出.")
                break
            elif not user_input.strip():
                print("输入为空,请重新输入.")
                continue
            else:
                # reply = chat.send(user_input)
                # print(f"AI: {reply}")
                print("AI老师:",end="",flush=True)
                for chunk in chat.send(user_input):
                    print(chunk,end="",flush=True)

                print()# 换行

