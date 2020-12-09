country = input()
tool = input()
score = 0
total_score = 20

if country == 'Russia':
    if tool == 'ribbon':
        score = 9.1 +9.4
    elif tool == "hoop":
        score = 9.3 + 9.8
    else:
        score = 9.6 + 9

elif country == 'Bulgaria':
    if tool == 'ribbon':
        score = 9.6 +9.4
    elif tool == 'hoop':
        score = 9.55 + 9.75
    else:
        score = 9.50 + 9.40

elif country == 'Italy':
    if tool == 'ribbon':
        score = 9.2 +9.5
    elif tool == 'hoop':
        score = 9.45 + 9.35
    else:
        score = 9.7 + 9.15

print(f"The team of {country} get {score:.3f} on {tool}.")
print(f"{((20-score)/20 * 100):.2f}%")