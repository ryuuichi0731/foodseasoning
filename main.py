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
        if (event.message.text == "カレーメニュー") or (event.message.text == "chicken_curry_cancel") or (event.message.text == "green_curry_cancel") or (event.message.text == "keema_curry_cancel"):
            TextSendMessage(
                text='画像メニューから自分好みのカレーを選んでね。',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/images01',

                alt_text='curry_imagemap_no.01',

                base_size=BaseSize(height=453, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='chicken_curry',
                        area=ImagemapArea(
                            x=30, y=50, width=320, height=355
                        )
                    ),
                    MessageImagemapAction(
                        text='green_curry',
                        area=ImagemapArea(
                            x=360, y=50, width=320, height=355
                        )
                    ),
                    MessageImagemapAction(
                        text='keema_curry',
                        area=ImagemapArea(
                            x=690, y=50, width=320, height=355
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
#img_powder
    if event.type == "message":
        if (event.message.text == "chicken_curry_next") or (event.message.text == "green_curry_next") or (event.message.text == "keema_curry_next"):
            TextSendMessage(
                text='画像メニューから自分好みのスパイスを選んでね。',
            ),
            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/powder_img',

                alt_text='powder_spice_img',

                base_size=BaseSize(height=685, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='spice_clove',
                        area=ImagemapArea(
                            x=0, y=10, width=150, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_cinnamon',
                        area=ImagemapArea(
                            x=160, y=10, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_cumin',
                        area=ImagemapArea(
                            x=330, y=10, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_tougarashi',
                        area=ImagemapArea(
                            x=860, y=10, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_bigcardamon',
                        area=ImagemapArea(
                            x=0, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_nutmeg',
                        area=ImagemapArea(
                            x=160, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_allspice',
                        area=ImagemapArea(
                            x=340, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_bayleaf',
                        area=ImagemapArea(
                            x=510, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_greencardamon',
                        area=ImagemapArea(
                            x=340, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_coriander',
                        area=ImagemapArea(
                            x=680, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_blackpepper',
                        area=ImagemapArea(
                            x=870, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_mace',
                        area=ImagemapArea(
                            x=520, y=10, width=170, height=320
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)            

            
#チキンカレー_flex            
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
                    # info
                        BoxComponent(
                            layout='vertical',
                            margin='lg',
                            spacing='sm',
                            contents=[
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='材料名',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=' ①鶏モモ肉\n ②タマネギ\n ③シメジ\n ④水\n ⑤オリーブオイル\n ⑥バター',
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5
                                        )
                                    ],
                                ),
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='spice',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=" ⑦お好きな調味料\n　（トマトソース）\n ⑧お好きなスパイス",
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5,
                                        ),
                                    ],
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
                        style='primary',
                        height='sm',
                        action=MessageAction(label='次へ進む', text='chicken_curry_next'),
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='secondary',
                        height='sm',
                        action=MessageAction(label='カレーを選びなおす', text="chicken_curry_cancel")
                    )
                ]
                ),
            )
            message = FlexSendMessage(alt_text="hello", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )

            
#チキンカレー_flex 

#グリーンカレー_flex            
    if event.type == "message":
        if (event.message.text == "green_curry"):
            bubble = BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url='https://images.unsplash.com/photo-1560684352-8497838a2229?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                    # title
                        TextComponent(text='グリーンカレー', weight='bold', size='xl'),
                    # info
                        BoxComponent(
                            layout='vertical',
                            margin='lg',
                            spacing='sm',
                            contents=[
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='材料名',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=' ①鶏モモ肉\n ②タマネギ\n ③ほうれん草\n ④ナス\n ⑤エリンギ\n ⑥豆乳\n ⑦オリーブオイル',
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5
                                        )
                                    ],
                                ),
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='spice',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=" ⑦お好きな調味料\n　（グリーンペースト）\n ⑧お好きなスパイス",
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5,
                                        ),
                                    ],
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
                        style='primary',
                        height='sm',
                        action=MessageAction(label='次へ進む', text='green_curry_next'),
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='secondary',
                        height='sm',
                        action=MessageAction(label='カレーを選びなおす', text="green_curry_cancel")
                    )
                ]
                ),
            )
            message = FlexSendMessage(alt_text="hello", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )

            
#グリーンカレー_flex

#キーマカレー_flex            
    if event.type == "message":
        if (event.message.text == "keema_curry"):
            bubble = BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url='https://production-orp.s3.amazonaws.com/uploads/recipes/image/0000300319/20160801160506.jpg',
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                    # title
                        TextComponent(text='キーマカレー', weight='bold', size='xl'),
                    # info
                        BoxComponent(
                            layout='vertical',
                            margin='lg',
                            spacing='sm',
                            contents=[
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='材料名',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=' ①豚挽肉\n ②ピーマン\n ③赤ピーマン\n ④タマネギ\n ⑤ニンジン\n ⑥コーン\n ⑦水\n ⑧オリーブオイル',
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5
                                        )
                                    ],
                                ),
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='spice',
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=" ⑦お好きな調味料\n　（味噌ソース）\n ⑧お好きなスパイス",
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5,
                                        ),
                                    ],
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
                        style='primary',
                        height='sm',
                        action=MessageAction(label='次へ進む', text='keema_curry_next'),
                    ),
                    SeparatorComponent(),
                    ButtonComponent(
                        style='secondary',
                        height='sm',
                        action=MessageAction(label='カレーを選びなおす', text="keema_curry_cancel")
                    )
                ]
                ),
            )
            message = FlexSendMessage(alt_text="hello", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )          
#キーマカレー_flex
            
            
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
