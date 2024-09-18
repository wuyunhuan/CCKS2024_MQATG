from openai import OpenAI
import pandas as pd
import os
import re
import ast
import dashscope

# 阿里云api key
dashscope.api_key="sk-b2012aa4ccd74b50b8ace1d9f3338f63"
# deepseek  api key
client = OpenAI(
  base_url = "https://api.deepseek.com/v1",
  api_key = "sk-d2bc92984d694f348ced436f12803320"
)

# 生成10个填空题
def qag_tk(text):
    prompt = f"""任务说明：作为军事装备领域的专家，请一步步思考，仔细分析下方文章内容，生成十个高质量且内容不同的中文填空题问答对，只输出结果即可，不需要任何解释。
                         ###文章内容:
                         {text}
                         ### 生成填空题要求:
                            1. **空白设置**：在问题中精心选择一处关键信息留空如______，确保填空的答案直接来源于原文或可由原文推断得出。
                            2. **填空题格式**：严格按以下生成示例，中文格式，question_type_id为整数类型且值固定为1，question为字符串类型，answer为字符串类型
                            3.所生成的问题直接且紧密地关联于文章的核心信息。
                            4.所生成问题和答案有高匹配度。
                            5.所生成的问题要表述完美，逻辑清晰，易于理解。
                         ### 生成示例（仅供参考，实际生成内容需依据上述要求）:
                         {{'question_type_id': 1, 'question': '战斗机、轰炸机和侦察机的留空时间取决于空中加油路径与的______接近程度。', 'answer': '战斗空域'}}
                         {{'question_type_id': 1, 'question': '自适应基地的概念基于灵活分散的理念，提升作战______能力。', 'answer': '机动'}}
                         """
    # 调用deepseek API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


# 生成10个单选题
def qag_dx(text):
    prompt = f"""任务说明：作为军事装备领域的专家，请一步步思考，仔细分析下方文章内容，生成十个高质量且内容不同的中文单选题问答对，只输出结果即可，不需要任何解释.
                           ###文章内容:
                           {text}
                           ### 生成单选题要求:
                              1. **单选题格式**：严格按以下生成示例，中文格式，question_type_id为整数类型且值固定为2，question为字符串类型，choices为数组类型,包含四种答案如[A，B，C，D]，answer为字符串类型，只能为A或B或C或D
                              2.所生成的问题直接且紧密地关联于文章的核心信息。
                              3.所生成问题和答案有高匹配度。
                              4.所生成的问题要表述完美，逻辑清晰，易于理解。
                           ### 生成示例（仅供参考，实际生成内容需依据上述要求）:
                           {{'question_type_id':2, 'question': '为增强美空中加油机战备态势，并确保更全面的作战范围，美军寻求在未来的全球部队管理计划中增加______中队的数量。', 'choices': ['A战斗机', 'B后勤', 'C飞行员', 'D加油机'], 'answer': 'D'}}
                           {{'question_type_id': 2, 'question': '美国将与印太区域合作伙伴签订新的空中加油机基地协议，不包括以下哪个地区？', 'choices': ['A东亚一', 'B东南亚', 'C大洋洲', 'D南美洲'], 'answer': 'D'}}
                           {{'question_type_id': 2, 'question': '2019年美军在________中阐明印太司令部的军事战略，通过摆出战斗姿态，将作战可靠的部队部署在前沿地带，迫使敌人通过符合国际公认规则的良性手段推进其利益。', 'choices': ['A 《印太战略报告》', 'B 《海洋公约》', 'C 《印太时局分析》', 'D 《安全公约》'], 'answer': 'A'}}
                    """
    # 调用deepseek API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


# 生成10个判断题
def qag_pd(text):
    prompt = f"""任务说明：作为军事装备领域的专家，请一步步思考，仔细分析下方文章内容，生成十个高质量且内容不同的中文判断题问答对，只输出结果即可，不需要任何解释.
                       ###文章内容:
                       {text}
                       ### 生成判断题要求:
                          1. **判断题格式**：严格按以下生成示例，中文格式，question_type_id为整数类型且值固定为3，question为字符串类型，answer为字符串类型
                          2.所生成的问题直接且紧密地关联于文章的核心信息。
                          3.生成问题和答案有高匹配度。
                          4.所生成的问题要表述完美，逻辑清晰，易于理解。
                       ### 生成示例（仅供参考，实际生成内容需依据上述要求）:
                       {{'question_type_id': 3, 'question': '自适应基地是一个旨在提升空中资产生存能力的概念。', 'answer': '对'}}
                       {{'question_type_id': 3, 'question': '自适应基地这一概念，在反介入/区域拒止环境中具备持久作战的能力。', 'answer': '对'}}
                       {{'question_type_id': 3, 'question': '2019年，美国认为其空军的空中加油机机队现状不满足印太司令部提出的自适应基地概念的需求。', 'answer': '对'}}
                       """

    # 调用deepseek API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content



# 生成2个复杂题
def qag_fz(text):
    # 初始化对话历史
    dialog_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    prompt = f"""任务说明：您是一位在军事装备领域拥有深厚专业知识的专家，仔细阅读并分析下方军事装备领域文章内容，生成两个高质量且内容不同的中文复杂问答题问答对，需要根据复杂度和质量和格式要求进行一步步思考。思考步骤一一列出。
                     ###复杂度要求：
                            #问题深度：问题要求深入理解文章主题或涉及高级概念；
                            #逻辑结构:问题与答案的逻辑要非常复杂，而且要包含多层次推理；
                            #语言表达: 需要使用复杂的词汇、术语或句式结构；
                            #答案需要通过阅读多个段落获得，需要出现经过总结推理后的文字。
                     ###质量要求:
                            #1.所生成的问题直接且紧密地关联于文章的核心信息。
                            #2.所生成问题和答案有高匹配度。
                            #3.所生成问题要表述得非常清晰、语法要非常正确、逻辑要非常连贯。
                     ###格式要求:
                            #1. **复杂问答题格式**：严格按以下生成示例，中文格式，question_type_id为整数类型且值固定为4，question为字符串类型，answer为字符串类型。
                     ### 生成示例:
                     {{'question_type_id': 4, 'question': '美国空军加油机的“自适应基地”构想是什么？', 'answer': '这一概念设想在面临空中威胁的情况下，部队能够从多个规模更小、更分散、更具弹性的基地进行部署、战场生存、作战、机动并迅速恢复战力。'}}
                     {{'question_type_id': 4, 'question': '美印太司令部空中加油机适应性基地的两种替代方案是什么？', 'answer': '方案之一，寻求在未来的全球部队管理计划中增加加油机中队的数量。方案之二，美国与遍及东亚、东南亚和大洋洲的区域合作伙伴签订新的空中加油机基地协议。'}}
                    ###文章内容:
                     {text}
                     """
    # 将用户请求添加到对话历史
    dialog_history.append({"role": "user", "content": prompt})
    # 调用qwen2API
    resp = dashscope.Generation.call(
        model='qwen2-72b-instruct',
        messages=dialog_history
    )
    #  第一次生成
    # print("第一次生成结果：++++++++++++")
    # print(resp.output.text)
    dialog_history.append({"role": "assistant", "content": resp.output.text})

    prompt_2 = f'''根据思考步骤的反馈，重新生成新的复杂度高的问答对。'''
    # 将用户请求添加到对话历史
    dialog_history.append({"role": "user", "content": prompt_2})
    # 调用API
    resp = dashscope.Generation.call(
        model='qwen2-72b-instruct',
        messages=dialog_history
    )
    # #  第二次生成
    # print("第二次生成结果：++++++++++++")
    print(resp.output.text)
    return resp.output.text

# 生成问题总入口
def qag(text, question_type):
    # question_type:填空题，单选题，判断题，复杂问答题

    if question_type == '填空题':
        return qag_tk(text)

    if question_type == '单选题':
        return qag_dx(text)

    if question_type == '判断题':
        return qag_pd(text)

    if question_type == '复杂问答题':
        return qag_fz(text)

# 生成结果后处理，使其符合要求格式
def parse_content(content):
    try:
        # 尝试使用literal_eval转换字符串
        result = ast.literal_eval(content)
        return result
    except (ValueError, SyntaxError) as e:
        print(content)
        pattern_question_type_id = r"(?:question_type_id':|question_type_id:)\s*(.*?),"
        match_question_type_id = re.search(pattern_question_type_id, content).group(1)

        pattern_question = r"(?:question':|question:)\s*(.*?),"
        match_question = re.search(pattern_question, content).group(1).replace("'", "")

        pattern_answer = r"(?:answer':|answer:)\s*(.*?)}"
        match_answer = re.search(pattern_answer, content).group(1).replace("'", "")

        if match_question_type_id == 2:
            pattern_choices = r"(?:choices':|choices:)\s*\[(.*?)\],"
            match_choices = re.search(pattern_choices, content).group(1).replace("'", "")
            result = {
                'question_type_id': int(match_question_type_id),
                'question': match_question,
                'choices': [match_choices],
                'answer': match_answer
            }
        else:
            result = {
                'question_type_id': match_question_type_id,
                'question': match_question,
                'answer': match_answer
            }
        return result

# 评分处理问题和选项结合
def combine_question_and_choices(row):
    question = row.get('question')
    choices = row.get('choices', [])  # 如果'choices'不存在，默认为空列表
    choices_str = f" 选项: {', '.join(choices)}" if choices else ""  # 只有当有choices时才拼接选项部分
    return f"{question}{choices_str}"

# 将字符串形式的字典转换为实际字典
def safe_literal_eval(resp_str):
    try:
        # 尝试使用literal_eval转换字符串
        result = ast.literal_eval(resp_str)
        return result
    except (ValueError, SyntaxError) as e:
        # 如果转换失败，打印错误信息并返回None或者其他默认值
        print(f"Error evaluating literal in string: {resp_str}. Error: {e}")

        return None  # 或者根据需要返回某个默认值
# 评分处理获取分数
def extract_score_enhanced(text):
    # 匹配所有指定格式并提取数字
    match = re.search(r'\b(score":|score":\s*|score: |Score: |score:\*\* |score of |score of \*\*|rate this question |as |评分为|评分：|评分结果：)(\d+)', text)
    if match:
        return int(match.group(2))
    return None

# 问题相关性：S1
def evaluate_question_relevance(text, question):
    """
    评估问题与文章内容的相关性。
    """
    prompt = f'''
    ###文章内容:
    {text}

    ###问题:
    {question}

    ###评分结果示例：

    {{"score":78}}


    ###任务:
    请分析上述问题与提供的文章内容的相关性，并给出一个0到100的分数来量化这种相关性。0表示完全不相关，100表示问题直接且紧密地关联于文章的核心信息。同时，请遵循评分结果示例的格式返回结果，不需要任何解释。
    '''
    # 调用deepAPI
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content":prompt},
        ],
        stream=False
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content

# 问题与答案匹配度：S2
def evaluate_answer_match(text, question_type, question, answer):
    """
    评估问题与答案的匹配度。
    """
    # 问答匹配度:S2
    prompt = f'''
    ###文章内容:
    {text}

    ###问题类型:
    {question_type}

    ###问题:
    {question}

    ###答案:
    {answer}

    ###评分结果示例：
    {{ "score":78}}


    ###任务:
    请综合考虑文章内容、问题类型以及提供的问题与答案，评估它们之间的匹配度。特别注意，问题类型对评价标准有重要影响：例如，事实性问题的答案需直接且准确引用文章中的信息；解释性问题则要求答案能合理解析文章相关内容；推理性问题的解答应基于文章内容进行合理推断。请仅输出一个0到100的整数，用来量化问题与答案的匹配程度，其中0表示完全不匹配，100表示答案完美符合问题要求及类型标准。同时，请遵循评分结果示例的格式返回结果，不需要任何解释。
    '''
    # 调用API
    # 调用API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content

# 问题流畅度：S3
def evaluate_fluency_question(question_type, question_text_with_choices):
    """
    评估问题流畅度。
    """
    prompt = f'''
    ###问题类型:
    {question_type}

    ###问题内容:
    {question_text_with_choices}

    ###评分结果示例：

     {{"score":78}}


    ###任务:
    请依据问题类型及内容，评估该问题表述的清晰度、语法正确性、逻辑连贯性以及对目标受众的适宜性。其中0分表示问题表述极不流畅，存在严重理解障碍；100分表示问题表述完美，逻辑清晰，易于理解。
    同时，请遵循评分结果示例的格式返回结果，不需要任何解释。
    '''
    # 调用API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content

# 答案流畅度：S4
def evaluate_fluency_answer(question_type, answer):
    if question_type == "复杂问答题":
        """
        评估答案的流畅度。
        """
        # 流畅度评估可能需要根据文本长度、语法结构等因素综合判断
        # 这里仅做示意，实际应调用模型
        prompt = f'''
        ###问题类型:
        {question_type}

        ###答案内容:
        {answer}

        ###评分结果示例：
         {{"score":78}}


        ###任务:
        请依据问题类型及答案内容，评估该答案表述的清晰度、语法正确性、逻辑连贯性以及对目标受众的适宜性。其中0分表示答案表述极不流畅，存在严重理解障碍；100分表示答案表述完美，逻辑清晰，易于理解。
        同时，请遵循评分结果示例的格式返回结果，不需要任何解释。
        '''
         # 调用API

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        # print(response.choices[0].message.content)
        return response.choices[0].message.content
    else:
        return 0
# 问题复杂度：S5
def evaluate_complexity(question_type, text, question_text_with_choices, answer):
        if question_type == "复杂问答题":
            """
            评估问题的复杂度。
            """
            prompt = f'''
            ###文章内容:
            {text}

            ###问答对:
            **问题:**{question_text_with_choices}
            **回答:**{answer}

            ###评分结果示例：

            {{ "score":78}}


            ###复杂度评估任务:
            请根据文章内容及上述问答对，评估该问答对的复杂程度。复杂度考量因素包括但不限于：
            -**问题深度:**问题是否要求深入理解文章主题或涉及高级概念？
            -**逻辑结构:**问题与答案的逻辑是否复杂，是否包含多层次推理？
            -**语言表达:**是否使用了复杂的词汇、术语或句式结构？
            -**跨段落:**问题的答案是否需要通过阅读多个段落获得？

            请给出一个0-100的分数来量化其复杂程度，其中0表示非常简单，100表示极其复杂。同时，请遵循评分结果示例的格式返回结果，不需要任何解释。
            '''
            # 调用API
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": prompt},
                ],
                stream=False
            )
            # print(response.choices[0].message.content)
            return response.choices[0].message.content
        else:
            return 0

# 计算每个问答对的Sq
def calculate_score(question_type_id, s1, s2, s3, s4, s5):
    if question_type_id == 4:

        sq = 0.2 * s1 + 0.2 * s2 + 0.1 * s3 + 0.1 * s4 + 0.4 * s5
    else:
        sq = 0.4 * s1 + 0.4 * s2 + 0.2 * s3

    return sq
# 获取Sq 值最高的前两个和三个记录
def top_records(group):
    if group['question_type_id'].iloc[0] in [1, 4]:
        # 如果 question_type_id 是 1 或 4，则取 Sq 值最高的前两个记录
        return group.nlargest(2, 'Sq')
    else:
        # 否则取 Sq 值最高的前三个记录
        return group.nlargest(3, 'Sq')
# 主函数
if __name__ == "__main__":
    # # 获取当前目录
    current_dir = os.getcwd()
    # 读取document_test文件,包含10篇文章。需要进行修改为测试的文档
    file_path_doc = os.path.join(current_dir, 'document_test')
    data_doc = pd.read_csv(file_path_doc)

    # 生成10个填空题、单选题、复杂问答题，重复生成复杂问答题
    question_type=['填空题','单选题','判断题','复杂问答题']
    resp_list = []
    for text in data_doc['content']:
        resps=' '
        for  value in question_type:
            resp = qag(text,value)
            resps+=resp
        resp_list.append(resps)
    data_doc['qa']=resp_list
    # 保存为初始结果
    data_doc.to_csv('初始问答对.csv', index=False)
    # 生成结果后处理
    file_path_qa = os.path.join(current_dir, '初始问答对.csv')
    df_original = pd.read_csv(file_path_qa)
    # 初始化qa_id计数器
    qa_id_counter = 1
    new_rows = []
    for index, row in df_original.iterrows():
        contents = re.findall(r'\{[^{}]*\}', row['qa'])
        for content in contents:
            new_rows.append({
                'qa_id': f'qa_{qa_id_counter}',
                'doc_id': row['doc_id'],
                'content': content
            })
            qa_id_counter += 1
    df_new = pd.DataFrame(new_rows)
    df_new['content'] = df_new['content'].apply(parse_content)
    df_new.to_csv('qa_格式问答对.csv', index=False)

    # qa_格式问答对评分
    file_path_doc = os.path.join(current_dir, 'qa_格式问答对.csv')
    merged_df = pd.read_csv(file_path_doc)
    # 将字符串形式的字典转换为实际字典
    merged_df['qa_dic'] = merged_df['content'].apply(safe_literal_eval)

    question_type_mapping = {
        1: "填空题",
        2: "单选题",
        3: "判断题",
        4: "复杂问答题"
    }

    # 提取'question_type_id'
    merged_df['question_type_id'] = merged_df['qa_dic'].apply(lambda x: x.get('question_type_id'))

    # 使用映射关系添加'question_type'列
    merged_df['question_type'] = merged_df['question_type_id'].map(question_type_mapping)

    merged_df['question_text_with_choices'] = merged_df['qa_dic'].apply(combine_question_and_choices)

    # 提取'answer'
    merged_df['answer'] = merged_df['qa_dic'].apply(lambda x: x.get('answer'))

    # 进行评分
    # S1得分
    merged_df['raw_S1'] = merged_df.apply(
        lambda row: evaluate_question_relevance(row['content'], row['question_text_with_choices']), axis=1)
    # 应用这个增强版函数到merged_df的'raw_S1'列
    merged_df['S1'] = merged_df['raw_S1'].apply(extract_score_enhanced)
    print("S1评分结束")
    # S2得分
    merged_df['raw_S2'] = merged_df.apply(
        lambda row: evaluate_answer_match(row['content'], row['question_type'], row['question_text_with_choices'],
                                          row['answer']), axis=1)

    # 应用这个增强版函数到merged_df的'raw_S2'列
    merged_df['S2'] = merged_df['raw_S2'].apply(extract_score_enhanced)
    print("S2评分结束")
    # S3得分
    merged_df['raw_S3'] = merged_df.apply(
        lambda row: evaluate_fluency_question(row['question_type'], row['question_text_with_choices']), axis=1)
    # 应用这个增强版函数到merged_df的'raw_S3'列
    merged_df['S3'] = merged_df['raw_S3'].apply(extract_score_enhanced)
    print("S3评分结束")
    # S4得分
    merged_df['raw_S4'] = merged_df.apply(lambda row: evaluate_fluency_answer(row['question_type'], row['answer']),
                                          axis=1)
    merged_df['S4'] = merged_df.apply(
        lambda row: extract_score_enhanced(row['raw_S4']) if row['raw_S4'] != 0 else 0, axis=1)
    print("S4评分结束")
    # S5得分
    merged_df['raw_S5'] = merged_df.apply(
        lambda row: evaluate_complexity(row['question_type'], row['content'], row['question_text_with_choices'],
                                        row['answer']), axis=1)
    merged_df['S5'] = merged_df.apply(
        lambda row: extract_score_enhanced(row['raw_S5']) if row['raw_S5'] != 0 else 0, axis=1)
    print("S5评分结束")
    merged_df['Sq'] = merged_df.apply(
        lambda row: calculate_score(row['question_type_id'], row['S1'], row['S2'],
                                    row['S3'], row['S4'], row['S5'], ), axis=1)
    # 保存为CSV
    merged_df.to_csv('qa_格式问答对_score.csv', index=False, encoding='utf-8')

    # 获取前2，前3的问答对
    file_path_doc = os.path.join(current_dir, 'qa_格式问答对_score.csv')
    data = pd.read_csv(file_path_doc)
    # 应用函数到每个分组
    result = data.groupby(['doc_id', 'question_type_id']).apply(top_records).reset_index(drop=True)
    # 显示结果
    print(result)
    result['qa_id'] = 'qa_' + (result.index + 1).astype(str)
    # 只保留需要的列
    result = result[['qa_id', 'doc_id', 'content']]
    result.to_csv('final_qa.csv', index=False, encoding='utf-8')

