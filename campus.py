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
        print("=" * 40)
        print("  北交大校园助手")
        print("=" * 40)
        print("  python campus.py search <关键词>      搜索信息")
        print("  python campus.py search add <词> <内容> 添加信息")
        print("  python campus.py todo add <任务>      添加待办")
        print("  python campus.py todo list           查看待办")
        print("  python campus.py todo done <编号>     完成待办")
        print("  python campus.py todo del <编号>      删除待办")
        return

    cmd = sys.argv[1]

    if cmd == "search":
        action = sys.argv[2] if len(sys.argv) > 2 else ""
        if action == "add":
            key = sys.argv[3] if len(sys.argv) > 3 else ""
            detail = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else ""
            if key and detail:
                data = load_data()
                info = data.get("info", {})
                info[key] = detail
                data["info"] = info
                save_data(data)
                print(f"已添加信息: {key}")
            else:
                print("请输入关键词和内容，例如: python campus.py search add 快递 地址")
        else:
            keyword = action
            if keyword:
                data = load_data()
                info = data.get("info", {})
                found = False
                for name, detail in info.items():
                    if keyword in name or keyword in detail:
                        print(f"\n【{name}】")
                        print(f"  {detail}")
                        found = True
                if not found:
                    print(f"\n未找到关于「{keyword}」的信息")
            else:
                print("请输入搜索关键词，例如: python campus.py search 图书馆")

    elif cmd == "todo":
        action = sys.argv[2] if len(sys.argv)>2 else ""
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
        elif action == "del":
            num = int(sys.argv[3])
            if 1 <= num <= len(todos):
                removed = todos.pop(num - 1)
                data["todos"] = todos
                save_data(data)
                print(f"已删除: {removed['task']}")
            else:
                print("待办编号无效")
        else:
            print(f"未知操作: {action}")
            print("可用: add <内容> | list | done <编号> | del <编号>")

    else:
        print(f"未知命令: {cmd}")

if __name__ == "__main__":
    main()
