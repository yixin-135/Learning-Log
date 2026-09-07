# ReAct 第一课：我亲手跑的 Agent

1. 什么是 ReAct：LLM 通过 Thought（思考）→ Action（行动）→ Observation（观察）循环，直到 Finish。
2. 我做了什么：改了 tools.py 里的工具，让 Agent 回答"图书馆几点关门"，它搜索后正确回答 22:00。
3. 我观察到的关键：第 2 步会根据第 1 步的观察结果改变决策——信息够了就直接 Finish，不够就换个思路。

教训：报错不可怕，读了错误信息才知道是 serpapi 版本问题。