import pandas as pd
import matplotlib.pyplot as plt

# 防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载泰坦尼克号数据集
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print("=== 数据概览 ===")
print(df.head())
print(f"\n总人数: {len(df)}, 存活: {df['Survived'].sum()}, 遇难: {len(df) - df['Survived'].sum()}")

# 图1: 男女存活率
plt.figure(figsize=(6, 4))
survived_by_sex = df.groupby("Sex")["Survived"].mean()
print(f"\n男女存活率:\n{survived_by_sex}")
survived_by_sex.plot(kind="bar", color=["steelblue", "pink"])
plt.title("男女存活率")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 图2: 船舱等级存活率
plt.figure(figsize=(6, 4))
survived_by_class = df.groupby("Pclass")["Survived"].mean()
print(f"\n船舱等级存活率:\n{survived_by_class}")
survived_by_class.plot(kind="bar", color=["gold", "silver", "#8B4513"])
plt.title("船舱等级存活率")
plt.ylabel("Survival Rate")
plt.xlabel("1=头等舱 2=二等舱 3=三等舱")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 图3: 年龄分布
plt.figure(figsize=(8, 4))
df["Age"].dropna().hist(bins=30, color="steelblue", edgecolor="white")
plt.title("乘客年龄分布")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print("\n=== 分析结论 ===")
print(f"1. 女性存活率 {survived_by_sex['female']:.0%}，男性 {survived_by_sex['male']:.0%}  —— 妇女优先")
print(f"2. 头等舱存活率 {survived_by_class[1]:.0%}，三等舱 {survived_by_class[3]:.0%}  —— 有钱人先走")
print(f"3. 船上乘客平均年龄 {df['Age'].mean():.0f} 岁，大部分 20-40 岁")
