# CCKS2024_MQATG
CCKS2024_基于大模型的军事装备领域问答生成技术评测
# 任务定义
根据给定的军事装备领域文章，生成10个问题答案对，其包含2道填空题、3道单选题、3道判断题以及2道复杂问答题。
### 如下图举例所示
![image](https://github.com/user-attachments/assets/9cc1f4dd-166e-4572-b075-81196f065959)
![image](https://github.com/user-attachments/assets/2a17f1bb-66c1-4395-a37e-1a5c5582a5aa)

# 评价指标

从五个维度来评估生成的问答与答案的质量，每个维度的评分通过使用给定的Prompt来调用DeepSeek-V2-0628大模型得出。
### 五个维度如下
![image](https://github.com/user-attachments/assets/da486c31-5537-4c38-91dc-1a0c5691c445)

### 其中复杂度评分Prompt如下
![image](https://github.com/user-attachments/assets/d208e2c5-3bf1-43d9-82dd-d40182e4e5a8)

### 每个类型题目维度总分计算公式
![image](https://github.com/user-attachments/assets/6f91d6a5-bc14-4e76-aee5-12b271060896)

# 实现方案要求
![image](https://github.com/user-attachments/assets/00c00bfa-bfe2-49a9-b8c9-9038a7d24f2f)

# 解决方案概述
![image](https://github.com/user-attachments/assets/69a3976f-4439-44cf-8fd0-b4d60fe2142e)

### 开源模型选择结果
![image](https://github.com/user-attachments/assets/21a636b5-ba73-419e-92de-3aba90cd3a34)

### 填空题Prompt设计
![image](https://github.com/user-attachments/assets/8035eb84-ffa9-4e9b-ad2b-ce5a3660f7d4)

### 复杂问答题Prompt设计
![image](https://github.com/user-attachments/assets/d64e6075-5246-4043-8453-80db838ef11b)

### 生成框架

![image](https://github.com/user-attachments/assets/b7c49f7f-6932-4967-b8aa-b5155774249c)

# 比赛结果
![image](https://github.com/user-attachments/assets/8cde9201-c32c-424b-87c4-aa450d0c9d2a)
