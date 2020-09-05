from pyrogram import Client, Filters, Message, InlineKeyboardMarkup, InlineKeyboardButton
from databases.user_database import gerkules_user_db


@Client.on_message(Filters.command(["start"]))
# Adds user to database unless he's already in it.
def start(client: Client, message: Message):
    gerkules_user_db.cursor.execute(f"SELECT * FROM users WHERE username= '{message.from_user.username}'")
    if not gerkules_user_db.cursor.fetchall():
        gerkules_user_db.cursor.execute("INSERT INTO users (username, stage, quota) values (?, ?, ?)",
                                        (message.from_user.username, 0, -1))
        gerkules_user_db.conn.commit()
        print(f"New user {message.from_user.username} added.")
    else:
        print(f"{message.from_user.username} hit 'start' again.")
        message.continue_propagation()
# Prompts the user to set his calorie plan.
    client.send_message(message.from_user.username, f'Welcome, {message.from_user.username}!\n'
                                                    f'My name is Gerkules. I can count your daily calorie intake!\n'
                                                    f'What would you like to do?',
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("Set plan", callback_data="Set plan"),
                                    InlineKeyboardButton("Help", callback_data="Help")
                                ]
                            ]
                        )
                        )
    message.continue_propagation()
