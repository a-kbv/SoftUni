climbers = int(input())
musala = 0
monblan = 0
kilimandzharo = 0
k2 = 0
everest = 0
total_count = 0


for climber in range(1, climbers+1):
    num = int(input())
    total_count += num
    if num <= 5:
        musala += num
    elif num >=6 and num <=12:
        monblan += num
    elif num >=13 and num <=25:
        kilimandzharo +=num
    elif num >=26 and num <=40:
        k2 += num
    else:
        everest += num
print(f"{musala/total_count*100:.2f}%")
print(f"{monblan/total_count*100:.2f}%")
print(f"{kilimandzharo/total_count*100:.2f}%")
print(f"{k2/total_count*100:.2f}%")
print(f"{everest/total_count*100:.2f}%")