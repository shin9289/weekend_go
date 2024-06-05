from django.conf import settings
import requests
from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, FlexSendMessage, ImageSendMessage

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
                          "uri": "https://maps.app.goo.gl/iDW4AC1g5J4ZGtYG7"
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
                          "uri": "https://maps.app.goo.gl/b9AvL5xpfQisRy6CA"
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
            "url": "https://camilleblog.com/wp-content/uploads/2021/09/%E9%99%BD%E6%98%8E%E5%B1%B1%E6%99%AF%E9%BB%9E-%E8%8D%89%E5%B1%B1%E7%8E%89%E6%BA%AA-by-camilleblog.com-2021090413.jpg",
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
                          "uri": "https://maps.app.goo.gl/avv95r9QnCjBbMx46"
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
                          "uri": "https://maps.app.goo.gl/NufueX3HPV264r6Z9"
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
                          "uri": "https://maps.app.goo.gl/6HGwkdtmZutuuzkF9"
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

#低難度健行步道
def easy_trail(event):
    flex_message = FlexSendMessage(
            alt_text='低難度健行步道',
            contents={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "低難度健行步道",
            "size": "xl",
            "weight": "bold"
          }
        ],
        "flex": 3
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "難度",
            "align": "center",
            "weight": "bold",
            "color": "#905c44",
            "offsetBottom": "xs"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "xl"
          }
        ],
        "flex": 2
      }
    ],
    "paddingBottom": "xs"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "劍潭山親山步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=34"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "Google Map",
                  "uri": "https://maps.app.goo.gl/p2ip8a4h5CDRHAgXA"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "新山夢湖登山步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=55"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "Google Map",
                  "uri": "https://maps.app.goo.gl/2XYU2Rr1eww4Hotb7"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "頂山—石梯嶺步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=10"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "Google Map",
                  "uri": "https://maps.app.goo.gl/awBH64i5StmBqjp4A"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "明舉山步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=45"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "Google Map",
                  "uri": "https://maps.app.goo.gl/sbFcv43aitGhYpuU8"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "樹梅古道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=1427"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "Google Map",
                  "uri": "https://maps.app.goo.gl/YDmmE6rPF6m6BFei9"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      }
    ],
    "paddingAll": "md"
  }
            } 
    )
    line_bot_api.reply_message(event.reply_token, flex_message)

#中難度健行步道
def medium_trail(event):
    flex_message = FlexSendMessage(
            alt_text='中難度健行步道',
            contents={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "中難度健行步道",
            "size": "xl",
            "weight": "bold"
          }
        ],
        "flex": 3
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "難度",
            "align": "center",
            "weight": "bold",
            "color": "#905c44",
            "offsetBottom": "xs"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "xl"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "xl"
          }
        ],
        "flex": 2
      }
    ],
    "paddingBottom": "xs"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "陽明山東西大縱走",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=428"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/V8natfQR1dkVHtaS9"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "小觀音山群峰步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=605"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/3Mc79ZWjmhA7BGE49"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "環台北天際線第一段",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          },
          {
            "type": "text",
            "text": "石碇至新店",
            "color": "#5f473a",
            "weight": "bold",
            "size": "md"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=960"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/2CryGVbXjcJJELEi8"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "大屯主峰步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=69"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/doUZoJN11twzzHwL9"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "猴山岳登山步道",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=133"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/3L2QbDGQf7nPAL7y6"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      }
    ],
    "paddingAll": "md"
  }
            } 
    )
    line_bot_api.reply_message(event.reply_token, flex_message)

#高難度健行步道
def hard_trail(event):
    flex_message = FlexSendMessage(
            alt_text='高難度健行步道',
            contents={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "高難度健行步道",
            "size": "xl",
            "weight": "bold"
          }
        ],
        "flex": 3
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "難度",
            "align": "center",
            "weight": "bold",
            "color": "#905c44",
            "offsetBottom": "xs"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "xl"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "xl"
          },
          {
            "type": "icon",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "size": "xl"
          }
        ],
        "flex": 2
      }
    ],
    "paddingBottom": "xs"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "筆架連峰",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=51"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/tuoLHQpw2pvxdFrC8"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "三峽五寮尖",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=88"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/au8PXZT9FSUzeLfZ7"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "基隆劍龍稜",
            "size": "lg",
            "weight": "bold",
            "color": "#5f473a"
          }
        ],
        "paddingAll": "lg",
        "backgroundColor": "#f4e8d5"
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
                  "label": "步道介紹",
                  "uri": "https://hiking.biji.co/index.php?q=trail&act=detail&id=662"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "登山口",
                  "uri": "https://maps.app.goo.gl/DKH69aCcK1cjCpB49"
                },
                "style": "primary",
                "height": "sm",
                "color": "#5f473a"
              }
            ],
            "margin": "md"
          }
        ],
        "backgroundColor": "#f4e8d5",
        "paddingBottom": "md",
        "paddingEnd": "md"
      }
    ],
    "paddingAll": "md"
  }
            } 
    )
    line_bot_api.reply_message(event.reply_token, flex_message)

#基隆河自行車道
def keelungbike(event):
  image_message = ImageSendMessage(
  original_content_url='https://www.travel.taipei/content/images/2023/map/Keelung.jpg',
  preview_image_url='https://www.travel.taipei/content/images/2023/map/Keelung.jpg'
  )
  text='從左岸的林安泰疏散門進入河濱自行車道，遊客可以看見記錄著基隆河緣起、整治故事的解說牌，讓民眾在運動休閒之餘，還能了解基隆河長長的歷史故事。\n\n大佳河濱公園是屬河床填土後的新生地，放眼望去盡是綠野草皮，靠西之地建設成都會型綠化公園，其中以中山橋到大直橋間段的親水公園最具特色，地標「希望之泉」的噴泉設計，高達25層樓高的扇形噴泉水幕，精采的水舞、夜晚亮麗的五彩霓虹燈光，整個河濱之地瞬間成為繽紛亮麗，背景在圓山飯店古典輝煌的紅色建築陪襯下，景致格外好看、令人難忘，可以說是市區閤家老少、戀愛男女朋友約會的最佳去處。\n\n遊客若是從右岸的美堤疏散門進入，也同樣可以看見堤防壁上用圖案細說基隆河的歷史故事，沿途騎乘至南湖河濱公園右岸「 內湖葫蘆洲吊橋橋墩 」及「 五分吊橋遺址 」感受基隆河發展之歷史見證，同樣精彩耀眼，夜遊基隆河，更可看到眩麗的摩天輪及內湖科技園區夜景。'
  line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
  line_bot_api.reply_message(event.reply_token, image_message)


