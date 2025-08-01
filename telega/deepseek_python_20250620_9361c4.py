from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

bot = Bot(token="TOKEN")
dp = Dispatcher()

@dp.message()
async echo(message: types.Message):
    await message.answer("Привет!")

async def on_startup(bot: Bot):
    await bot.set_webhook(
        url="https://yourdomain.com/bot",
        certificate=types.FSInputFile("/path/to/cert.pem")  # если нужен сертификат
    )

app = web.Application()
webhook_handler = SimpleRequestHandler(dp, bot)
webhook_handler.register(app, path="/bot")

setup_application(app, dp, bot=bot)

if __name__ == "__main__":
    dp.startup.register(on_startup)
    web.run_app(app, host="0.0.0.0", port=8443)