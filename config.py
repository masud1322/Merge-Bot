import os


class Config(object):
    API_HASH = os.environ.get("37cd301906894752fd9b7881924921b4")
    BOT_TOKEN = os.environ.get("7755705821:AAE9rySNaQVsH7sKP-xbp1XQbquPDpHFQVo")
    TELEGRAM_API = os.environ.get("24237949")
    OWNER = os.environ.get("7202314047")
    OWNER_USERNAME = os.environ.get("cinemazbd_official", "CodeXBro")
    PASSWORD = os.environ.get("1234")
    DATABASE_URL = os.environ.get("mongodb+srv://realtechbd3:OMZVjlDOUiR8ODfO@cluster0.cr9m6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002426353185")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("BQG67qcAhz0_JtHmlqwrPRBXiVcsJsSa3c433h4TMO_IEDBLSMAUG9Rn-J5QlqbCTjgK0uBM9IFsrLUjc4a8Lqp6maVYJ6CfdPiudpj-fF-yQ3cVxb-LLhPAyuzr_Z8CAMZkxsrazFvellC_H7ZplbtK4Ly9rZA7mdmWZIBnPjBEFs59RVjLVkiWaLRkNzuTm-eamYmekpiwGGtRDnyuHia0UtR0HfX-BF0mq6laO12GdTVCtup6gzfN-UTfaS2pD4dWFO0-SXRgkJ0GwT32xG-6JSsYDPF1hSTaBQmIf8vFYMi3evd9XcuC8OU9JRdlkMmELgUx0nPbmB2phg6PbOfcKSQ2MwAAAAGtSpc_AA", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
