from __future__ import unicode_literals, absolute_import

import json
import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    ImagemapSendMessage, BaseSize, URIImagemapAction,
    ImagemapArea, MessageImagemapAction, ExternalLink
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.imagemap_message = ImagemapSendMessage(
            base_url='https://baseurl.com/image/ct01',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=453, width=1040),
            
            @handler.add(MessageEvent, message=TextMessage)
            def handle_message(event):
            if event.type == "message":
                if event.message.type == "text":
            
                actions=[
                    MessageImagemapAction(
                        text='hello',
                        area=ImagemapArea(
                            x=40, y=56, width=313, height=340
                        )
                    ),
                    MessageImagemapAction(
                        text='hello',
                        area=ImagemapArea(
                            x=363, y=59, width=314, height=337
                        )
                    ),
                    MessageImagemapAction(
                        text='hello',
                        area=ImagemapArea(
                            x=690, y=60, width=317, height=335
                        )
                    )
                ]
            )

            self.message = [{
                "type": "imagemap",
                "baseUrl": "https://example.com/base",
                "altText": "this is an imagemap",
                "baseSize": {
                    "height": 453,
                    "width": 1040
                },
            
                "actions": [
                    {
                        "type": "uri",
                        "text": "hello",
                        "area": {
                            "x": 40,
                            "y": 56,
                            "width": 313,
                            "height": 340
                        }
                    },
                    {
                        "type": "message",
                        "text": "hello",
                        "area": {
                            "x": 363,
                            "y": 59,
                            "width": 314,
                            "height": 337
                        }
                    },
                    {
                        "type": "message",
                        "text": "hello",
                        "area": {
                            "x": 690,
                            "y": 60,
                            "width": 317,
                            "height": 335
                        }
                    }
                ]
            }]

        @responses.activate
        def test_push_imagemap_message(self):
            responses.add(
                responses.POST,
                LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
                json={}, status=200
            )

            self.tested.push_message('to', self.imagemap_message)

            request = responses.calls[0].request
            self.assertEqual(request.method, 'POST')
            self.assertEqual(
                request.url,
                LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push')
            self.assertEqual(
                json.loads(request.body),
                {
                    "to": "to",
                    'notificationDisabled': False,
                    "messages": self.message
                }
            )

        @responses.activate
        def test_reply_imagemap_message(self):
            responses.add(
                responses.POST,
                LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
                json={}, status=200
            )

            self.tested.reply_message('replyToken', self.imagemap_message)

            request = responses.calls[0].request
            self.assertEqual(request.method, 'POST')
            self.assertEqual(
                request.url,
                LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
            self.assertEqual(
                json.loads(request.body),
                {
                    "replyToken": "replyToken",
                    'notificationDisabled': False,
                    "messages": self.message
                }
            )

        @responses.activate
        def test_multicast_imagemap_message(self):
            responses.add(
                responses.POST,
                LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
                json={}, status=200
            )

            self.tested.multicast(['to1', 'to2'], self.imagemap_message)

            request = responses.calls[0].request
            self.assertEqual(request.method, 'POST')
            self.assertEqual(
                request.url,
                LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
            self.assertEqual(
                json.loads(request.body),
                {
                    "to": ['to1', 'to2'],
                    'notificationDisabled': False,
                    "messages": self.message
                }
            )


    if __name__ == '__main__':
        unittest.main()
