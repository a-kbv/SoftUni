moment = input()
ticket_type = input()
ticket_count = int(input())
trophy_photo = input()
ticket_price = 0

if moment == "Quarter final":
    if ticket_type == 'Standard':
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90

if moment == "Semi final":
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40

if moment == "Final":
    if ticket_type == 'Standard':
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

sum = ticket_price * ticket_count

if sum > 4000:
    sum *= 0.75
    trophy_photo = "N"
elif sum > 2500:
    sum *= 0.9
if trophy_photo == "Y":
    sum += 40 * ticket_count

print(f"{sum:.2f}")