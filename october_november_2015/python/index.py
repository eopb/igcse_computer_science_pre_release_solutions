import time

MAX_SAFE_TEMP = 37.5
MIN_SAFE_TEMP = 36.0


def monitor_baby_regular():
    while True:
        temperature = input("What is the babies temperature: ")
        try:
            temperature = float(temperature)
        except:
            print("Please only input numbers")
            continue
        if temperature <= MIN_SAFE_TEMP:
            print("The baby is too cold.")
        if temperature > MAX_SAFE_TEMP:
            print("The baby is at too hot.")
        else:
            print("The baby is at safe temperature.")
        # change time to 10 min
        time.sleep(60)


def monitor_baby_regular_array():
    three_hours_from_now = time.time() + (3 * 60 * 60)
    # three_hours_from_now = time.time() + 20
    temperatures = []
    while time.time() < three_hours_from_now:
        temperature = input("What is the babies temperature: ")
        try:
            temperature = float(temperature)
        except:
            print("Please only input numbers")
            continue
        temperatures.append(temperature)
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    temp_range = highest_temp - lowest_temp
    print("The highest temperature was " + str(highest_temp))
    print("The lowest temperature was " + str(lowest_temp))
    print("The temperature range was " + str(temp_range))

def monitor_baby_regular_array_warn():
    # three_hours_from_now = time.time() + (3 * 60 * 60)
    three_hours_from_now = time.time() + 20
    temperatures = []
    while time.time() < three_hours_from_now:
        temperature = input("What is the babies temperature: ")
        try:
            temperature = float(temperature)
        except:
            print("Please only input numbers")
            continue
        temperatures.append(temperature)
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    temp_range = highest_temp - lowest_temp
    print("The highest temperature was " + str(highest_temp))
    print("The lowest temperature was " + str(lowest_temp))
    print("The temperature range was " + str(temp_range))
    if temp_range > 1:
        print("Temperature changed by more than 1 degree.")
    times_out_of_range = 0
    for temperature in temperatures:
        if (temperature <= MIN_SAFE_TEMP) or (temperature > MAX_SAFE_TEMP):
            times_out_of_range += 1
    if times_out_of_range > 2:
        print("Temperature went out of range more than two times.")


monitor_baby_regular_array()