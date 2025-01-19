# (c) @X_XF8 || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "19193584"))
	API_HASH = os.environ.get("API_HASH", "6cce5fd44ffbeba47414ca91143dc8c2")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002229217917"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "0")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "0")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "6169288210"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","-1001534150170")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL","-1002229217917")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "6169288210").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent Netflix For Movies. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [Netflix For Movies](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [𝑫𝑬𝑽𝑳𝑶𝑷𝑬𝑹](https://t.me/X_XF8) 
│
├🔹 **Bot Support:** [طلبات VIP](https://t.me/+8X3SYWdWdq9lODY8)
│
├🔸 **Bot Updates:** [Netflix For Movies](https://t.me/MOVIES4ARAB)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@X_XF8](https://t.me/X_XF8)
 
 I am Super noob Please Support My Hard Work.


"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **Netflix For Movies**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
