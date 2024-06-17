# myapp/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class AnnouncementConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "announcement_group"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Send message to the group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'announcement_message',
                'message': message,
            }
        )

    def announcement_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
