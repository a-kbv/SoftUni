tickets = [t.strip() for t in (input().split(", "))]
winning_symbols = ['@', '$', '#', '^']

def is_jackpot(ticket):
    left_side = ticket[0:10]
    right_side = ticket[10:20]

    if not left_side == right_side:
        return False
    for win_sym in winning_symbols:
        if win_sym * 10 == left_side:
            print(f'ticket "{ticket}" - 10{win_sym} Jackpot!')
            return True
    return False

def is_winningticket(ticket):
    left_side = ticket[0:10]
    right_side = ticket[10:20]

    for win_sym in winning_symbols:
        if win_sym * 6 in left_side and win_sym * 6 in right_side:
            count_left = left_side.count(win_sym)
            count_right = right_side.count(win_sym)
            count = min(count_left, count_right)
            print(f'ticket "{t}" - {count}{win_sym}')
            return True
    return False

for t in tickets:
    # IF NOT 20
    if not len(t) == 20:
        print(f"invalid ticket")
        continue
    # JACKPOT
    if is_jackpot(t):
        continue
    if is_winningticket(t):
        continue
    print(f'ticket "{t}" - no match')
