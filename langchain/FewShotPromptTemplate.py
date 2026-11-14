from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate

#1,定义实例
examples = [
    {"input":"高兴","output":"愉悦"},
    {"input":"快速","output":"迅猛"},
    {"input":"美丽","output":"艳丽"}
]

#2,定义实例的格式化模版
example_prompt = PromptTemplate.from_template(
    template="输入:{input}\n输出:{output}"
)

#3,创建FewShotPromptTemplate
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="请根据以下事例,将输入词语转换成同义词",
    suffix="基于实例回答问题.用户输入:{word}\n输出:",
    input_variables=["word"]

)
#4,调用
prompt_text = few_shot_prompt.format(word="悲伤")
print(prompt_text)

llm = Tongyi(model="qwen-plus")
chain = few_shot_prompt | llm
print(chain.invoke({"word":"悲伤"}))
