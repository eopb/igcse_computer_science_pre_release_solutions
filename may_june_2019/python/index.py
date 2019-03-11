import itertools
from statistics import mean


class Row(object):
    def __init__(self, date, bus_punctuality):
        self.date = date
        self.bus_punctuality = bus_punctuality


default_data = [
    Row(date="Mon1", bus_punctuality=[0, 0,  2, 1, -1, 0]),
    Row(date="Tue1", bus_punctuality=[0, 1,  0, 0, -1, -5]),
    Row(date="Wed1", bus_punctuality=[0, 0, -1, 0, -1, -5]),
    Row(date="Thu1", bus_punctuality=[2, 0, -1, 0, -2, -5]),
    Row(date="Fri1", bus_punctuality=[2, 1, -2, 0, -4, -4]),
    Row(date="Mon2", bus_punctuality=[4, 2, -2, 0, -1, -3]),
    Row(date="Tue2", bus_punctuality=[0, 0, -3, 0, -2, -5]),
    Row(date="Wed2", bus_punctuality=[3, 0, -1, 0,  0, 0]),
    Row(date="Thu2", bus_punctuality=[4, 0,  0, 0,  0, 0]),
    Row(date="Fri2", bus_punctuality=[-2, 0,  0, 0,  0, 0]),
    Row(date="Mon3", bus_punctuality=[-5, 1, -2, 2,  0, 0]),
    Row(date="Tue3", bus_punctuality=[0, 0,  0, 0,  1, -2]),
    Row(date="Wed3", bus_punctuality=[0, 0,  1, 0,  2, -3]),
    Row(date="Thu3", bus_punctuality=[3, 0,  1, 0, -3, 1]),
    Row(date="Fri3", bus_punctuality=[4, 2,  1, 0,  1, 1]),
    Row(date="Mon4", bus_punctuality=[-1, 0,  1, 0,  1, 1]),
    Row(date="Tue4", bus_punctuality=[8, 0, -1, 0,  3, 0]),
    Row(date="Wed4", bus_punctuality=[1, 1, -1, 0, -1, 0]),
    Row(date="Thu4", bus_punctuality=[1, 0,  2, 0,  0, -2]),
    Row(date="Fri4", bus_punctuality=[-2, 0, -2, 0,  0, -5]),
]

# think this is not correct


def number_late_arrivals(bus_data):
    number_late_arrivals = list(
        itertools.repeat(0, len(bus_data[0].bus_punctuality)))
    for day in bus_data:
        for i, bus_time in enumerate(day.bus_punctuality, start=0):
            if bus_time < 0:
                number_late_arrivals[i] += 1
    return number_late_arrivals.index(max(number_late_arrivals))


def avarge_minutes_late_per_bus(bus_data):
    avarge_number_of_minutes_late = []
    for bus_number in range(len(bus_data[0].bus_punctuality)):
        lateness = []
        for day in bus_data:
            lateness.append(day.bus_punctuality[bus_number] * -1)
        avarge_number_of_minutes_late.append(mean(lateness))
    return avarge_number_of_minutes_late


def avarge_minutes_late_per_late_bus(bus_data):
    avarge_number_of_minutes_late = []
    for bus_number in range(len(bus_data[0].bus_punctuality)):
        lateness = []
        for day in bus_data:
            bus_latness = day.bus_punctuality[bus_number] * -1
            if bus_latness > 0:
                lateness.append(bus_latness)
        if lateness == []:
            avarge_number_of_minutes_late.append(0)
        else:
            avarge_number_of_minutes_late.append(mean(lateness))
    return avarge_number_of_minutes_late


def bus_route_most_days_late(bus_data):
    number_of_times_late = []
    for bus_number in range(len(bus_data[0].bus_punctuality)):
        times_late = 0
        for day in bus_data:
            if day.bus_punctuality[bus_number] < 0:
                times_late += 1
        number_of_times_late.append(times_late)
    return number_of_times_late.index(max(number_of_times_late))


def specific_day(bus_data):
    while True:
        input_var = input("What day do you want data on: ")
        for day in bus_data:
            if day.date == input_var:
                return day
        print("Error no data for that date")


def number_of_busses_late_for_day(bus_data):
    day = specific_day(bus_data)
    number_late = 0
    for bus_punctuality in day.bus_punctuality:
        if bus_punctuality < 0:
            number_late += 1
    return number_late


print(number_of_busses_late_for_day(default_data))
