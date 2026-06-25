#!/usr/bin/env python3
"""
Symbiote Decision Preset — 二选一决策助手原型

这是 Symbiote 项目「工作决策场景」的当下可实现版本。
在脑机接口成熟之前，先用文字界面模拟 AI 共生体的决策辅助能力。

用法:
    python decide.py
    python decide.py "我在纠结要不要跳槽"
    python decide.py --file my_decision.txt
"""

import os
import sys
import argparse
import yaml

try:
    from openai import OpenAI
except ImportError:
    print("请先安装 openai: pip install openai pyyaml")
    sys.exit(1)


def load_config(config_path: str = "config.yaml") -> dict:
    """加载配置文件，支持环境变量替换"""
    if not os.path.exists(config_path):
        # 生成默认配置
        default_config = {
            "llm": {
                "provider": "openai",
                "api_key": "${OPENAI_API_KEY}",
                "model": "gpt-4o-mini",
                "temperature": 0.3,
            },
            "output": {
                "language": "zh",
                "show_confidence": True,
                "show_next_step": True,
            },
        }
        print(f"配置文件 {config_path} 不存在，已创建默认配置。请编辑后重试。")
        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(default_config, f, allow_unicode=True)
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # 替换环境变量
    api_key = config["llm"]["api_key"]
    if api_key.startswith("${") and api_key.endswith("}"):
        env_var = api_key[2:-1]
        config["llm"]["api_key"] = os.environ.get(env_var, "")

    return config


def load_system_prompt(template_name: str = "binary-choice") -> str:
    """加载 prompt 模板"""
    template_dir = os.path.join(os.path.dirname(__file__), "prompt-templates")
    template_path = os.path.join(template_dir, f"{template_name}.md")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"模板不存在: {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def build_user_prompt(
    raw_input: str, language: str = "zh"
) -> str:
    """将用户的原始输入包装为结构化的用户 prompt"""

    wrapper_zh = f"""## 用户面临的选择

{raw_input}

---

请按系统角色中指定的格式，对以上两个选项进行分析。

如果用户没有明确给出两个选项，从描述中推断出最可能的两个选项并命名。
如果用户只给了一个选项，假设对比选项是"维持现状"。"""

    wrapper_en = f"""## Decision to Analyze

{raw_input}

---

Please analyze the two options above using the format specified in your system role.

If the user hasn't clearly named two options, infer the two most likely ones and name them.
If only one option is given, assume the alternative is "maintain the status quo"."""

    return wrapper_zh if language == "zh" else wrapper_en


def analyze(client: OpenAI, model: str, system_prompt: str, user_prompt: str, temperature: float) -> str:
    """调用 LLM 进行分析"""
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(
        description="Symbiote 二选一决策助手",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python decide.py
  python decide.py "我在纠结要不要跳槽去创业公司 vs 留在大厂"
  python decide.py --file my_decision.txt
  python decide.py --template risk-assessment "这个投资靠谱吗"
        """,
    )
    parser.add_argument(
        "decision", nargs="?", default=None,
        help="你的决策困境描述"
    )
    parser.add_argument(
        "--file", "-f", default=None,
        help="从文件读取决策描述"
    )
    parser.add_argument(
        "--config", "-c", default="config.yaml",
        help="配置文件路径（默认 config.yaml）"
    )
    parser.add_argument(
        "--template", "-t", default="binary-choice",
        help="Prompt 模板名（默认 binary-choice）"
    )
    args = parser.parse_args()

    # 获取用户输入
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            user_input = f.read().strip()
    elif args.decision:
        user_input = args.decision
    else:
        print("=" * 50)
        print("  Symbiote 决策助手 — 原型 v0.1")
        print("=" * 50)
        print()
        print("描述你正在纠结的选择（例如：")
        print('  "我在纠结要不要跳槽去创业公司 vs 留在大厂"')
        print()
        user_input = input("> ").strip()

    if not user_input:
        print("没有收到输入，退出。")
        sys.exit(0)

    # 加载配置
    config = load_config(args.config)
    llm_config = config["llm"]
    output_config = config["output"]

    # 检查 API Key
    api_key = llm_config["api_key"]
    if not api_key:
        print("错误: 未设置 API Key。请在 config.yaml 中设置或设置环境变量。")
        sys.exit(1)

    # 加载 prompt 模板
    system_prompt = load_system_prompt(args.template)

    # 构建用户 prompt
    user_prompt = build_user_prompt(user_input, output_config.get("language", "zh"))

    # 调用 LLM
    print()
    print("正在分析...")
    print()

    client = OpenAI(api_key=api_key)
    try:
        result = analyze(
            client,
            llm_config["model"],
            system_prompt,
            user_prompt,
            llm_config.get("temperature", 0.3),
        )
        print(result)
    except Exception as e:
        print(f"分析出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
