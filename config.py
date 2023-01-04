import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "2899387")) #optional
API_HASH = getenv("API_HASH", "067b3319346995e9e48ee5214204960b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1965690214").split()))
OWNER_ID = int(getenv("tanya"))
MONGO_URL = getenv("MONGO_URL", "https://cloud.mongodb.com/v2/63b44950f41e791783e487d5#/clusters")
BOT_TOKEN = getenv("BOT_TOKEN", "5967565644:AAGdxLgh1jUObIhdnrYZkrW1CQApMIHw2gI")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "1001739310661")
LOG_GROUP = getenv("LOG_GROUP","1001615991661")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change

STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAiOQfUxaiHJJkmZuksRPt2s6HaU6PwUyTQVxm8mrPoEuk1AhMvyMmNqyL4RH-OSb2yQJ3cSDcSg1-3tHZZ_cEhomfH50V0USnhHaAbAd_OqT25BZHM5Ey_bkZsUhsN8WoqLDW-MlkSrQpgxPztMxOPRGWmNNaHrbpHgkA8fiHjWMrzOVZaEoLt307mPYdfxutCWP2YSwsgq7s7hAuWnasQUFxzyLVm8Gy0TTl_XBSyhMbO3EWtyP_k1_GpSoU-BLMDy3WpP_rfdre37dmkvKpO1cNqbisp2UW8JU3tqVwEe-eO4r5-q0T3y5OQR_EqvGCBkCl_UoLqaMl89-ZK7Er9AAAAAB1Kg1mAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
