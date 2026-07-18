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
          print("待办功能开发中...")
      else:
          print(f"未知命令: {cmd}")

if __name__ == "__main__":
      main()