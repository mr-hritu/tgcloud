import os

class Config:
    API_ID = int( os.getenv("api_id","29616312") )
    API_HASH = os.getenv("api_hash","dd1a05ab4c47a5a037cc067cf4bded27")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001924268233") )
    CHANNEL_USERNAME = os.getenv("channel_username","private_bots")
    TOKEN = os.getenv("token","6204094475:AAF4073uqa1RNcTtgHfHaUUyi7vkKvxBQq8")
    DOMAIN  = os.getenv("domain","https://testapp.herokuapp.com")
 
