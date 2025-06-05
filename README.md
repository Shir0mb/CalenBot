# Telegram Calendar Bot 📅

A simple Telegram bot that lets you create and view calendar events in a chat.  
Ideal for use with a friend or group to keep track of upcoming activities.

## Features

- Create an event with a name, date, and time  
- View all upcoming events  
- Simple file-based storage (JSON)  
- Easy to deploy on free hosting platforms like Railway or Render  

## Commands

```
/crea_evento EventName yyyy-mm-dd hh:mm
```
Creates a new event.  
Example: `/crea_evento Meeting 2025-06-15 14:30`

```
/mostra_eventi
```
Displays a list of all saved events.

## Project Structure

```
.
├── bot.py               # Main bot script
├── events.json          # JSON file to store events (optional, auto-created)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Requirements

- Python 3.10+  
- A Telegram bot token from [@BotFather](https://t.me/BotFather)  

Install dependencies locally with:

```bash
pip install -r requirements.txt
```

## Deployment (e.g. Railway)

1. Create an account on [Railway](https://railway.app)  
2. Link this GitHub repository  
3. Set the environment variable:  
   `BOT_TOKEN=your-telegram-bot-token`  
4. Deploy and your bot will run online 24/7!

## Notes

- Events are stored in a local JSON file (`events.json`).  
- For long-term hosting on platforms where the filesystem is ephemeral, consider switching to a database like SQLite or PostgreSQL.

## License

MIT License — free to use and modify.
