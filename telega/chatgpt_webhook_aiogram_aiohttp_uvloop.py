import asyncio
import uvloop
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.dispatcher.webhook import SendMessage
from starlette.middleware.cors import CORSMiddleware
import uvicorn

  # ---------------------------
# Настройки
# ---------------------------
API_TOKEN = "YOUR_BOT_TOKEN"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://your-domain.com{WEBHOOK_PATH}"
HOST = "0.0.0.0"
PORT = 8000

# ---------------------------
# Хранилище данных в памяти
# ---------------------------
temp_data_store = []  # Список для хранения температурных данных

# ---------------------------
# Создание FastAPI и бота
# ---------------------------
app = FastAPI()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ---------------------------
# Обработчик Telegram команды
# ---------------------------
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Используй /data чтобы получить последние температуры.")

@dp.message(commands=["data"])
async def cmd_data(message: types.Message):
    if temp_data_store:
        latest = temp_data_store[-1]  # Последняя запись
        text = f"Устройство: {latest['device']}, Дата: {latest['date']}, Температуры: {latest['temperature']}"
    else:
        text = "Нет данных."
    await message.answer(text)

# ---------------------------
# Приём данных от клиента
# ---------------------------
@app.post("/temperature")
async def receive_temp_data(request: Request):
    data = await request.json()
    temp_data_store.append(data)
    print("Получены данные:", data)
    return JSONResponse({"status": "ok", "received": data})

# ---------------------------
# Webhook от Telegram
# ---------------------------
@app.post(WEBHOOK_PATH)
async def telegram_webhook(update: dict):
    telegram_update = Update(**update)
    await dp.feed_update(bot, telegram_update)
    return {"status": "ok"}

# ---------------------------
# Запуск
# ---------------------------
if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    import nest_asyncio
    nest_asyncio.apply()

    async def on_startup():
        await bot.set_webhook(WEBHOOK_URL)

    uvicorn.run("main:app", host=HOST, port=PORT, log_level="info")
