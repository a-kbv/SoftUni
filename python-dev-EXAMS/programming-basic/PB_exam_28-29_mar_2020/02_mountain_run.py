import math
record = float(input())
distance = float(input())
time_for_m = float(input())

time_needed = distance * time_for_m
decelleration = (math.floor(distance / 50)) * 30
total_time = time_needed + decelleration

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record:.2f} seconds slower.")