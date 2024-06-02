from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, MessageTemplateAction
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
               events = parser.parse(body, signature)
        except InvalidSignatureError:
               return HttpResponseForbidden()
        except LineBotApiError:
               return HttpResponseBadRequest()

        for event in events:
               if isinstance(event, MessageEvent):
                     if isinstance(event.message,TextMessage):
                           handle_text_message(event)
        return HttpResponse()
    else:
         return HttpResponseBadRequest ()

def handle_text_message(event):
    #user_id = event.source.user_id
    received_text = event.message.text

    # 測試
    if received_text=="測試":
        func.sendText(event)
    #展覽
    if received_text=="華山1914文創產業園區展覽資訊":
        func.huashan(event) 
    if received_text=="松山文創園區展覽資訊":
        func.songshan(event) 
    if received_text=="世貿／南港展覽館展覽資訊":
        func.twtc(event)
    #市集
    if received_text=="市集":
        actions = [
                MessageTemplateAction(
                    label="六月June",
                    text="六月市集資訊"
                ),
                MessageTemplateAction(
                    label="七月July",
                    text="七月市集資訊"
                ),
                MessageTemplateAction(
                    label="八月August",
                    text="八月市集資訊"
                )
            ]
        func.send_template_message(
            event=event,
            title="請選擇月份",
            text="我們將會整理該月市集資訊給您呦💗",
            actions=actions
        )
    
    #台北秘境
    if received_text=="台北秘境":
        func.taipei_secret_place(event)
    
    #健行步道
    if received_text=="健行步道":
        actions = [
                MessageTemplateAction(
                    label="低",
                    text="低難度健行步道"
                ),
                MessageTemplateAction(
                    label="中",
                    text="中難度健行步道"
                ),
                MessageTemplateAction(
                    label="高",
                    text="高難度健行步道"
                )
            ]
        func.send_template_message(
            event=event,
            title="健行步道",
            text="請選擇難度",
            actions=actions
        )
