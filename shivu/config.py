 class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6675050163"
    sudo_users = "6675050163", "6087651372","7640076990","1420481421","6645960688"
    GROUP_ID = -1002499806698
    TOKEN = "7583740884:AAHNM9iVB-bWa3T4USseHrTavjBV8P6lAag"
    mongo_url = "mongodb+srv://sunnymuduli584:<db_password>@sunny.s9g6h.mongodb.net/"
    PHOTO_URL = ["https://i.ibb.co/Z63d8xB1/photo-2025-03-21-05-25-47.jpg"]
    SUPPORT_CHAT = "Anime_Circle_Club"
    UPDATE_CHAT = "Waifu_Chan_Bot_updates"
    BOT_USERNAME = "@Waifu_Chan_Robot"
    CHARA_CHANNEL_ID = "-1002640379822"
    api_id = 28480539
    api_hash = "6320d9f1bc1f0b72ad66ebdb9d6bfc2c"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
