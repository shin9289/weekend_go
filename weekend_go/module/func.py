from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, FlexSendMessage

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

#按鈕樣板
def send_template_message(event, title, text, actions):
    buttons_template = ButtonsTemplate(
        title=title,
        text=text,
        actions=actions
    )
    template_message = TemplateSendMessage(
        alt_text=title,
        template=buttons_template
    )
    line_bot_api.reply_message(event.reply_token, template_message)


#台北秘境
def taipei_secret_place(event):
    flex_message = FlexSendMessage(
            alt_text='台北秘境',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://tlife.thsrc.com.tw/s3/quill/20230222-R3aME3ohw8rlcgSVm28BISvKxZxvwoWhv1evnEbb.jpg",
            "size": "full",
            "gravity": "top",
            "aspectRatio": "3:4",
            "aspectMode": "cover"
          }
        ],
        "paddingAll": "0px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "陽明湧泉與水道系統",
                    "size": "xl",
                    "color": "#000000",
                    "weight": "bold"
                  }
                ],
                "paddingAll": "5px"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://img.icons8.com/?size=100&id=53430&format=png&color=FAB005",
                    "margin": "5px"
                  },
                  {
                    "type": "text",
                    "text": "台北市 北投區",
                    "margin": "10px"
                  }
                ],
                "paddingBottom": "3px",
                "paddingAll": "3px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "秘境介紹",
                          "uri": "https://travel.yam.com/article/125078"
                        },
                        "style": "primary",
                        "color": "#905c44"
                      }
                    ],
                    "margin": "2px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "怎麼去？",
                          "uri": "https://www.google.com/maps/place/%E9%99%BD%E6%98%8E%E6%B9%A7%E6%B3%89/@25.1449818,121.5170681,13.83z/data=!4m6!3m5!1s0x3442ade6a5f6bba7:0x744ac6a7d40de4a2!8m2!3d25.1422858!4d121.5433745!16s%2Fg%2F11g7cv1gvx?authuser=0&entry=ttu"
                        },
                        "style": "primary",
                        "color": "#b78b68"
                      }
                    ],
                    "margin": "2px"
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ytimg.com/vi/lk0dDcxA6EM/maxresdefault.jpg",
            "size": "full",
            "gravity": "top",
            "aspectRatio": "3:4",
            "aspectMode": "cover"
          }
        ],
        "paddingAll": "0px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "本山礦場",
                    "size": "xl",
                    "color": "#000000",
                    "weight": "bold"
                  }
                ],
                "paddingAll": "5px"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://img.icons8.com/?size=100&id=53430&format=png&color=FAB005",
                    "margin": "5px"
                  },
                  {
                    "type": "text",
                    "text": "新北市 瑞芳區",
                    "margin": "10px"
                  }
                ],
                "paddingBottom": "3px",
                "paddingAll": "3px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "秘境介紹",
                          "uri": "https://newtaipei.travel/zh-tw/attractions/detail/111421"
                        },
                        "style": "primary",
                        "color": "#905c44"
                      }
                    ],
                    "margin": "2px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "怎麼去？",
                          "uri": "https://www.google.com/maps/place/%E6%9C%AC%E5%B1%B1%E7%A4%A6%E5%A0%B4/@25.1018012,121.8562666,17z/data=!3m1!4b1!4m6!3m5!1s0x345d44dfa8b89181:0xb5cbc074abfe37bb!8m2!3d25.1017964!4d121.8588415!16s%2Fg%2F11cspthz85?authuser=0&entry=ttu"
                        },
                        "style": "primary",
                        "color": "#b78b68"
                      }
                    ],
                    "margin": "2px"
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
            } 
    )
    line_bot_api.reply_message(event.reply_token, flex_message)





