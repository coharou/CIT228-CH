def ShowMessages(msg):
    for text in msg:
        print(text)

def SendMessages(msg):
    sent_messages = []
    for text in msg:
        print(text)
        sent_messages.append(text)
    return sent_messages