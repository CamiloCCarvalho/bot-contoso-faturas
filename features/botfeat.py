from botcity.core import DesktopBot

wait_low = 100
wait_mid = 500
wait_long = 3000

def bot_paste_l(bot_main: DesktopBot, text: str):
    bot_main.paste(text, wait_low)

def bot_past_m(bot_main: DesktopBot, text:str):
    bot_main.paste(text, wait_mid)

def bot_past_long(bot_main: DesktopBot, text:str):
    bot_main.paste(text, wait_long)

