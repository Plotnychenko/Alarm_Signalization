Python 3.9

Використовуються API Telegram та API Twilio.
Для роботи API Telegram необхідні дані (https://tlgrm.ru/docs/api/obtaining_api_id).
api_id - присвоюється після реєстрації на сайті https://my.telegram.org/auth?to=apps відподвідно до документації Telegram.
api_hash - присвоюється після реєстрації на сайті https://my.telegram.org/auth?to=apps відподвідно до документації Telegram.
session_name - будь-яке ім'я для сессії.
chat_name - назва чату з якого необхідно відстежувати повідомлення.
  
Для роботи API Twilio необхідні дані:
twilio_ssid - присвоюється після реєстрації на сайті https://console.twilio.com/.
twilio_token - присвоюється після реєстрації на сайті https://console.twilio.com/.
twilio_url - після реєстрації на сайті https://console.twilio.com/ необхідно перейти до налаштувань, виставити у випадаючому меню метод GET, скопіювати url и вставити у відповідне місце в коді.
phone_number - номер телефону З ЯКОГО будуть виконуватись дзвінки. Можна використати той, на який реєструвався аккаунт в Twilio, а можна той, який вони надають.
dial_number - номери телефонів, на які будуть виконуватись дзвінки. Можна передати списком/кортежем.

Функція normal_handler під час роботи сессії в реальному часі відстежує нові повідомлення в чаті. Всі повідомлення цього чату потрапляють у файл. У випадку, якщо повідомлення містить слова "Оголошено тривогу" викликається функція alarm_signalization, яка просто проходить по всім номерам списку і використовує до них метод Twilio calls.create.

# МОЖЛИВІ ПОМИЛКИ API Twilio
1.
_Unable to create record: The number +380xxxxxxxxx unverified. Trial accounts may only make calls to verified numbers._ 
  Для того, щоб все працювало в пробній версії Twilio необхідно верифікувати номери телефонів, на які необхідно здійснювати дзінки. Для цього необхідно в Twilio Console перейти до Phone numbers -> Manage -> Verified Caller IDs і в правому верхньому куті натиснути Add a new caller ID. У вікні, яке з'явиться, необхідно вписати номер телефону БЕЗ +380 (тобто для номеру +380990123456 необхідно ввести лише 0123456) і вписати код із повідомлення, яке прийде на вказаний номер.
2.
_Unable to create record: Account not authorized to call +380xxxxxxxxx. Perhaps you need to enable some international permissions_
Щоб виправити цю помилку, необхідно в Twilio Console перейти Voice -> Settings -> Geo permissions і поставити галочку навпроти Ukraine. Після цього натиснути Save знизу.
