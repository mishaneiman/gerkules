from pyrogram import Client, Filters, Message, InlineQuery, CallbackQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from databases.food_database import gerkules_food_db
from databases.user_database import gerkules_user_db


@Client.on_callback_query(Filters.regex("Input meal"))
def input_meal_begin(client: Client, callback_query: CallbackQuery):
    print(f"{callback_query.from_user.username} is inputting a meal.")
    client.send_message(callback_query.from_user.username, "What did you eat?")
    callback_query.continue_propagation()


@Client.on_message(Filters.text)
def input_meal(client: Client, message: Message):
    gerkules_food_db.cursor.execute(f"SELECT * FROM food WHERE food_name='{message.from_user.username}'")
    message.continue_propagation()
    if not gerkules_food_db.cursor.fetchall():
        @Client.on_message(Filters.text)
        def
        gerkules_food_db.cursor.execute("INSERT INTO food (food_name, cal_per_100g) values (?, ?, ?)",
                                        (message.from_user.username, 0, -1))
        gerkules_food_db.conn.commit()
        print(f"New user {message.from_user.username} added.")
    else:
        print(f"{message.from_user.username} hit 'start' again.")


