# prompt模板使用Jinja2语法，简单点就是用双大括号代替f-string的单大括号
# 本配置文件支持热加载，修改prompt模板后无需重启服务。


# LLM对话支持的变量：
#   - input: 用户输入内容

# 知识库和搜索引擎对话支持的变量：
#   - context: 从检索结果拼接的知识文本
#   - question: 用户提出的问题


PROMPT_TEMPLATES = {
    # LLM对话模板
    "llm_chat": "{{ input }}",

    # 基于本地知识问答的提示词模板
    "knowledge_base_chat":
    """
    <CMD>Answer questions based on known information, concisely and professionally. If you cannot get an answer from it, please say "The question cannot be answered based on known information." No fabrication is allowed in the answer. Please use English for the answer.</CMD>
    <Knowledge>{{ context }}</Knowledge>、
    <Question>{{ question }}</Question>""",

    # 基于agent的提示词模板
    "agent_chat":
    """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can be repeated zero or more times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    history:
    {history}

    Question: {input}
    Thought: {agent_scratchpad}
"""
}

