from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
from datetime import datetime

EVENTS_FILE = "events.json"

# Load events
def load_events():
    try:
        with open(EVENTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save events
def save_events(events):
    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=2)

# /crea_evento command
async def crea_evento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Usa: /crea_evento nome yyyy-mm-dd hh:mm")
        return

    nome = args[0]
    data_str = f"{args[1]} {args[2]}"
    try:
        data = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    except ValueError:
        await update.message.reply_text("Formato data/ora non valido. Usa yyyy-mm-dd hh:mm")
        return

    eventi = load_events()
    eventi.append({"nome": nome, "data": data_str})
    save_events(eventi)

    await update.message.reply_text(f"Evento '{nome}' creato per il {data_str}")

# /mostra_eventi command
async def mostra_eventi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    eventi = load_events()
    if not eventi:
        await update.message.reply_text("Nessun evento trovato.")
        return

    risposta = "📅 Eventi:\n"
    for e in eventi:
        risposta += f"- {e['nome']} il {e['data']}\n"

    await update.message.reply_text(risposta)

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token("7907510128:AAHDM8Kxz6DFPOPOlowZTodWyvjDA_1gMXU").build()

    app.add_handler(CommandHandler("crea_evento", crea_evento))
    app.add_handler(CommandHandler("mostra_eventi", mostra_eventi))

    print("Bot in esecuzione...")
    app.run_polling()
