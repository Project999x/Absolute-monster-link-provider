# +++ Modified By Yato [telegram username: @i_killed_my_clan & @ProYato] +++ # aNDI BANDI SANDI JISNE BHI CREDIT HATAYA USKI BANDI RAndi 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8311348398:AAGy02UrCSC7eFRTt1lVg0yvuvIxWi7u0Pc")
APP_ID = int(os.environ.get("APP_ID", "19822764"))
API_HASH = os.environ.get("API_HASH", "b240e413364b8608a542a7cafc6903be")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "1418213560"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kaido0099878:XR5TnmaT55neAJ2U@cluster0.ksifz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Absolute_Monster_bot")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Shirohige_Animes_Academy</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://files.catbox.moe/117uzx.jpg"
START_IMG = "https://files.catbox.moe/g5gc0j.jpg"
# Messages
START_MSG = """<b>›› ʜᴇʏ!!, {mention} ~\n\n<blockquote expandable>ʟᴏᴠᴇ ᴛᴏ ᴡᴀᴛᴄʜ ᴀɴɪᴍᴇ sᴇʀɪᴇs ᴀɴᴅ ᴍᴏᴠɪᴇs? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>"""
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/WhiteBeard_Sama>ᴡʜɪᴛᴇ ʙᴇᴀʀᴅ ꜱᴀᴍᴀ</a>\n» Anime Channel: <a href=https://t.me/Shirohige_Animes_Academy>Animes</a>\n» 𝐇ᴇɴᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ: <a href=https://t.me/Dsh_Alliance>𝐇ᴇɴᴛᴀɪ</a>\n» ᴏᴡɴᴇʀ: <a href=https://t.me/WhiteBeard_sama>ᴡʜɪᴛᴇ ʙᴇᴀʀᴅ ꜱᴀᴍᴀ</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed for to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {ᴀʙꜱᴏʟᴜᴛᴇ ᴍᴏɴꜱᴛᴇʀ}
<blockquote><b>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Whitebeard_sama>ᴡʜɪᴛᴇ ʙᴇᴀʀᴅ ꜱᴀᴍᴀ</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Shirohige_Animes_Academy>ᴀɴɪᴍᴇ</a>\n» 𝐇ᴇɴᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ : <a href=https://t.me/Dsh_Alliance>𝐇ᴇɴᴛᴀɪ</a>\n» sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : <a href=https://t.me/+2yT168VxMrBiNTc1>𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ</a>\n» ᴏᴡɴᴇʀ : <a href=https://t.me/WhiteBeard_Sama>ᴡʜɪᴛᴇ ʙᴇᴀʀᴅ ꜱᴀᴍᴀ</a></blockquote></b>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Shirohige_Animes_Academy'> Animes</a>
<blockquote expandable>›› 𝐇ᴇɴᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ: <a href='https://t.me/Dsh_Alliance'>𝐇ᴇɴᴛᴀɪ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/Shirohige_Hindi_Toonz'>ᴡᴇʙsᴇʀɪᴇs</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/WhiteBeard_sama'>ᴡʜɪᴛᴇ ʙᴇᴀʀᴅ ꜱᴀᴍᴀ</a>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1001985214229")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "7149088701").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
