# app_main.py (или любое другое имя вашего основного файла)

from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

# Определите пути к вашим SSL-файлам
# Рекомендуется использовать абсолютные пути или относительные от места запуска скрипта
# В продакшене лучше не хранить ключи прямо рядом с кодом приложения,
# а указывать пути к безопасным местам (например, /etc/letsencrypt/live/yourdomain.com/)

# Пример для разработки (если ключи лежат в той же папке или в подпапке 'certs')
# Убедитесь, что эти пути правильные для вашей системы!
SSL_KEYFILE_PATH = os.getenv("SSL_KEYFILE", "./certs/privkey.pem")
SSL_CERTFILE_PATH = os.getenv("SSL_CERTFILE", "./certs/fullchain.pem")

# Или, если вы точно знаете пути:
# SSL_KEYFILE_PATH = "/etc/letsencrypt/live/yourdomain.com/privkey.pem"
# SSL_CERTFILE_PATH = "/etc/letsencrypt/live/yourdomain.com/fullchain.pem"

@app.get("/")
async def read_root():
    return {"message": "Hello, secure World from programmatic Uvicorn!"}

@app.post("/telegram_webhook")
async def telegram_webhook():
    # Здесь будет ваша логика обработки вебхука Telegram
    # Например:
    # from aiogram import types
    # update = types.Update(**(await request.json()))
    # await dp.process_update(update)
    return {"status": "ok", "message": "Webhook received"}

# Главная точка входа для запуска Uvicorn
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",  # Слушать на всех доступных интерфейсах
        port=8000,       # Порт, на котором будет работать HTTPS (см. замечания ниже)
        ssl_keyfile=SSL_KEYFILE_PATH,
        ssl_certfile=SSL_CERTFILE_PATH,
        # reload=True,   # Отключите reload в продакшене, но полезно для разработки
        # workers=4,     # Используйте Gunicorn для управления worker'ами в продакшене
                         # или настройте здесь, если не используете Gunicorn
    )