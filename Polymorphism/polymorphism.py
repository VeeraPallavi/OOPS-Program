class Messenger:

    def use_keyboard(self):
        print("Using Keyboard")
    
    def send_message(self):
        print("text mesage sent")
    
    def receive_message(self):
        print("text message received")
    
class WhatsApp(Messenger):

    def send_message(self):
        print("Text, video & audio sent using WA")
    
    def receive_message(self):
        print("Text, video, audio received using WA")
    
    def send_live_loation(self):
        print("Live location sent")

class FaceBook(Messenger):

    def send_message(self):
        print("Text, video & audio sent using FB")
    
    def receive_message(self):
        print("Text, video, audio received using FB")
    
    def use_builtin_apps(self):
        print("Using builtin apps")
class InstaMessenger(Messenger):

    def send_message(self):
        print("Text, video & audio sent using IM")
    
    def receive_message(self):
        print("Text, video, audio received using IM")
    
    def add_filters(self):
        print("Filters using insta")

def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()
    if type(ref) == WhatsApp:
        ref.send_live_loation()
    if type(ref) == FaceBook:
        ref.use_builtin_apps()
    if type(ref) == InstaMessenger:
        ref.add_filters()

wa = WhatsApp()
fb = FaceBook()
im = InstaMessenger()

use_messenger(wa)
use_messenger(fb)
use_messenger(im)

