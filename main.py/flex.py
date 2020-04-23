from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImagemapArea, ImagemapSendMessage, URIImagemapAction, MessageImagemapAction, Video, BaseSize, ExternalLink,
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

#ここから------

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == "message":
        if (event.message.text == "chicken_curry"):
            bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://images.unsplash.com/photo-1585937421612-70a008356fbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='チキンカレー', weight='bold', size='xl'),
                     # material
                    BoxComponent(
                        layout='baseline',
                        spacing='sm',
                        contents=[
                            TextComponent(
                                text='材料\n　・鶏モモ肉\n　・タマネギ\n　・シメジ\n　・トマトソース（お好きな調味料）\n　・水\n　・オリーブオイル\n　・バター\n　・カレー（お好きなスパイス、ハーブ）',
                                color='#aaaaaa',
                                size='sm',
                                flex=1
                            ),
                        ],
                    )
                ],
            ),
                            footer=BoxComponent(
                                layout='vertical',
                                spacing='sm',
                                contents=[
                                    SpacerComponent(size='sm'),
                                    ButtonComponent(
                                        style='text',
                                        height='sm',
                                        action=MessageAction(label='選びなおす', text='cancel_chicken_curry'),
                                    ),
                                    SeparatorComponent(),
                                    ButtonComponent(
                                        style='text',
                                        height='sm',
                                        action=MessageAction(label='次へ進む', text="next_chicken_curry")
                                    ),
                                ]
                            ),
        )
        message = FlexSendMessage(alt_text="curry_menu_CC", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message




#ここまで------


    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save content.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
