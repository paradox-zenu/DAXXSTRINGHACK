# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20046177"
    API_HASH = "83d15f2956be4b4b927acded8bdf780f"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7797647724:AAGGCkfuaA6QtjTPl0i3DgW9i9ekUJ11CUg")
    MONGO_URL = "mongodb+srv://gojo:gojo123@cluster0.ohs4a.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["6928164580"])
