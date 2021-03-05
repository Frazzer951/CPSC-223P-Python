import random

series = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"]


def get_winning_ticket_number():
    winning_ticket = ""
    winning_ticket += random.choice(series[:10])
    winning_ticket += random.choice(series[:10])
    winning_ticket += random.choice(series[:10])
    winning_ticket += random.choice(series[:10])
    winning_ticket += random.choice(series[10:])
    winning_ticket += random.choice(series[10:])
    winning_ticket += random.choice(series[10:])
    winning_ticket += random.choice(series[10:])
    return winning_ticket


winning_tickets = []

for i in range(10):
    winning_tickets.append(get_winning_ticket_number())

print("winning tickets:", winning_tickets)
