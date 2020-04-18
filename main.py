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
    SeparatorComponent, QuickReply, QuickReplyButton
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == “message”:
        if event.message.type == “カレーメニュー”:
            actions = []
            actions.append(MessageImagemapAction(
                  text = ‘１’,
                  area = ImagemapArea(
                      x = 31, y = 49, width = 322, height = 355
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = ‘２’,
                  area = ImagemapArea(
                      x = 360, y = 49, width = 324, height = 365
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = ‘３’,
                  area = ImagemapArea(
                      x = 689, y = 42, width = 316, height = 368
                  )
            ))
            
            message = ImagemapSendMessage(
                base_url = ‘https://currytype01.fc2.net’ + request.host + ‘/imagemap/’ + uuid.uuid4().hex, # prevent cache
                alt_text = ‘代替テキスト’,
                base_size = BaseSize(height=453, width=1040),
                actions = actions
            )
            line_bot_api.reply_message(event.reply_token, message)

@app.route(“/imagemap//“, methods=[‘GET’])
def imagemap(uniqid, size):
    img = Image.open(“./imagemap.png”)
    img_resize = img.resize((int(size), int(size)))
    img_io = io.BytesIO()
    img_resize.save(img_io, ‘PNG’)
    img_io.seek(0)
    return send_file(img_io, mimetype=‘image/png’)
                
                
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

