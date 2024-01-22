import time

from pyrogram import Client

api_hash = "8da85b0d5bfe62527e5b244c209159c3"
api_id = "2496"

async def create_telegram_session(api_id, api_hash, phone_number):
    async with Client(str(time.time()), api_id, api_hash) as app:
        # Попытка входа существующего пользователя
        try:
            await app.connect()
            sent_code_info = await app.send_code(phone_number)
            phone_code = input("Please enter your phone code: ")  # Sent phone code using last function
            await app.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)
        except Exception as e:
            print(f"Error: {e}")
            print("Creating a new session...")
            # Если не удалось войти, создаем новую сессию
            await app.send_code(phone_number)
            code = input("Введите код подтверждения: ")
            await app.sign_in(phone_number, code=code)

        # Вывод информации о текущем пользователе
        me = await app.get_me()
        print(f"Logged in as: {me.first_name} {me.last_name} (@{me.username})")


if __name__ == "__main__":
    phone_number = input("Введите номер телефона (в формате +1234567890): ")

    # Запуск скрипта
    import asyncio

    asyncio.run(create_telegram_session(api_id, api_hash, phone_number))
