min_control = int(input())
sec_control = int(input())
distance = float(input())
sec_per_100_m = int(input())

time_control_in_seconds = min_control * 60 + sec_control
times_shortened = (distance / 120) * 2.5
time = (distance/100) * sec_per_100_m - times_shortened

if time <= time_control_in_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {(time - time_control_in_seconds):.3f} second slower.")