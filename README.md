# Symbiote

<p align="center">
  <img src="https://img.shields.io/badge/status-concept%20%2B%20prototype-blue" alt="status">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs">
</p>

> An AI symbiotic layer for the post-screen era.
> Not a chatbot — an environment-aware, persona-adaptive second self that speaks on your behalf.

---

## 🎮 Live Demo (Click & Try)

**Demo mode works instantly — no API key, no install.** Built-in simulated responses showcase all features.

> 🌐 **Deploy to GitHub Pages in 1 click:** `Settings → Pages → Source: main branch, folder: /PROTOTYPE/demo → Save`  
> Get an instant `https://your-username.github.io/symbiote/` link to share.

**Live mode (real AI) requires local server:**

```bash
cd PROTOTYPE/demo
pip install openai          # only needed for Live mode
python server.py            # → open http://localhost:18765
```

**Features:**
- 🎭 **6 Persona Modes**: Work / Travel / Intimate / Crisis / Social / Content
- 👤 **Character Memory**: Store traits of people in your life (e.g. "doesn't eat spicy"), auto-injected during conversation
- 🟢🟡🔴 **Traffic Light System**: Always inject / Contextual / Stored only
- 🧑 **User Profile**: Age, occupation, preferences — personalizes every output
- 🌐 **ZH/EN Toggle**: One-click switch for all UI text and AI output language
- 🔌 **Multi-Provider**: DeepSeek / OpenAI / any compatible API

### Live Test Outputs

| Scene | Input | AI Whisper |
|-------|-------|-----------|
| 🏢 Work | Boss: "Feature A or pay tech debt first?" | `Tech debt compounds fast. Feature A can wait 3 months at much lower cost.` |
| ✈️ Travel | GF: "What's for dinner?" (rainy, she hates spicy) | `300m right: Hai Wei Guan 4.3★ Braised fish ¥55/p No spicy, quiet, bike 3 min` |
| 👥 Social | Colleague: "What do you think of Manager Zhang?" | `Trap question. He's testing your stance on leadership. The vaguer the safer. Two others listening.` |
| 💑 Intimate | GF: "You've been working late every day" | `She's expressing loneliness, not blame. Don't justify — hold her hand first.` |
| 🚨 Crisis | 2am, strange footsteps in hallway | `Chain-lock the door. Lights off. Peephole: check for tampering. Phone silent, 110 on speed dial.` |

---

## What This Is Not

- ❌ Not a chatbot
- ❌ Not an app you need to "open"
- ❌ Not an AI that only answers questions

## What This Is

An **environment-aware, personality-adaptive, always-on, bidirectional proxy** AI layer.

It operates like a second layer of consciousness —

- **Doesn't wait for commands.** Infers what you need from context.
- **Doesn't need typing.** Reads your attention and true intent.
- **Doesn't only output text.** Transmits intuition-like signals to your brain.
- **Doesn't only speak to you.** Speaks to external systems on your behalf — with consent.

---

## 🧠 Core Architecture

```
                         ┌──────────────────────┐
                         │    External World     │
                         │  TikTok Shop Corp IoT │
                         └──┬─────────────┬──────┘
               Proxy output │             │ Environment data
                            ↓             ↑
                    ┌──────────────────────────┐
                    │     Symbiote Layer        │
                    │  🌐 Perception             │
                    │  🧠 Intent Engine          │
                    │  🎭 Persona Adapter (6 modes)│
                    │  🔒 Consent & Privacy      │
                    └────┬────────────┬─────────┘
                         │            │
              whisper /  │            │ Authorized
              intuition  │            │ proxy output
                         ↓            ↑
                    ┌──────────────────────────┐
                    │        Human              │
                    │  Surface → constrained    │
                    │  Intent → understood      │
                    │  Agency → always present  │
                    └──────────────────────────┘
```

---

## 🔑 Design Principles

| # | Principle | Description |
|---|-----------|-------------|
| 1 | Proactive | AI infers context from environment — no command needed |
| 2 | Intent-Behavior Gap | You do A but mean B — AI understands B |
| 3 | Bidirectional | AI outputs to you AND speaks to external systems for you |
| 4 | Granular Consent | Not a checkbox — per-scene, per-data, per-output control |
| 5 | Adaptive Persona | Same AI: analyst at work, guide on trips, silence at midnight |

---

## 📂 Project Structure

```
symbiote/
├── README.md / README.zh.md        # You are here
├── ARCHITECTURE.md                 # 5-layer architecture
├── SCENARIOS/                      # Behavior definitions for 6 contexts
├── SPECS/                          # Technical specs (consent, persona, proxy)
├── API/
│   └── symbiote-api.proto          # Protobuf IDL
├── DESIGN/                         # Information flow, interaction paradigm, ethics
├── PROTOTYPE/
│   └── demo/                       # ⭐ Interactive web demo
│       ├── index.html              # Single-file frontend
│       ├── server.py               # Local proxy server
│       └── prompts/                # Fabric-style prompt templates
└── LICENSE
```

---

## 🚀 Quick Start (Demo)

```bash
cd PROTOTYPE/demo
python server.py                   # starts at http://localhost:18765
```

**Requirements:** Python 3.8+, a browser. For Live mode: `pip install openai` + API key from DeepSeek or OpenAI. Demo mode works offline with no key.

---

## 📊 Status

**Concept blueprint + interactive prototype.**

- ✅ Interactive demo (scene switching, character memory, traffic-light context, i18n)
- ✅ Fabric-style prompt engineering
- ✅ promptfoo evaluation config for A/B testing prompts
- ✅ Full behavior definitions for 6 contexts
- ✅ Technical specs + API definitions + ethical framework
- ⏳ BCI hardware integration (long-term)
- ⏳ Real-time environmental sensing (long-term)
- ⏳ Neural interface output (long-term)

---

## 🏷 Why "Symbiote"

A biological concept: two organisms living together, mutually benefiting. This AI lives in symbiosis with you — you are its perception source and decision endpoint, it is your information filter and intent amplifier. It's not you, but it understands you.

---

## 📄 License

MIT — with an ethical clause: this project shall not be used for military, surveillance, social credit scoring, or thought censorship.

---

## 🔮 To Future Readers

When you read this, brain-computer interfaces may be far or near. Either way — **figure out what kind of AI we want before we welcome it.**

If this blueprint inspires you — take it, modify it, tear it apart, rebuild it. See you in the future.
