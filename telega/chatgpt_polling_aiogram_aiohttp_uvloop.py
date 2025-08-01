import asyncio
import uvloop
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiogram.utils.executor import start_polling
import nest_asyncio

# ---------------------------
# Настройки
# ---------------------------
API_TOKEN = "YOUR_BOT_TOKEN"
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
dp = Dispatcher(bot)

# ---------------------------
# Обработчик Telegram команды
# ---------------------------
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Используй /data чтобы получить последние температуры.")

@dp.message_handler(commands=["data"])
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
# Запуск
# ---------------------------
if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    nest_asyncio.apply()

    from threading import Thread
    import uvicorn

    def start_fastapi():
        uvicorn.run(app, host=HOST, port=PORT, log_level="info")

    # Запуск FastAPI в отдельном потоке
    Thread(target=start_fastapi).start()

    # Запуск Telegram-бота в режиме Polling
    start_polling(dp, skip_updates=True)
