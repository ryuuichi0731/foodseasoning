from __future__ import unicode_literals, absolute_import

import json
import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    ImagemapSendMessage, BaseSize, URIImagemapAction,
    ImagemapArea, MessageImagemapAction,
    Video, ExternalLink
)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == "message":
        if (event.message.type == "メニュー"):
            actions = []
            actions.append(MessageImagemapAction(
                  text = 'chicken_curry',
                  area = ImagemapArea(
                      x = 29, y = 60, width = 314, height = 338
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = 'green_curry',
                  area = ImagemapArea(
                      x = 359, y = 61, width = 316, height = 340
                  )
            ))
            actions.append(MessageImagemapAction(
                  text = 'keema_curry',
                  area = ImagemapArea(
                      x = 695, y = 58, width = 317, height = 344
                  )
            ))

            message = ImagemapSendMessage(
                base_url = 'https://' + request.host + '/imagemap/' + uuid.uuid4().hex, # prevent cache
                alt_text = '代替テキスト',
                base_size = BaseSize(height=460, width=1040),
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
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
