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


monitor_baby_regular()
