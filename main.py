from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(
    'xYCsNc5Y1TuoZ3bNc7I2NA/3q2ranP+PVXLw3NYfzR6oVZZZt0HpXwMx5xiIXL/l/CcTnmbfdLzSNK+pamj4o6Hp57DRHfYRPJFVRiFVJ3GXiJgwwD7K5KqtT33ghT8Ur3J+2t18bHPhHxiPGd7AwwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f24522c4332ab6a8f2e20cf21cc86498')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )


if __name__ == "__main__":
    app.run()
