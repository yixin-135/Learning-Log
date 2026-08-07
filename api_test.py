from openai import OpenAI

  # DeepSeek API 跟 OpenAI 格式兼容
client = OpenAI(
      api_key="sk-cf2cbefc35f5416d8f33f7cd5d8855a3",
      base_url="https://api.deepseek.com"
  )

response = client.chat.completions.create(
      model="deepseek-chat",
      messages=[
          {"role": "system", "content": "你是一个Python学习助手"},
          {"role": "user", "content": "用一句话解释什么是RAG"}
      ]
  )

print(response.choices[0].message.content)