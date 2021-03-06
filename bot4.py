from flask import Flask, request
import telebot
import config

bot = telebot.TeleBot(config.TOKEN4)
bot.set_webhook(url = "http://c34d125cbdd3.ngrok.io")
app = Flask(__name__)


@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "ok"


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello!')


if __name__ == "__main__":
    app.run()

#     python "D:\bot4.py"