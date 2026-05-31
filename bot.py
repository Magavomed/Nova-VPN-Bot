from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "🎉 <b>Добро пожаловать в Nova VPN!</b>\n\n"
        "Это твой надёжный помощник для обхода блокировок.",
        parse_mode="HTML",
        reply_markup=get_main_menu()
    )

def get_main_menu():
    kb = [
        [types.InlineKeyboardButton(text="🚀 Активировать VPN", callback_data="activate")],
        [types.InlineKeyboardButton(text="👤 Мой Аккаунт", callback_data="account")],
        [types.InlineKeyboardButton(text="ℹ️ О Nova VPN", callback_data="about")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)

@dp.callback_query(F.data == "activate")
async def activate(callback: types.CallbackQuery):
    await callback.message.answer("✅ VPN активирован! (пока тестовый режим)")

@dp.callback_query(F.data.in_(["account", "about"]))
async def other_buttons(callback: types.CallbackQuery):
    await callback.message.answer("Эта функция пока в разработке...")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
