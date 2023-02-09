#Topic - Consumer

from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected')

    def websocket_receive(self, event):
        print('message received')

    def websocket_disconnect(self, event):
        print('websocket disconnected')

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('websocket connected')

    async def websocket_receive(self, event):
        print('message received')
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected')