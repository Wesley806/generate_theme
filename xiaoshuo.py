from langchain import OpenAI, LLMChain
from langchain.chains import SimpleSequentialChain

openai_api_key = 'sk-proj-' #填自己的key
openai = OpenAI(api_key=openai_api_key)

class PlotAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def generate_plot(self, theme):
        prompt = f"生成小说{theme}的具体故事情节."
        return self.llm(prompt)

class CharacterAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def describe_interaction(self, plot):
        prompt = f"基于小说情节，描述主要角色之间的交互:\n\n{plot}"
        return self.llm(prompt)

class DialogueAgent:
    def __init__(self, llm):
        self.llm = llm
    
    def write_dialogue(self, interaction):
        prompt = f"基于角色交互的描述, 编写出具体的对话内容:\n\n{interaction}"
        return self.llm(prompt)


def generate_novel(theme):
    llm = OpenAI(api_key=openai_api_key)

    plot_agent = PlotAgent(llm)
    character_agent = CharacterAgent(llm)
    dialogue_agent = DialogueAgent(llm)

    # 故事情节
    plot = plot_agent.generate_plot(theme)
    print("故事情节:\n", plot)

    # 角色交互
    interaction = character_agent.describe_interaction(plot)
    print("角色交互:\n", interaction)

    # 对话内容
    dialogue = dialogue_agent.write_dialogue(interaction)
    print("对话内容:\n", dialogue)

    # 组合以上内容
    novel = f"{plot}\n\n{interaction}\n\n{dialogue}"
    return novel

# 生成游戏相关题材小说
theme = "武侠类型"
novel = generate_novel(theme)

# 保存小说内容到文件
with open("武侠小说.txt", "w") as file:
    file.write(novel)

print("Finish !! 小说保存在武侠小说.txt文件中")
