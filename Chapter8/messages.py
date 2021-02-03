#import messages_activity
#from messages_activity import ShowMessages, SendMessages
#from messages_activity import ShowMessages as ShowMsg, SendMessages as SendMsg
#from messages_activity import *
import messages_activity as msg_act

messages = ['Hi!', 'Hello', 'how r u?', 'im ok, u?']

print()
print('-- Original:')
msg_act.ShowMessages(messages)
print(messages)
print()
print('-- New:')
print(msg_act.SendMessages(messages))
print()