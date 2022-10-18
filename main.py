from entry import dp

from aiogram import executor
from mainn import bot
bot.reg_handlers(dp)


async def start(_):
    print("I will Help! /.................")


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=start)


if __name__ == "__main__":
    main()
