# https://t.me/ultroid_official



import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "21606847"))
API_HASH = os.environ.get("API_HASH", "b9708b698eed88f053454aed2598e571")


OWNER = os.environ.get("OWNER", "WOLVERIN_P") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1383239349")) #Owner user id
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://fiwavew866:InNfBs6moAkaYeyt@cluster0.7jgv8.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluserhh")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001866287032")) #database save channel id 
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001909796512"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com") 
SHORTLINK_API = os.environ.get("SHORTLINK_API", "8960075d61d126996682b45d5d8b4503a8d5e717")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/HTDTeraBox/6")

# ignore this one
SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link. Owner @NeonGhost_Networks \n\n Join For Newly Release MOvies @new_movies_2024_hindi")

try:
    ADMINS=[6020516635]
    for x in (os.environ.get("ADMINS", "1383239349").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my all Channel/Group to use me\n\nKindly Please join Channel</b>\n After Joining All channels Please click on Try Again ")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "@NeonGhost_Network") # remove None and fo this ->: "here come your txt" also with this " " 

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(1383239349)

LOG_FILE_NAME = "uxblogs.txt"

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
   





# https://t.me/ultroid_official
