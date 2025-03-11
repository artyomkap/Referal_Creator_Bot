# Referal_Creator_Bot
This is a web application Telegram bot project based on AIOgram 3 and SQLAlchemy and MariaDB.
This project also contain code for menus autogeneration where it is used for drawing. 

This project is made for creating referal link(promocode) with different setting based on websites and other solutions. All website settings are hardcoded, because were used as examples.
Every promocode has it is own type and different type of settings as it is said above.

In order to launch project you need:
1. Python 3.12 and earlier.
2. pip install -r requirements.txt
3. create MySQL connection and change in the .env fil or create *.db file and change connection type in .env as well.
4. create BotToken in @BotFather and change it in the .env file.
5. Create webhook using NGROK or xTunnel (up to you)
6. change webhook url in config.py file, also change port if you use different ports for webhook.
