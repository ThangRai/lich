from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from lunarcalendar import Converter, Solar

from datetime import date

async def am_lich(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = date.today()
    solar = Solar(today.year, today.month, today.day)
    lunar = Converter.Solar2Lunar(solar)

    reply = f"Hôm nay dương lịch: {today.strftime('%d/%m/%Y')}\n" \
            f"Lịch âm: Ngày {lunar.day} tháng {lunar.month}" \
            f"{' (nhuận)' if lunar.isleap else ''} năm {lunar.year}"

    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token("6608663537:AAEYd275xo-mwlCKTlkVMSl2fgTNMFFD4CA").build()

    app.add_handler(CommandHandler("licham", am_lich))

    print("Bot đang chạy...")
    app.run_polling()
