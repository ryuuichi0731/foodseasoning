from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, MessageImagemapAction,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton, ImagemapArea,ImagemapSendMessage,
    URIImagemapAction, MessageImagemapAction, Video, BaseSize, ExternalLink,
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == “message”:
        if event.message.type == “カレーメニュー”:
            'base_url': 'https://foodseasoning.web.fc2.com/img/images01',
            'alt_text': 'This is an imagemap',
            'base_size': BaseSize(width=1040, height=453),
            
            'actions': [
                MessageImagemapAction(
                    text='Hey',
                    area=ImagemapArea(x=30, y=50, width=320, height=355)
                ),
                MessageImagemapAction(
                    text='Hey',
                    area=ImagemapArea(x=360, y=50, width=320, height=355)
                ),
                MessageImagemapAction(
                    text='Hey',
                    area=ImagemapArea(x=690, y=50, width=320, height=355)
                )
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGEMAP),
            ImagemapSendMessage(**arg).as_json_dict()
        )           
                
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

