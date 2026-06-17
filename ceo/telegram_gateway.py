"""
AI-COMPANY
ceo/telegram_gateway.py

Telegram Gateway
"""

import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from ceo.command_center import CommandCenter


class TelegramGateway:

    def __init__(self):

        self.token = os.getenv("TELEGRAM_BOT_TOKEN")

        self.command_center = CommandCenter()

        self.application = Application.builder().token(self.token).build()

        self.register_handlers()

    def register_handlers(self):

        self.application.add_handler(

            CommandHandler("start", self.start)

        )

        self.application.add_handler(

            CommandHandler("status", self.status)

        )

        self.application.add_handler(

            CommandHandler("report", self.report)

        )

        self.application.add_handler(

            MessageHandler(

                filters.TEXT & ~filters.COMMAND,

                self.receive_command

            )

        )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        await update.message.reply_text(

            "✅ AI-COMPANY Online\n\n"

            "ส่งคำสั่งมาได้เลย"

        )

    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        status = self.command_center.system_status()

        await update.message.reply_text(str(status))

    async def report(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        report = self.command_center.daily_report()

        await update.message.reply_text(str(report))

    async def receive_command(

        self,

        update: Update,

        context: ContextTypes.DEFAULT_TYPE

    ):

        command = update.message.text

        self.command_center.execute(command)

        await update.message.reply_text(

            "✅ รับคำสั่งแล้ว\n"

            f"คำสั่ง: {command}"

        )

    def run(self):

        print("[TELEGRAM] Bot Started")

        self.application.run_polling()


if __name__ == "__main__":

    gateway = TelegramGateway()

    gateway.run()
