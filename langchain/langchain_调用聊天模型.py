from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
#1,创建模型客户端
llm = ChatTongyi(
    model="qwen-plus",
    streaming=True
)
#准备上下文+当前用户信息
chat_history = [
    SystemMessage(content="背景设定: 你是一位ai老师"),#背景设定
    HumanMessage(content="你是谁"),#当前用户信息
]
#3,携带上下文调用模型
res = llm.stream(input=chat_history)
#4,处理模型返回结果
for chunk in res:
    print(chunk.content, end="", flush=True)#实时打印

