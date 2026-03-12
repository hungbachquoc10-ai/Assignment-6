def odds(numbers):
    return [num for num in numbers if num % 2 == 0]
def main():
    user_input = input("Enter a list of integers separated by spaces: ")
    try:
        original_list = [int(x) for x in user_input.split()]
        cut_down_list = odds(original_list)
        print(" Results:")
        print(f"Original List: {original_list}")
        print(f"Cut-down Listd (odds number deleted): {cut_down_list}")
    except ValueError:
        print("Error: Please only enter whole numbers separated by spaces.")
if __name__ == "__main__":
    main()