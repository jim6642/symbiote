# 场景目录

Symbiote 的核心能力之一是**场景感知**——AI 根据当前环境自动切换行为模式。

每个场景文件定义了：
- 场景描述和触发条件
- 感知信号组合
- AI 行为模式（对人类 + 对外界）
- 人格配置文件
- 边界条件（什么情况下不触发）

---

## 场景列表

| # | 场景 | 核心能力 | 文档 |
|---|------|---------|------|
| 1 | 工作决策 | 数据分析 + 方案评估 + 沟通起草 | [work-decision.md](./work-decision.md) |
| 2 | 旅行导航 | 路线规划 + 景点讲解 + 偏好协调 | [travel-navigation.md](./travel-navigation.md) |
| 3 | 亲密空间 | 情感共鸣 + 氛围感知 + 沉默陪伴 | [intimate-space.md](./intimate-space.md) |
| 4 | 内容消费 | 真实兴趣识别 + 平台信号代理 | [content-consumption.md](./content-consumption.md) |
| 5 | 社交互动 | 微表情/语气分析 + 话题建议 + 形象保护 | [social-encounter.md](./social-encounter.md) |
| 6 | 学习专注 | 注意力管理 + 记忆强化 + 节奏调节 | [learning-focus.md](./learning-focus.md) |
| 7 | 紧急事件 | 风险评估 + 快速响应 + 多方协调 | [crisis-emergency.md](./crisis-emergency.md) |
| 8 | 日常管理 | 习惯追踪 + 时间优化 + 琐事自动化 | [daily-routine.md](./daily-routine.md) |

---

## 场景叠加

场景不是互斥的。一个用户可能同时处于多个场景：

```
例如：
  场景组合 = [WORK_SOLO, LEARNING_FOCUSED]
  → AI 行为：工作模式（理性）+ 专注保护（不打扰 + 降噪）

  场景组合 = [TRAVEL_TRANSIT, CONTENT_SCROLLING]
  → AI 行为：旅行模式（轻松）+ 内容推荐（推荐与旅途相关的内容）

  场景组合 = [INTIMATE_CONFLICT, TIME_LATE_NIGHT]
  → AI 行为：亲密模式 + 时间敏感 → 极度克制，几乎不主动输出
```

## 场景切换

场景切换必须平滑、无感知。用户不应该意识到"AI 切换模式了"——它只是自然地做出了恰当的回应。
