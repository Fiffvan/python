from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Url
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import setup_dialogs

BOT_TOKEN = '7157534842:AAGuExWpdrTvidFSCi17FIFxOlnTwaHns'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class MySG(StatesGroup):
    start = State()
    next = State()

async def go_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.message.answer("Поехали!")


dialog = Dialog(
        Window(
            Const("Привет!"),
            Button(
                Const("Поехали"),
                id="go",  # id используется для определения нажатой кнопки
                on_click=go_clicked,
                ),
            Url(
                Const("Github"),
                Const('https://github.com/Tishka17/aiogram_dialog/'),
                ),

            state=MySG.start,
        ),
)

dp.include_router(dialog)

@dp.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    # Важно: всегда устанавливайте `mode=StartMode.RESET_STACK`, чтобы не накапливать диалоги
    await dialog_manager.start(MySG.start, mode=StartMode.RESET_STACK)

setup_dialogs(dp)

if __name__ == '__main__':
    dp.run_polling(bot)