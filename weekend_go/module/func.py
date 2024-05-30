from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='成功'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤'))

#松山文創園區
def songshan(event):
    url = "https://www.songshanculturalpark.org/exhibition"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.select('.rows')

    activity_info = []
    activity_info.append("🎉松山文創園區🎉")
    for row in rows:
        date = row.select_one('.date').text.strip()
        title = row.select_one('.lv_h2').text.strip()
        link = row.select_one('.btn')['href']
        activity_info.append(f"\n活動名稱：{date}\n活動日期：{title}\n活動連結：https://www.songshanculturalpark.org{link}")

    if activity_info:
        news_text = "\n".join(activity_info)
        try:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=news_text))
                
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="抱歉，沒有找到最新消息。"))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="錯誤2"))
