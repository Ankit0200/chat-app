import json
import time

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from .models import *

class MySyncConsumer(SyncConsumer):


    # THIS IS CALLED WHEN THE WEBSOCKET IS FORMED.
    def websocket_connect(self, event):
        print(" Websocket connected")
        self.send({
            'type': 'websocket.accept',

        })
        # print("Channel Layer .......",self.channel_layer)
        # print("Channel Layer .......", self.channel_name)
        # ADD CHANNEL TO NEW OR EXISTING GROUP.

        # TO GET THE GROUP NAME DO THE FOLLOWING

        print(self.scope['url_route']['kwargs']['groupname'])
        self.group= self.scope['url_route']['kwargs']['groupname']

        async_to_sync(self.channel_layer.group_add)(self.group, self.channel_name)

    # THIS IS CALLED WHEN THE DATA IS RECEIVED FROM THE CLIENT.

    def websocket_receive(self, event):

        # print(f"Received message is ", event['text'])
        data=json.loads(event['text'])
        # print(data)
        # print(data['msg'])
        group=Group.objects.get(name=self.group)
        
        # CREATE NEW CHAT OBJECT
        chatt=chat.objects.create(message=data['msg'],group=group)



        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'chat.message',
                'message': event['text']
            }
        )

    # THIS METHOD HANDLES THE MESSAGE RECEIVED FROM THE GROUP.
    def chat_message(self, event):
        print(event)
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    # THIS IS CALLED WHEN CONNECTION IN DISCONNECTED.

    def websocket_disconnect(self, event):
        # print("Websocket disconnected")
        # print("Channel Layer .......", self.channel_layer)
        # print("Channel Name...............",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)("Programmers", self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    # THIS IS CALLED WHEN THE WEBSOCKET IS FORMED.
    async def websocket_connect(self, event):
        await self.send({
            'type': 'websocket.accept'
        })
        print(" Websocket connected")

    # THIS IS CALLED WHEN THE DATA IS RECEIVED FROM THE CLIENT.

    async def websocket_receive(self, event):
        print(" Websocket received")

    # THIS IS CALLED WHEN CONNECTION IN DISCONNECTED.

    async def websocket_disconnect(self, event):
        print("Websocket disconnected")
