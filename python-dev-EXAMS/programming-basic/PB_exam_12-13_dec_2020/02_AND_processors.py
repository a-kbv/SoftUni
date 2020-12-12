import math

def processorrs_profit():
    needed_processor_count = int(input())
    personal = int(input())
    working_days = int(input())

    work_hours = personal * working_days * 8
    processors_made = math.floor(work_hours / 3)

    if processors_made >= needed_processor_count:
        profit = processors_made - needed_processor_count
        return f"Profit: -> {(profit * 110.10):.2f} BGN"
    else:
        loses = needed_processor_count - processors_made
        return f"Losses: -> {(loses * 110.10):.2f} BGN"

print(processorrs_profit())