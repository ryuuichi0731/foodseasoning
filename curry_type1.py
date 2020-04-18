
from linebot.models import (
    ImagemapArea,
    ImagemapSendMessage,
    URIImagemapAction,
    MessageImagemapAction,
    Video, BaseSize, ExternalLink,
)

#ここからーーー ーーー 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == “message”:
        if event.message.type == “curryメニュー”:
            
            imagemap_message = ImagemapSendMessage(
                base_url='https://currytype01.fc2.net/',
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
