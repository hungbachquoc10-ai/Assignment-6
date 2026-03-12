def great_numbers():
    numbers = []
    print("Enter numbers one by one(Press Enter on an empty line to finish).")
    while True:
        input_value = input("Enter a number: ")
        if input_value == "":
            break
        try:
            x = float(input_value)
            numbers.append(x)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    numbers.sort(reverse=True)
    top_5 = numbers[:5]
    print(" Results: ")
    if top_5:
        print("The five greatest numbers (descending):")
        for i in top_5:
            print(i)
    else:
        print("No numbers were entered.")       
if __name__ == "__main__":  
    great_numbers()