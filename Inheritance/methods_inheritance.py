class Messenger:
    def send_message(self):
        print("Text message is sent")
    
    def receive_message(self):
        print("Text message is received")

class InternalMessenger(Messenger):
    pass

class WhatsAppMessenger(Messenger):

    def send_message(self):
        print("Text, phots, videos and Files is Sent")
    
    def receive_message(self):
        print("Text, photos, videos, Files is received")
    
    def set_dp(self):
        print("DP is set ")
    
    def set_status(self):
        print("Status is set")

im = InternalMessenger()
im.send_message()

wm = WhatsAppMessenger()
wm.send_message()
wm.set_status()