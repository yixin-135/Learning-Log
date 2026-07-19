import sys
import json
import os

DATA_FILE = "data.json"

def load_data():
      if os.path.exists(DATA_FILE):
          with open(DATA_FILE, "r", encoding="utf-8") as f:
              return json.load(f)
      return {"todos": [], "info": {}}

def save_data(data):
      with open(DATA_FILE, "w", encoding="utf-8") as f:
          json.dump(data, f, ensure_ascii=False, indent=2)

def main():
      if len(sys.argv) < 2:
          print("用法: python campus.py [search|todo] ...")
          return

      data = load_data()
      cmd = sys.argv[1]

      if cmd == "search":
          print("搜索功能开发中...")
      elif cmd == "todo":
          action = sys.argv[2]
          data = load_data()
          todos = data.get("todos", [])
          if action == "add":
               task = " ".join(sys.argv[3:])
               todos.append({"task": task, "done": False})
               data["todos"] = todos
               save_data(data)
               print(f"已添加待办: {task}")
          elif action == "list":
            if not todos:
              print("暂无待办")
            else:
              print("\n待办列表:")
              for i, t in enumerate(todos, 1):
                  status = "✓" if t["done"] else "○"
                  print(f"  [{status}] {i}. {t['task']}")
          elif action == "done":
           num = int(sys.argv[3])
           if 1 <= num <= len(todos):
               todos[num - 1]["done"] = True
               data["todos"] = todos
               save_data(data)
               print(f"已完成: {todos[num - 1]['task']}")
          else:
              print("待办编号无效")
      else:
          print(f"未知命令: {cmd}")

if __name__ == "__main__":
      main()