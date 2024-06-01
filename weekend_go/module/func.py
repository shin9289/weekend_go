from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

#測試訊息
def sendText(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='成功'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤'))

#華山1914文創產業園區
def huashan(event):
    url = "https://www.huashan1914.com/w/huashan1914/exhibition?typeId=17111317255246856"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.select('.item-static')

    activity_info = []
    activity_info.append("📢華山1914文創產業園區展覽資訊")
    for row in rows:
        date = row.select_one('.event-date').text.strip()
        title = row.select_one('.card-text-name').text.strip()
        link = row.select_one('a')['href']
        activity_info.append(f"\n活動名稱：{date}\n活動日期：{title}\n活動連結：https://www.huashan1914.com{link}")
    activity_info.append("⚠️活動資訊皆由華山1914文創產業園區官網提供⚠️")
    
    news_text = "\n".join(activity_info)
    try:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=news_text))
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="⚠️emm...系統出了點小問題，請至華山1914文創產業園區官網自行查詢：https://www.huashan1914.com"))


#松山文創園區
def songshan(event):
    url = "https://www.songshanculturalpark.org/exhibition"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.select('.rows')

    activity_info = []
    activity_info.append("📢松山文創園區展覽資訊")
    for row in rows:
        date = row.select_one('.date').text.strip()
        title = row.select_one('.lv_h2').text.strip()
        link = row.select_one('.btn')['href']
        activity_info.append(f"\n活動名稱：{date}\n活動日期：{title}\n活動連結：https://www.songshanculturalpark.org{link}")
    activity_info.append("⚠️活動資訊皆由松山文創園區官網提供⚠️")
    
    news_text = "\n".join(activity_info)
    try:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=news_text))
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="⚠️emm...系統出了點小問題，請至松山文創園區官網自行查詢：https://www.songshanculturalpark.org"))
    

#世貿／南港展覽館
def twtc(event):
    url = "https://www.twtc.com.tw/exhibition.aspx?p=home"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.find('div', {'id': 'menu1'}).find('tbody').find_all('tr')

    activity_info = []
    activity_info.append("📢世貿／南港展覽館4-6月展覽資訊")
    for row in rows:
        date = row.find_all('td')[0].text.strip()
        title = row.find_all('td')[1].find('a').text.strip()
        link = row.find_all('td')[1].find('a')['href']
        if title.lower()=="more":
            continue
        activity_info.append(f"\n活動名稱：{date}\n活動日期：{title}\n活動連結：{link}")
    activity_info.append("⚠️活動資訊皆由台北世貿中心官網提供⚠️")
    
    news_text = "\n".join(activity_info)
    try:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=news_text))
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="⚠️emm...系統出了點小問題，請至台北世貿中心官網自行查詢：https://www.twtc.com.tw/exhibition.aspx?p=home"))

#市集月份
def market_month(event):
    template_message = TemplateSendMessage(
        alt_text='市集月份',
        template=ButtonsTemplate(
            title='請選擇月份',
            text='',
            actions=[
                MessageTemplateAction(
                    label='六月June',
                    text='六月市集資訊',
                ),
                MessageTemplateAction(
                    label='七月July',
                    text='七月市集資訊'
                ),
                MessageTemplateAction(
                    label='八月August',
                    text='八月市集資訊'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, template_message)
