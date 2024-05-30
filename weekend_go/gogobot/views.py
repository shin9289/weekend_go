from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
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
       func.sendText(event)  # 呼叫func.py中的函式
    if received_text=="松山文創園區展覽資訊":
       func.songshan(event) 