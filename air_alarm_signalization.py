import json
from telethon import TelegramClient, events
from twilio.rest import Client

# Открытие файла с данными для работы
with open("authorization_data.json", "r") as auth_data_file:
    auth_data = json.load(auth_data_file)

# Данные для Telegram
api_id = auth_data["api_id"]
api_hash = auth_data["api_hash"]
session_name = auth_data["session_name"]
# Данные для Twilio
twilio_ssid = auth_data["twilio_ssid"]
twilio_token = auth_data["twilio_token"]
twilio_url = auth_data["twilio_url"]
phone_number = auth_data["phone_number"]
dial_number = auth_data["dial_number"]
chat_name = auth_data["chat_name"]

client = TelegramClient(session_name, api_id, api_hash)
caller = Client(twilio_ssid, twilio_token)


def alarm_signalization(numbers_list):
    for number in numbers_list:
        print(f"Сповіщення: {number}")
        caller.calls.create(to=number, from_=phone_number,
                            url=twilio_url, method="GET")


@client.on(events.NewMessage(chats=chat_name))
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    with open('alarm_log.txt', 'a', encoding='utf8') as outfile:
        outfile.write(user_mess)
    if "Оголошено тривогу" in user_mess:
        alarm_signalization(dial_number)


client.start()
client.run_until_disconnected()
