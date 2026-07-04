# Home Remedy — AI-Powered Symptom Checker

> **Select your symptoms. Get instant, AI-generated home remedy suggestions — powered by Groq's LLaMA 3.1.**

🤖 Powered by **Groq API + LLaMA 3.1** &nbsp;|&nbsp; 🐍 Built with **Python** &nbsp;|&nbsp; 💻 Runs in your **terminal**

---

## The Problem

When you feel unwell, the first instinct is to Google symptoms — and end up drowning in medical jargon, scary diagnoses, and irrelevant ads. Most people don't need a hospital visit for minor ailments; they need quick, practical, safe home remedy suggestions.

**Home Remedy brings AI directly into your terminal to help with exactly that.**

---

## What It Does

A lightweight command-line tool where you select your symptoms from a menu, and a **large language model (LLaMA 3.1 via Groq API)** instantly recommends safe, practical home remedies tailored to your input — in plain, readable language.

---

## Demo

```
============================================================
        HOME REMEDY — AI Symptom Checker
        Powered by Groq LLaMA 3.1
============================================================

Select your symptoms (enter numbers separated by commas):

 1. Headache          2. Fever             3. Cold & Cough
 4. Sore Throat       5. Stomach Ache      6. Nausea
 7. Fatigue           8. Body Pain         9. Indigestion
10. Skin Irritation

Your selection: 1, 3, 7

Analyzing symptoms: Headache, Cold & Cough, Fatigue...

─────────────────────────────────────────────────────────
AI Recommendation (LLaMA 3.1 via Groq):

Based on your symptoms, here are some safe home remedies:

1. Ginger-honey tea — helps with congestion and fatigue
2. Steam inhalation — relieves nasal blockage and headache
3. Adequate rest and hydration — critical for recovery
4. Tulsi (basil) leaves boiled in water — natural immunity boost
...
─────────────────────────────────────────────────────────

⚠️  For educational use only. Consult a doctor for serious symptoms.
```

---

## Features

| Feature | Description |
|---|---|
| 🧠 LLM-Powered Responses | Uses Groq's ultra-fast LLaMA 3.1 inference for intelligent remedy suggestions |
| 📋 Interactive CLI Menu | Simple numbered symptom selection — no typing, no errors |
| ⚡ Real-time AI Output | Groq's API delivers near-instant responses |
| 🌿 Home Remedy Focused | Responses are practical, safe, and non-alarmist |
| 🛡️ Responsible AI Design | Built-in disclaimer for educational use — promotes safe AI usage |
| 🪶 Lightweight | Pure Python CLI — no frontend, no database, minimal dependencies |

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| AI Model | LLaMA 3.1 (Meta) |
| AI Inference | Groq API (ultra-low latency LLM inference) |
| Interface | Command Line Interface (CLI) |
| Libraries | `groq`, `os`, `sys` |

---

## Why Groq + LLaMA 3.1?

**Groq** provides the fastest LLM inference available — responses in milliseconds vs. seconds with other providers. For a CLI tool where the user is waiting in a terminal, speed is critical to usability.

**LLaMA 3.1** (by Meta) is an open-weight model with strong general knowledge — capable of nuanced, context-aware medical home remedy suggestions without hallucinating dangerous advice.

---

## Project Structure

```
Home_remedy/
│
├── main.py              # Entry point — CLI menu and Groq API integration
├── symptoms.py          # Symptom list and selection logic
├── requirements.txt     # Python dependencies
├── .env.example         # Template for API key setup
└── README.md
```

---

## How to Run

### Prerequisites
- Python 3.8+
- A free Groq API key — get one at [console.groq.com](https://console.groq.com)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Shouryamishra2007/Home_remedy.git
cd Home_remedy

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your Groq API key
# Create a .env file and add:
GROQ_API_KEY=your_api_key_here

# 4. Run the app
python main.py
```

---

## How It Works

```
User selects symptoms
from numbered CLI menu
          │
          ▼
Selected symptoms formatted
into a structured prompt
          │
          ▼
Prompt sent to Groq API
(LLaMA 3.1 model)
          │
          ▼
LLaMA 3.1 generates
tailored home remedy suggestions
          │
          ▼
Response displayed in terminal
with safety disclaimer
```

---

## What I Learned

- **Groq API integration** — how to authenticate, structure prompts, and handle LLM responses in Python
- **Prompt engineering** — crafting system prompts that keep the model focused on safe, practical home remedies
- **Responsible AI design** — building disclaimers and guardrails into AI-powered tools
- **CLI UX design** — making terminal applications intuitive and user-friendly without a frontend
- **Real-world LLM application** — taking an AI API from zero to a working, usable product

---

## Responsible Use Notice

> ⚠️ **This tool is for educational purposes only.**
> Home Remedy is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns. The AI-generated suggestions are general home remedies for minor, common ailments only.

---

## Future Improvements

- [ ] Add voice input for symptom selection
- [ ] Web interface using Flask
- [ ] Multilingual support (Hindi, regional languages)
- [ ] Symptom severity filter (mild / moderate / severe)
- [ ] Integration with nearest clinic finder for serious symptoms
- [ ] Conversation history — multi-turn symptom discussion

---

## Developer

**Shourya Mishra**
BS in Artificial Intelligence & Cybersecurity — IIT Patna (CPI: 9.08/10)

- 🔗 [LinkedIn](https://www.linkedin.com/in/shourya-mishra-25b402370)
- 💻 [GitHub](https://github.com/Shouryamishra2007)
- 📧 mishrashourya224@gmail.com

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with Python · Powered by Groq API + LLaMA 3.1 · For educational use*
