from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class CompaniesListConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'companies_list'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def reload_page(self, event):
        # Send message to WebSocket
        reload_page = event['reload_page']

        self.send(text_data=json.dumps({
            'reload_page': reload_page
        }))
