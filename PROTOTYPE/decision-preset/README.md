# Decision Preset 原型

> 这是 Symbiote 在未来"工作决策场景"的一个当下可实现版本。
> 它不是等待脑机接口的蓝图，而是你今天就能用的决策辅助工具。

---

## 这是什么

一个轻量的 prompt 预设系统。你描述你的二选一困境，它：
1. 用结构化的 prompt 模板包装你的问题
2. 调用 AI API（OpenAI / Claude / 任何兼容接口）
3. 返回「成功概率 + 关键因素 + 下一步行动」的结构化分析

---

## 快速开始

### 1. 安装依赖

```bash
pip install openai pyyaml
```

### 2. 配置 API Key

复制 `config.example.yaml` 为 `config.yaml`：

```yaml
llm:
  provider: "openai"          # openai | anthropic | local
  api_key: "${OPENAI_API_KEY}" # 或直接填
  model: "gpt-4o-mini"
  temperature: 0.3

output:
  language: "zh"              # zh | en
  show_confidence: true
  show_next_step: true
```

### 3. 使用

```bash
# 交互式
python decide.py

# 命令行直接输入
python decide.py "我在纠结要不要跳槽去创业公司 vs 留在大厂"

# 从文件读取
python decide.py --file my_decision.txt
```

---

## Prompt 模板

模板在 `prompt-templates/` 目录下：

| 模板 | 用途 |
|------|------|
| `binary-choice.md` | 二选一决策 |
| `multi-option.md` | 多选项比较 |
| `risk-assessment.md` | 单选项风险评估 |

---

## 更多

→ 见 [PROTOTYPE README](../PROTOTYPE/README.md)
