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
            text = f"<b>Halo {first}, kamu mau <code>Rp. 15.000</code> dana? Caranya gampang, kamu download Neo+ kemudian daftar dengan memasukkan kode undangan <code>JTLB22</code>. Jika sudah buka rekening, tunggu sampai pembukaan rekening sukses. Jika sudah upload buktinya disini dengan format\n<code>FOTO</code>\nNo Pendaftaran :\nNo Dana :\n\nCek secara berkala link File Sharingnya!",
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
