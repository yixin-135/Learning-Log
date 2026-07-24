import sys
print(sys.argv)
print(len(sys.argv))

import json

  # 存
data = {"name": "张三", "score": 90}
with open("test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

print("存好了")

  # 读
with open("test.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"读回来: {loaded}")
print(f"名字: {loaded['name']}, 分数: {loaded['score']}")

import json

  # 读现有的 data.json
with open("data.json", "r", encoding="utf-8") as f:
      data = json.load(f)

todos = data["todos"]   # 取待办列表
print(f"当前有 {len(todos)} 条待办")

  # 加一条
todos.append({"task": "复习Python", "done": False})
data["todos"] = todos

  # 存回去
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("加了一条，现在列表：")
for t in data["todos"]:
    print(f"  {t['task']} - {'✓' if t['done'] else '○'}")