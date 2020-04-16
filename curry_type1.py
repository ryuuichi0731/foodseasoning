from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    ImagemapArea,
    ImagemapSendMessage,
    URIImagemapAction,
    MessageImagemapAction,
    Video, BaseSize, ExternalLink,
)

import os
import json

#アクセスキーの取得
app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

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

#ここからーーー ーーー 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == “message”:
        if event.message.type == “テスト”:
            
            imagemap_message = ImagemapSendMessage(
                base_url='https://example.com/imagemap/image',
                alt_text='this is an imagemap',
                
                base_size=BaseSize(height=453, width=1040),
                actions=[
                    MessageImagemapAction(
                        text='hello',
                        area=ImagemapArea(
                            x=35, y=60, width=310, height=335
                        )
                    ),
                    MessageImagemapAction(
                        text='hello',
                        area=ImagemapArea(
                            x=365, y=60, width=310, height=335
                        )
                    ),
                    MessageImagemapAction(
                        text='hello',
                        area=ImagemapArea(
                            x=690, y=60, width=310, height=335
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
   
