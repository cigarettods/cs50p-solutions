def main():
    mealtime = input("What time is it? ")
    if 7 <= convert(mealtime) <= 8:
        print("breakfast time")
    elif 12 <= convert(mealtime) <= 13:
        print("lunch time")
    elif 18 <= convert(mealtime) <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    amount = (float(hours) * 60 + float(minutes)) / 60
    return amount

if __name__ == "__main__":
    main()
