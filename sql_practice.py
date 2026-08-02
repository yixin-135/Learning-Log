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

 # ===== 第 3 课：JOIN 联表查询 =====

  # 建第二张表 - 选课表
cur.execute("""
      CREATE TABLE IF NOT EXISTS courses (
          id INTEGER PRIMARY KEY,
          student_id INTEGER,
          course_name TEXT
      )
  """)

courses = [
      (1, 1, "Python程序设计"),
      (2, 1, "数据结构"),
      (3, 2, "Python程序设计"),
      (4, 3, "数据结构"),
      (5, 3, "操作系统"),
      (6, 4, "操作系统"),
      (7, 5, "Python程序设计"),
      (8, 5, "数据结构"),
  ]
cur.executemany("INSERT OR REPLACE INTO courses VALUES (?, ?, ?)", courses)
conn.commit()

  # 两张表的数据：
  # students: id, name, score, grade
  # courses:  id, student_id, course_name
  # courses.student_id 对应 students.id

  # JOIN: 把学生名字和他们选的课连在一起
print("\n=== 每个学生选了哪些课（INNER JOIN）===")
for row in cur.execute("""
      SELECT students.name, courses.course_name
      FROM students
      JOIN courses ON students.id = courses.student_id
  """):
      print(row)

  # LEFT JOIN: 包含没选课的学生
print("\n=== 所有学生（包括没选课的）===")
for row in cur.execute("""
      SELECT students.name, courses.course_name
      FROM students
      LEFT JOIN courses ON students.id = courses.student_id
  """):
      print(row)

#查询 1：按分数排名（分数一样排同一名）
print("\n=== 分数排名 ===")
for row in cur.execute("SELECT name, score, RANK() OVER (ORDER BY score DESC) as ranking FROM students"):
     print(row)
#查询 2：给每行一个序号
print("\n=== 行号 ===")
for row in cur.execute("SELECT name, score, ROW_NUMBER() OVER (ORDER BY score DESC) as row_num FROM students"):
     print(row)

#1：每门课有多少人选
print("\n=== 每门课有多少人选 ===")
for row in cur.execute("SELECT course_name, COUNT(*) FROM courses GROUP BY course_name"):
      print(row)

#2：选了 Python程序设计 的学生名字和分数
print("\n=== 选了 Python程序设计 的学生名字和分数 ===")
for row in cur.execute("""
        SELECT students.name, students.score
        FROM students
        JOIN courses ON students.id = courses.student_id
        WHERE courses.course_name = 'Python程序设计'
    """):
        print(row)
conn.close()
