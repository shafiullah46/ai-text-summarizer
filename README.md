# ⚡ AI Text Summarizer Utility

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

An intelligent, Python-based text summarization microservice designed to transform lengthy developer issue reports, logs, or complex technical text into precise, one-line actionable summaries using OpenAI's API.

---

## 🚀 Key Features

- **Single-Line Formatting:** Uses parameterized prompt engineering to force concise outputs under 80 tokens.
- **Balanced Temperature Scaling:** Configured at `temperature=0.5` to balance semantic accuracy with natural phrasing.
- **Robust Exception Handling:** Features multi-layer dynamic parsing to support standard OpenAI response objects alongside custom test environments.
- **Environment-Driven Configuration:** Loads API credentials securely via system environment variables (`OPENAI_API_KEY`, `OPENAI_API_BASE`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **SDK:** `openai` (Official Python Library)
- **Environment:** Virtualenv (`venv`)

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/shafiullah46/ai-text-summarizer.git](https://github.com/shafiullah46/ai-text-summarizer.git)
cd ai-text-summarizer

2. Virtual Environment Setup
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

3. Install Dependencies
pip install openai

4. Set Environment Variables & Run
# On Windows PowerShell:
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_API_BASE="your_base_url_here"

# Run the summarizer script
python summarizer.py

💻 Sample Execution
Input Paragraph:

Artificial Intelligence enables machines to mimic human intelligence, performing tasks such as learning, problem-solving, and decision-making with increasing accuracy.

Generated One-Line Summary:

AI empowers machines to simulate human cognitive functions like learning and decision-making accurately.

👨‍💻 Author
Shafiullah Niazi

Deputy Director ML/DevOps | Cloud & AI Infrastructure Specialist
