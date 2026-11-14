from langchain_community.chat_models.tongyi import ChatTongyi


class MultiTurnChat:
    def __init__(self,model: str ,system_prompt: str = None) -> None:
        #创建支持流式输出的客户端
        self.llm = ChatTongyi(
            model=model,
            streaming=True
        )
        #使用二元组存储对话历史
        self.chat_history = []
        if system_prompt:
            self.chat_history.append(("system", system_prompt))

    def add_user_message(self,content:str) ->None :
        self.chat_history.append(("human",content))
    def add_ai_message(self,content:str) -> None:
        self.chat_history.append(("ai",content))
    def send(self,user_message:str):
        """
        1,增加用户消息到历史上下文
        2,调用模型
        3,收集ai的返回值并逐块返回
        4,将ai的回复整加到历史上下文
        """
        self.add_user_message(user_message)
        reply = self.llm.stream(input=self.chat_history)
        full_reply = ""
        for chunk in reply:
            if chunk.content:
                full_reply += chunk.content

                yield chunk.content

        self.add_ai_message(full_reply)
    #h获取全部对话历史
    def get_history(self):
        return self.chat_history.copy()

if __name__=="__main__":
    model ="qwen-plus"
    system_prompt = "背景设定:你现在是一个AI老师,负责AI课程"
    #创建多轮对话对象
    chat = MultiTurnChat(
        model = model,
        system_prompt = system_prompt
    )
    print("多轮对话已经启动.输入'exit'和'quit'退出程序",)
    while True:
        user_input = input("用户:")

        if user_input in ["exit","quit"]:
            print("对话结束!拜拜")
            print(f"最终对话历史:{chat.get_history()}")
            break
        if not user_input.strip():
            print("请勿输入空白字符!")
            continue

        print("AI老师:",end="",flush=True)
        for chunk in chat.send(user_input):
            print(chunk,end="",flush=True)
        print()

