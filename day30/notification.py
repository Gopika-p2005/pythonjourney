class Notification:

    def send(self,message):

        print("sending notification",message)

class Email(Notification):

    def send(self,message):

        print("sending notification via email",message)

class WhatsApp(Notification):

    def send(self,message):

        print("sending notification via wa",message)

email_instance=Email()

email_instance.send("you have an interview tomorrow")

wa_instance=WhatsApp()

wa_instance.send("you have an interview tomorrow")