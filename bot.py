import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Charger le token depuis le fichier .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Fonction pour la commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Salut ! Je suis Campus IA, ton assistant pour la fac. Pose-moi une question !"
    )

# Fonction pour répondre aux messages texte
async def repondre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_utilisateur = update.message.text
    # Pour l'instant, on répond juste un écho
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"J'ai bien reçu ton message : '{message_utilisateur}'. Mon cerveau IA arrive bientôt !"
    )

if __name__ == '__main__':
    print("Démarrage du bot...")
    # Créer l'application
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajouter les gestionnaires
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, repondre))

    print("Bot en ligne ! Appuie sur Ctrl+C pour arrêter.")
    # Lancer le bot
    application.run_polling()
