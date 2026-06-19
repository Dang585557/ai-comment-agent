# AI-COMPANY

AI-COMPANY is a modular AI automation platform designed to manage multiple AI teams from a single dashboard.

## Features

- CEO Command Center
- AI Manager
- Multi-Agent Architecture
- Telegram Control
- Web Dashboard
- Computer Control
- Mobile Lab
- GitHub Integration
- Multiple LLM Providers
- Workflow Engine
- Monitoring System
- Memory System

---

## Project Structure

```
AI-COMPANY/
ceo/
manager/
dashboard/
agents/
workflows/
llm/
memory/
computer_control/
mobile_lab/
github/
database/
storage/
monitoring/
logs/
configs/
tests/
```
---

## Installation

```bash
git clone https://github.com/your-repository/AI-COMPANY.git
cd AI-COMPANY
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Environment

Create `.env`
```
OPENAI_API_KEY=
GEMINI_API_KEY=
ANTHROPIC_API_KEY=

GITHUB_TOKEN=
GITHUB_REPOSITORY=

TELEGRAM_BOT_TOKEN=
TELEGRAM_OWNER_CHAT_ID=

POSTGRES_PASSWORD=
JWT_SECRET=
```

---

## Run Backend

```bash
uvicorn dashboard.backend.api:app --reload
```

---

## Run Dashboard

```bash
npm install

npm run dev
```

---

## Main Modules

- CEO
- Manager
- Dashboard
- TikTok Team
- Video Team
- Developer Team
- Research Team
- Website Team
- Computer Lab
- Mobile Lab
- GitHub
- Monitoring
- Memory

---

## LLM Providers

- OpenAI
- Gemini
- Claude
- Local Model (Ollama)

---

## Future Modules

- Facebook
- YouTube
- Shopee
- Lazada
- LINE
- Marketing
- Sales
- Accounting
- Customer Service

---

## Version

AI-COMPANY v1.0.0
