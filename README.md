# Cybersecurity Knowledge Telegram Bot

Telegram bot that provides structured cybersecurity knowledge using a CSV-based dataset, OpenAI for reasoning and explanation, and Supabase as a backend service.

The bot responds in a **Rick Sanchez–inspired tone** (sarcastic, confident, scientific), while maintaining technically accurate and professional cybersecurity content.

---

## Features

- CSV-based cybersecurity knowledge base
- Natural language responses via OpenAI
- Supabase backend integration
- Telegram bot interface
- Environment-based configuration using `.env`
- Rick-style response tone (affects tone only, not correctness)

---

## Technology Stack

- Python 3.10+
- python-telegram-bot
- OpenAI API
- Supabase
- python-dotenv
- CSV

---

## Project Structure

```text
.
├── bot.py
├── handlers/
│ └── query_handler.py
├── services/
│ ├── openai_service.py
│ └── supabase_service.py
├── data/
│ └── cybersecurity.csv
├── .env.example
├── requirements.txt
└── README.md