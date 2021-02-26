def send_messages(messages):
    sent_messages = []
    while len(messages) > 0:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    return sent_messages


messages = [
    "This is a message",
    "There are many like it",
    "But they are not this message",
    "For this message is a message",
]
messages_copy = messages.copy()
sent_messages = send_messages(messages_copy)

print("\nMessages")
print(messages)
print("\nMessages Copy")
print(messages_copy)
print("\nSent Messages")
print(sent_messages)