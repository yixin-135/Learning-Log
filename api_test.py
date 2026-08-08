import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

# 一篇关于校园生活的文档
document = """
北京交通大学位于北京市海淀区，是一所以交通为特色的重点大学。
学校设有电子信息工程学院、计算机与信息技术学院、交通运输学院等多个学院。
图书馆位于校园中心，共五层，开放时间为每天08:00-22:00。
学生食堂包括学一食堂、学二食堂和清真食堂，分布在校园东西两侧。
本科生宿舍为六人间，配备空调，晚上23:00实行门禁管理。
校园卡可用于食堂消费、图书馆借书、宿舍门禁等场景。
奖学金评选每年9月进行，包括国家奖学金8000元和校级奖学金3000元。
"""

# 第1步：按段落分块
chunks = [line.strip() for line in document.strip().split("\n") if line.strip()]

print(f"总共 {len(chunks)} 个段落:")
for i, chunk in enumerate(chunks):
    print(f"\n--- 段落 {i+1} ---")
    print(chunk)

# 中文分词函数
def tokenize(text):
    return " ".join(jieba.cut(text))

# 第2步：分词后向量化
jieba_chunks = [tokenize(c) for c in chunks]
vectorizer = TfidfVectorizer()
chunk_vectors = vectorizer.fit_transform(jieba_chunks)

print(f"\n向量维度: {chunk_vectors.shape}")
print(f"{len(chunks)} 个段落，每个变成了 {chunk_vectors.shape[1]} 维的向量")

# 第3步：用户提问，找最相关段落
query = "图书馆几点关门"
query_terms = tokenize(query)
query_vector = vectorizer.transform([query_terms])

similarities = cosine_similarity(query_vector, chunk_vectors)[0]

print(f"\n问题: {query}")
print(f"\n各段落相似度得分:")
for i, score in enumerate(similarities):
    print(f"  段落 {i+1}: {score:.4f}  | {chunks[i][:50]}...")

# 取前 3 个最相关段落
import numpy as np
top3_idx = np.argsort(similarities)[-3:][::-1]  # 相似度最高的 3 个
print(f"\n前 3 个最相关段落:")
for i in top3_idx:
    print(f"  段落 {i+1}: {similarities[i]:.4f} | {chunks[i][:50]}...")

  # 把前 3 段拼成上下文
context = "\n".join([chunks[i] for i in top3_idx])
prompt = f"""你是一个校园助手。请根据以下文档内容回答用户的问题。
  如果文档中没有相关信息，请回答"我不清楚"。

  文档内容：
  {context}

  用户问题：{query}

  回答："""

client = OpenAI(
    api_key="REDACTED",
    base_url="https://api.deepseek.com"
  )
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
          {"role": "system", "content": "你是北京交通大学校园助手"},
          {"role": "user", "content": prompt}
      ]
  )

print(f"\n=== AI 基于文档的回答 ===")
print(response.choices[0].message.content)
