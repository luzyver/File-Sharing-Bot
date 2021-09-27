#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Hai {first}, anda beneran mau Rp. 15.000 dana?\ncaranya gampang,\n1. cukup download Neo+ di Play Store atau bisa melalui link https://s.bankneo.co.id/HJq700\n2. kemudian daftar masukkan kode reff : JTLB22\n3. buka rekening (menggunakan KTP dan Verif Wajah)\n4. tunggu sampai rekening terbuka\n5. jika sudah kirim buktinya ke Contact Admin",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
