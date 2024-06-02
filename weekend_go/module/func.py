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
  "contents": 
  [
    #陽明湧泉與水道系統
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
                          "uri": "https://www.google.com/maps/place/%E5%B0%8F%E9%9A%B1%E6%BD%AD%E7%80%91%E5%B8%83/@25.156683,121.5387329,16.47z/data=!4m6!3m5!1s0x3442adff1d510b01:0x1d9e751f23ade22e!8m2!3d25.1566331!4d121.540597!16s%2Fg%2F11c5zss_qk?authuser=0&entry=ttu"
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
    #小隱潭瀑布
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://taiwantour.info/wp-content/uploads/2019/09/1568383582-2229d1619a5165a2d51288aba06c39b4.jpg",
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
                    "text": "小隱潭瀑布",
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
                          "uri": "https://travel.yam.com/article/109163"
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
    },
    #草山玉溪石雕博物館
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcNC3M57bi9Z3Dfd5JeEzsFY8GyU7QwMB1gQ&s",
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
                    "text": "草山玉溪石雕博物館",
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
                    "text": "台北市 士林區",
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
                          "uri": "https://www.facebook.com/garden91/"
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
                          "uri": "https://www.google.com/maps/place/Garden91%E8%8D%89%E5%B1%B1%E7%8E%89%E6%BA%AA+(%E9%9C%80%E9%A0%90%E7%B4%84)/@25.107354,121.545329,15z/data=!4m5!3m4!1s0x0:0x336f56b10ffba362!8m2!3d25.107354!4d121.545329?sa=X&ved=2ahUKEwi3pbOP7-b7AhWvGaYKHQhoAg8Q_BJ6BAh6EAgB3%E7%80%91%E5%B8%83%EF%BD%9C%E9%8A%80%E6%B2%B3%E6%B4%9E/@24.9584884,121.5834063,15z/data%3D!4m2!3m1!1s0x0:0xd5265b4d2872f3ee?sa%3DX&ved=2ahUKEwiN2o237eb7AhUtE6YKHQKBBwEQ_BJ6BAhuEAg9%EF%BF%BD%EF%BF%BD%E9%A7%9D%E5%B3%B0/@25.2029854,121.69453,15z/data%3D!4m2!3m1!1s0x0:0xaa86df60b19fb4b?sa%3DX&ved=2ahUKEwiP0K_gveb7AhUFr1YBHTfMAAcQ_BJ6BAhwEAg9A%EF%BF%BD%E6%BD%AD%E7%80%91%E5%B8%83/@25.1566331,121.540597,15z/data%3D!4m5!3m4!1s0x0:0x1d9e751f23ade22e!8m2!3d25.1566331!4d121.5405970%E6%99%AF%E5%B9%B3%E5%8F%B0/@24.9403904,121.6317818,15z/data%3D!4m2!3m1!1s0x0:0x8cd38a6367d9ff9?sa%3DX&ved=2ahUKEwiTs-GH5dL7AhX_QPUHHVs7DdEQ_BJ6BQiCARAIE6%EF%BF%BD%EF%BF%BD%E5%85%89%E7%94%9F%E6%B4%BB%E5%9C%92%E5%8D%80/@25.0304218,121.5259963,15z/data%3D!4m5!3m4!1s0x0:0xf2c6ce7963e83e59!8mE7%EF%BF%BD%EF%BF%BD%E5%9C%92/@24.9985635,121.5809857,15z/data%3D!4m2!3m1!1s0x0:0xaafe06fd09b4d766?sa%3DX&ved=2ahUKEwjsg8jwmdD7AhUUM94KHYEwAkIQ_BJ6BQiOARAIAB%EF%BF%BD%E5%8B%95%E7%89%A9%E5%9C%92/@24.9985635,121.5809857,15z/data%3D!4m2!3m1!1s0x0:0xaafe06fd09b4d766?sa%3DX&ved=2ahUKEwimw-GL8cj7AhXQMd4KHUXVD-sQ_BJ6BQiZARAIE5%EF%BF%BD%EF%BF%BD%E7%B8%BD%E7%9D%A3%E6%BA%AB%E6%B3%89/@25.2221157,121.6459792,15z/data%3D!4m2!3m1!1s0x0:0xf7578af19df2fdf1?sa%3DX&ved=2ahUKEwjWvdiL4cP7AhWMFogKHQ3OA2IQ_BJ6BAh7EAgBE%EF%BF%BD%E6%97%85%E6%99%A8%E6%BA%AB%E6%B3%89%E6%B0%91%E5%AE%BF/@24.8655855,121.54752,15z/data%3D!4m2!3m1!1s0x0:0x2300d487cb11cb43?sa%3DX&ved=2ahUKEwi4oNDNqsH7AhWFB94KHUGXCFsQ_BJ6BAhoEAc%E6%98%A5%E5%A4%A9%E9%85%92%E5%BA%97/@25.137598,121.513561,15z/data%3D!4m8!3m7!1s0x0:0x12d9124e8cdfc5e6!5m2!4m1!1i2!8m2!3d25.137598!4d121.513561%E6%98%8E%E5%B1%B1%E5%A4%A9%E7%B1%9F%E6%B8%A1%E5%81%87%E9%85%92%E5%BA%97/@25.2019363,121.5954122,15z/data%3D!4m8!3m7!1s0x0:0x7c7fb525471a2ad7!5m2!4m1!1i2!8m2!3d25.2019363!4d121.5954122&coh=164777&entry=tt&shorturl=1"
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
    #馬槽花藝村
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://blogger.googleusercontent.com/img/a/AVvXsEi71TXTAtKmuU2kDiN26pXMxjAaLrB4LCjnmfkfJo1wguHCBfQAPX4JCnPN_SRq7X8EWgTfGNdfwTaiAGuaGHCoOzdwoeFAn7WBusb9VBJb0VNBunD1GyZ1Uvir4cq4Qcxjo3il305K-b-64faMS8bvb6aYJPM908LRF_VqoJWuvL1eKRbfpK0wYJyY=s1000",
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
                    "text": "馬槽花藝村",
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
                    "text": "台北市 士林區",
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
                          "uri": "https://niniyeh.com/flowervillage/"
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
                          "uri": "https://www.google.com/maps/place/%E9%A6%AC%E6%A7%BD%E8%8A%B1%E8%97%9D%E6%9D%91(%E9%99%BD%E6%98%8E%E5%B1%B1%E6%BA%AB%E6%B3%89)/@25.1887408,121.5694004,15z/data=!4m2!3m1!1s0x0:0x505b1e4cf7148715?sa=X&ved=1t:2428&ictx=111"
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
    #本山礦場
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
    },
    #觀音山蓄水池
    {
      "type": "bubble",
      "size": "mega",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://storage.googleapis.com/smiletaiwan-cms-cwg-tw/article/202101/article-6007c20c2740d.jpg",
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
                    "text": "觀音山蓄水池",
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
                    "text": "台北市 中正區",
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
                          "uri": "https://travel.yam.com/article/128816"
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
                          "uri": "https://www.google.com/maps/place/%E8%A7%80%E9%9F%B3%E5%B1%B1%E8%93%84%E6%B0%B4%E6%B1%A0/@25.0120986,121.5323697,17z/data=!4m6!3m5!1s0x3442a9f4dd56d381:0xb4bd9fd85efd5012!8m2!3d25.0111118!4d121.533464!16s%2Fg%2F11c45y56st?authuser=0&entry=ttu"
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





