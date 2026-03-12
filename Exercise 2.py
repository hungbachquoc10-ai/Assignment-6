the_season = ("winter", "spring", "summer", "autumn")
the_month = input("Enter the number of a month (1-12): ")
try:
    month = int(the_month)
    if 1 <= month <= 12:
        index = (month % 12) // 3
        print(f"Month {month} is in {the_season[index]}.")
    else:
        print("Please enter a number between 1 and 12.") 
except ValueError:
    print("Invalid input. Please enter a whole number.")
