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

sent_messages = send_messages(messages)

print("\nMessages")
print(messages)
print("\nSent Messages")
print(sent_messages)