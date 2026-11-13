from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
#1,创建模型客户端
llm = ChatTongyi(
    model="qwen-plus",
)
#准备上下文+当前用户信息
chat_history = [
    SystemMessage(content="背景设定: 你是一位ai老师"),#背景设定
    HumanMessage(content="你是谁"),#当前用户信息
]
#3,携带上下文调用模型
res = llm.invoke(input=chat_history)
print(res.content)


