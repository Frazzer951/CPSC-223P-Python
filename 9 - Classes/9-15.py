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

num_tries = 0
while True:
    num_tries += 1
    lotto_num = get_winning_ticket_number()
    if lotto_num in winning_tickets:
        break

print("\nnumber_of_tries to win:", num_tries)

print("\npossible winner:", lotto_num)
