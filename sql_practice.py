import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("""
      CREATE TABLE IF NOT EXISTS students (
          id INTEGER PRIMARY KEY,
          name TEXT,
          score INTEGER,
          grade TEXT
      )
  """)

students = [
      (1, "张三", 85, "大二"),
      (2, "李四", 92, "大一"),
      (3, "王五", 78, "大三"),
      (4, "赵六", 88, "大二"),
      (5, "陈七", 95, "大一"),
  ]
cur.executemany("INSERT OR REPLACE INTO students VALUES (?, ?, ?, ?)", students)
conn.commit()

print("=== 所有学生 ===")
for row in cur.execute("SELECT * FROM students"):
      print(row)

print("\n=== 大一学生 ===")
for row in cur.execute("SELECT name, score FROM students WHERE grade = '大一'"):
      print(row)

print("\n=== 按分数降序 ===")
for row in cur.execute("SELECT name, score FROM students ORDER BY score DESC"):
      print(row)

print("\n=== 前3名 ===")
for row in cur.execute("SELECT name, score FROM students ORDER BY score DESC LIMIT 3"):
      print(row)

# 1. 查分数大于 85 的学生
print("\n=== 分数大于85的学生 ===")
for row in cur.execute("SELECT name,score FROM students WHERE score >= 85"):
      print(row)

# 2. 查大二学生，按分数从低到高排
print("\n=== 大二学生，按分数升序 ===")
for row in cur.execute("SELECT name,score FROM students WHERE grade = '大二' ORDER BY score"):
      print(row)

# 3. 查分数最高的一个人
print("\n=== 分数最高的一个人 ===")
for row in cur.execute("SELECT name,score FROM students ORDER BY score DESC LIMIT 1"):
      print(row)

# ===== 第 2 课：分组聚合 =====

print("\n=== 每个年级人数 ===")
for row in cur.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade"):
      print(row)

print("\n=== 每个年级平均分 ===")
for row in cur.execute("SELECT grade, AVG(score) FROM students GROUP BY grade"):
      print(row)

print("\n=== 每个年级最高最低分 ===")
for row in cur.execute("SELECT grade, MAX(score), MIN(score) FROM students GROUP BY grade"):
      print(row)

print("\n=== 平均分 > 85 的年级 ===")
for row in cur.execute("SELECT grade, AVG(score) FROM students GROUP BY grade HAVING AVG(score) > 85"):
      print(row)

conn.close()
