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
        if (event.message.text == "Curry Menu") or (event.message.text == "chicken_curry_cancel") or (event.message.text == "green_curry_cancel") or (event.message.text == "keema_curry_cancel"):
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
        if (event.message.text == "chicken_curry_next") or (event.message.text == "green_curry_next") or (event.message.text == "keema_curry_next") or (event.message.text == "01_I'm Done") or (event.message.text == "Powder Spice"):
            TextSendMessage(
                text='画像メニューから自分好みのスパイスを選んでね。',
            ),
            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/powder_img',

                alt_text='powder_spice_img',

                base_size=BaseSize(height=750, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='spice_clove',
                        area=ImagemapArea(
                            x=0, y=10, width=160, height=330
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_cinnamon',
                        area=ImagemapArea(
                            x=160, y=0, width=160, height=330
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_cumin',
                        area=ImagemapArea(
                            x=330, y=0, width=160, height=330
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_tougarashi',
                        area=ImagemapArea(
                            x=860, y=10, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_blackpepper',
                        area=ImagemapArea(
                            x=510, y=10, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_mace',
                        area=ImagemapArea(
                            x=690, y=0, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_tougarashi',
                        area=ImagemapArea(
                            x=860, y=0, width=170, height=320
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
                            x=330, y=340, width=170, height=320
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
                            x=680, y=340, width=170, height=320
                        )
                    ),
                    MessageImagemapAction(
                        text='spice_coriander',
                        area=ImagemapArea(
                            x=860, y=340, width=170, height=320
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)

#spice_flavor_ring            
    if event.type == "message":
        if (event.message.text == "02_I'm Done") or (event.message.text == "Whole Spice"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/s.f.h',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=995, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='spicy_flavor',
                        area=ImagemapArea(
                            x=100, y=500, width=280, height=210
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_flavor',
                        area=ImagemapArea(
                            x=390, y=60, width=240, height=230
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_flavor',
                        area=ImagemapArea(
                            x=650, y=280, width=270, height=210
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_flavor',
                        area=ImagemapArea(
                            x=380, y=710, width=260, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='hot_flavor',
                        area=ImagemapArea(
                            x=110, y=250, width=250, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='herb_flavor',
                        area=ImagemapArea(
                            x=650, y=500, width=270, height=210
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
            
    #hall_spice_sweet
    if event.type == "message":
        if (event.message.text == "sweet_flavor"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/hall_spice/sweet',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=994, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='sweet_1',
                        area=ImagemapArea(
                            x = 61, y = 40, width = 293, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_2',
                        area=ImagemapArea(
                            x = 366, y = 42, width = 304, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_3',
                        area=ImagemapArea(
                            x = 681, y = 45, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_4',
                        area=ImagemapArea(
                            x = 61, y = 355, width = 289, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_5',
                        area=ImagemapArea(
                            x = 366, y = 356, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_6',
                        area=ImagemapArea(
                            x = 677, y = 351, width = 314, height = 305
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_7',
                        area=ImagemapArea(
                            x = 50, y = 660, width = 309, height = 299
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_8',
                        area=ImagemapArea(
                            x = 369, y = 661, width = 304, height = 298
                        )
                    ),
                    MessageImagemapAction(
                        text='sweet_9',
                        area=ImagemapArea(
                            x = 680, y = 661, width = 320, height = 296
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
#hall_spice_spicy
    if event.type == "message":
        if (event.message.text == "spicy_flavor"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/hall_spice/spicy',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=773, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='spicy_1',
                        area=ImagemapArea(
                            x = 61, y = 40, width = 293, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='spicy_2',
                        area=ImagemapArea(
                            x = 366, y = 42, width = 304, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='spicy_3',
                        area=ImagemapArea(
                            x = 681, y = 45, width = 304, height = 291
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
            
    #hall_spice_hot
    if event.type == "message":
        if (event.message.text == "hot_flavor"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/hall_spice/hot',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=994, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='hot_1',
                        area=ImagemapArea(
                            x = 61, y = 40, width = 293, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='hot_2',
                        area=ImagemapArea(
                            x = 366, y = 42, width = 304, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='hot_3',
                        area=ImagemapArea(
                            x = 681, y = 45, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='hot_4',
                        area=ImagemapArea(
                            x = 61, y = 355, width = 289, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='hot_5',
                        area=ImagemapArea(
                            x = 366, y = 356, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='hot_6',
                        area=ImagemapArea(
                            x = 677, y = 351, width = 314, height = 305
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
            
    #hall_spice_harbr
    if event.type == "message":
        if (event.message.text == "herb_flavor"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/hall_spice/harbr',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=957, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='harbr_1',
                        area=ImagemapArea(
                            x = 61, y = 40, width = 293, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='harbr_2',
                        area=ImagemapArea(
                            x = 366, y = 42, width = 304, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='harbr_3',
                        area=ImagemapArea(
                            x = 681, y = 45, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='harbr_4',
                        area=ImagemapArea(
                            x = 61, y = 355, width = 289, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='harbr_5',
                        area=ImagemapArea(
                            x = 366, y = 356, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='harbr_6',
                        area=ImagemapArea(
                            x = 677, y = 351, width = 314, height = 305
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
            
    #hall_spice_fresh
    if event.type == "message":
        if (event.message.text == "fresh_flavor"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/hall_spice/fresh',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=992, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='fresh_1',
                        area=ImagemapArea(
                            x = 61, y = 40, width = 293, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_2',
                        area=ImagemapArea(
                            x = 366, y = 42, width = 304, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_3',
                        area=ImagemapArea(
                            x = 681, y = 45, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_4',
                        area=ImagemapArea(
                            x = 61, y = 355, width = 289, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_5',
                        area=ImagemapArea(
                            x = 366, y = 356, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_6',
                        area=ImagemapArea(
                            x = 677, y = 351, width = 314, height = 305
                        )
                    ),
                    MessageImagemapAction(
                        text='fresh_7',
                        area=ImagemapArea(
                            x = 50, y = 660, width = 309, height = 299
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
            
    #hall_spice_bitter
    if event.type == "message":
        if (event.message.text == "bitter_flavor"):
            TextSendMessage(
                text='flavor_ring',
            ),

            imagemap_message = ImagemapSendMessage(

                base_url='https://foodseasoning.web.fc2.com/img/hall_spice/bitter',

                alt_text='spice_flavor_ring',

                base_size=BaseSize(height=994, width=1040),

                actions=[
                    MessageImagemapAction(
                        text='bitter_1',
                        area=ImagemapArea(
                            x = 61, y = 40, width = 293, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_2',
                        area=ImagemapArea(
                            x = 366, y = 42, width = 304, height = 296
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_3',
                        area=ImagemapArea(
                            x = 681, y = 45, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_4',
                        area=ImagemapArea(
                            x = 61, y = 355, width = 289, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_5',
                        area=ImagemapArea(
                            x = 366, y = 356, width = 304, height = 291
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_6',
                        area=ImagemapArea(
                            x = 677, y = 351, width = 314, height = 305
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_7',
                        area=ImagemapArea(
                            x = 50, y = 660, width = 309, height = 299
                        )
                    ),
                    MessageImagemapAction(
                        text='bitter_8',
                        area=ImagemapArea(
                            x = 369, y = 661, width = 304, height = 298
                        )
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, imagemap_message)
            
       
            
#クイックリプライ（spice_g）
#def spice_quantity
    if event.type == "message":
        if (event.message.text == "spice_clove") or (event.message.text == "spice_allspice") or (event.message.text == "spice_nutmeg") or (event.message.text == "spice_cinnamon") or (event.message.text == "spice_bigcardamon") or (event.message.text == "spice_mace") or (event.message.text == "spice_bayleaf"):
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='ブレンドする量を選択してください',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1/2", text="spice_小さじ1/2")
                        ),
                    ])))
    if event.type == "message":
        if (event.message.text == "spice_blackpepper") or (event.message.text == "spice_tougarashi"):
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='ブレンドする量を選択してください',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1/2", text="spice_小さじ1/2")
                        ),
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1", text="spice_小さじ1")
                        ),
                    ])))
    if event.type == "message":
        if (event.message.text == "spice_greencardamon"):
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='ブレンドする量を選択してください',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1/2", text="spice_小さじ1/2")
                        ),
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1", text="spice_小さじ1")
                        ),
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ2", text="spice_小さじ2")
                        ),
                    ])))
    if event.type == "message":
        if (event.message.text == "spice_cumin") or (event.message.text == "spice_coriander"):
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                        text='ブレンドする量を選択してください',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1/2", text="spice_小さじ1/2")
                        ),
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ1", text="spice_小さじ1")
                        ),
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ2", text="spice_小さじ2")
                        ),
                                QuickReplyButton(
                                    action=MessageAction(label="小さじ4", text="spice_小さじ4")
                        ),
                    ])))
            


            
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
