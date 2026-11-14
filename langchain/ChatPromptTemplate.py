from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#1,定义实例
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system","假如你是一个AI专家"),
    MessagesPlaceholder("history"),
    ("human","我刚才问了什么内容")
])

chat_history = [
    ("human","什么是langgragh"),
    ("ai","复杂Agent（如能自我反思、重试、调用多个工具并决策的AI助手）")
]
#插入到占位符的方法
# #1,
# res1 = chat_prompt_template.invoke(input={"history":chat_history}).to_string()
# print(type(res1))
# print(res1)
# #2,
# res2 = chat_prompt_template.format(history=chat_history)
# print(type(res2))
# print(res2)
#3,
llm = Tongyi(model="qwen-plus")
chain = chat_prompt_template | llm
res3 = chain.stream(input={"history":chat_history})
for chunk in res3:
    print(chunk,end="",flush=True)