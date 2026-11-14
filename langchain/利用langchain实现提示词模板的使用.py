from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate


#1,准备提示词模板

prompt_template = PromptTemplate.from_template(
    "假如你是一位{expert}专家,请你解释一下{content}是什么"
)
llm = Tongyi(model="qwen-plus")

chain = prompt_template | llm  # | 前一个的输出是后一个的输入

result = chain.stream(input={"expert":"AI","content":"Langgraph"})

for chunk in result :
    print(chunk,end="",flush=True)