# EMAIL
class Email:
    def __init__(self, sender, reciever, content, is_sent = False):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_sent = is_sent
    def send(self):
        self.is_sent = True
    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}"

emails = []

data = input()
while not data == "Stop":
    sender, reciever, content = data.split(" ")
    email = Email(sender, reciever, content)
    emails.append(email)
    data = input()

send_emails = list(map(int, input().split(", ")))

for each in send_emails:
    emails[each].send()

for email in emails:
    print(email.get_info())