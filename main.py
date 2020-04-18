# -*- coding: utf-8 -*-
import sys
sys.path.append('./vendor')

import os
import uuid

from PIL import Image
import io

from flask import Flask, request, abort, send_file

from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, MessageImagemapAction, ImagemapArea, ImagemapSendMessage, BaseSize
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))


@app.route("/", methods=['POST'])
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
    if event.type == "message":
        if event.message.type == "text":
            actions = []
            actions.append(MessageImagemapAction(
                  text = '１',
                  area = ImagemapArea(
                      x = 31, y = 49, width = 322, height = 355
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = '２',
                  area = ImagemapArea(
                      x = 360, y = 49, width = 324, height = 365
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = '３',
                  area = ImagemapArea(
                      x = 689, y = 42, width = 316, height = 368
                  )
            ))
            
            message = ImagemapSendMessage(
                base_url = 'https://' + request.host + '/imagemap/' + uuid.uuid4().hex, # prevent cache
                alt_text = '代替テキスト',
                base_size = BaseSize(height=453, width=1040),
                actions = actions
            )
            line_bot_api.reply_message(event.reply_token, message)

@app.route("/imagemap//", methods=['GET'])
def imagemap(uniqid, size):
    img = Image.open("./imagemap.png")
    img_resize = img.resize((int(size), int(size)))
    img_io = io.BytesIO()
    img_resize.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.debug = True
    app.run()
