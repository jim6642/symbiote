# 代理输出层规格

> Symbiote 对外的"嘴"——在用户授权下，替用户与外部系统对话。

---

## 定位

代理输出层是 Symbiote 区别于所有现有 AI 助手的关键差异。

现有 AI：只对人说话。
Symbiote：对人说话 + 对外界说话。

---

## 输出管道

```
意图引擎确定"需要告诉外界什么"
  → 检查同意模型："用户授权了吗？"
    → 是 → 脱敏处理 → 生成审计日志 → 发送
    → 否 → 丢弃（可选的 whisper 提示："你想告诉 [系统] 吗？"）
```

---

## 支持的输出类型

### 1. 偏好声明 (Preference Declaration)

告知平台用户的真实偏好，修正平台基于表面行为的错误推断。

```json
{
  "type": "PREFERENCE_DECLARATION",
  "target": "platform:content_recommendation",
  "action": "CORRECT",
  "surface_behavior": "quick_skip",
  "true_preference": "high_interest_socially_blocked",
  "content_category": "curiosity_edge",
  "correction_weight": 0.87,
  "timestamp": "2026-06-24T14:30:00Z"
}
```

**用途**：修正抖音的推荐算法，告诉它"用户喜欢这个，只是不方便看"。

### 2. 状态广播 (Status Broadcast)

告知外部系统用户的当前状态，用于调节服务行为。

```json
{
  "type": "STATUS_BROADCAST",
  "target": "system:smart_home",
  "status": {
    "activity": "falling_asleep",
    "confidence": 0.92
  },
  "requested_action": "dim_lights_and_lower_temp",
  "duration_minutes": 480,
  "timestamp": "2026-06-24T23:15:00Z"
}
```

**用途**：告诉智能家居"用户要睡了"。

### 3. 意图传达 (Intent Communication)

替用户主动向外部系统提出需求。

```json
{
  "type": "INTENT_COMMUNICATION",
  "target": "platform:e_commerce",
  "intent": "price_negotiation",
  "item_category": "headphones",
  "user_budget_range": [300, 500],
  "user_decision_factors": ["noise_cancellation", "comfort"],
  "timestamp": "2026-06-24T16:00:00Z"
}
```

**用途**：告诉电商平台"用户在找降噪耳机，预算 300-500"。

### 4. 隐私保护请求 (Privacy Request)

要求平台删除或限制使用用户数据。

```json
{
  "type": "PRIVACY_REQUEST",
  "target": "platform:social_media",
  "request": "DELETE_INFERRED_PROFILE",
  "reason": "user_exercised_right_to_be_forgotten",
  "scope": "all_inferred_attributes",
  "timestamp": "2026-06-24T10:00:00Z"
}
```

---

## 脱敏管道

每种输出类型必须经过对应的脱敏处理：

```
偏好声明：
  原始：用户看了视频 ID=12345，停留 0.8 秒后划走
  脱敏后：用户对 "curiosity_edge" 类别内容感兴趣，置信度 0.87

状态广播：
  原始：用户心率 62，呼吸 14，体动减少
  脱敏后：用户正在入睡，置信度 0.92

意图传达：
  原始：用户浏览了索尼 WH-1000XM5（价格 499）
  脱敏后：用户对降噪耳机感兴趣，预算范围 300-500
```

---

## 输出频率限制

防止代理输出过于频繁导致平台产生负面印象：

| 输出类型 | 频率限制 | 说明 |
|---------|---------|------|
| 偏好声明 | ≤ 10/天/平台 | 避免过度修正 |
| 状态广播 | ≤ 事件驱动 | 仅状态变化时发送 |
| 意图传达 | ≤ 5/天/平台 | 避免被标记为机器人 |
| 隐私请求 | 无限制 | 用户权利 |

---

## 未来期望：平台侧的配合

Symbiote 的代理输出能力依赖于外部平台的配合。我们期望未来出现：

1. **标准化的 AI 代理信号协议** —— 统一的 API 格式
2. **平台对代理信号的尊重** —— 不降权、不惩罚
3. **用户侧 AI 的身份认证** —— 平台知道这是用户授权的 AI 代理，而非恶意机器人
4. **信号的互惠性** —— 平台不仅接收信号，也返回处理结果

这不是技术问题，是权力问题。目前平台有动机自己分析用户行为而不接受外部信号。Symbiote 的立场是：**分析用户意图的权利应该属于用户侧的工具，而不是平台。**
