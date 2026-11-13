from langchain_community.llms.tongyi import Tongyi

#1, 创建Tongyi客户端
#qwen-max是狭义llms,适合单次调用
llm = Tongyi(model="qwen-max")
#2,调用模型

res = llm.invoke(input="你好")


print(type(res))
print(res)

