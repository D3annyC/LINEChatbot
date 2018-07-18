from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ecJBWIBQJ6RH7/SAo5VqFJFh1RfBkooN2HiwevskFRuznCa8frGzWY/hDNqpGoqsC2m3WmwLL/MxzFZiBgGzVOol1U1oWfYG0u4JUl8cme7O9Y/0vJ4ag2tQUSn1pKdSGBivuyeeyjnZyVpx3y+EzwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('17bf0a209fe18934dfdb579a82118aa6')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text='Hello, world')
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()