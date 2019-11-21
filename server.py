from flask import Flask, request, abort
import os
import random

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

line_bot_api = LineBotApi(
    'sRbByNEreS9vEJAZtCsgmiC8lZIK8npaiAy/b8qo43pTnMJVLNRkjfo3gx9+dYeFyGtbyAkI/8lNCijh6BHB76qV5mPl40ayKAy8gaB8yI1ZxeY80oO6T+nRl/+BEXzNFGABQLdjqr0JmPOZO7+Y8QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c8b7d4d90e16fb47555b486b1734f82b')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    except Exception as e:
        pass

    return 'OK'


msg = ["完全錯誤！", "也許吧", "有可能", "沒錯！", "可能是、可能不是", "我不認為", "沒有吧", "應該是", "我不知道"]


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg[random.randint(len(msg))]))


if __name__ == "__main__":
    app.run()
