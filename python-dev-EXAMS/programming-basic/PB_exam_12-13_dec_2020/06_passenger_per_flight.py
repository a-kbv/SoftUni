from math import *
def passengers_on_flight():
    company_dict = {}

    for _ in range(int(input())):

        company_name = input()
        flight_count = 0
        passengers_count = 0

        data = input()
        while not data == "Finish":
            passengers_count += int(data)
            flight_count += 1

            data = input()

        avg_pass = floor(passengers_count / flight_count)

        company_dict[company_name] = avg_pass

    for key, value in company_dict.items():
        print(f"{key}: {value} passengers.")

    maximum = max(company_dict, key=company_dict.get)
    print(f"{maximum} has most passengers per flight: {company_dict[maximum]}")

passengers_on_flight()