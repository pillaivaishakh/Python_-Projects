def classify_money(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for note in notes:
        count = amount // note
        print(f"{note} Rs. notes : {count}")
        amount %= note

if __name__ == "__main__":
    try:
        amount = int(input("Enter an integer value:\n"))
        classify_money(amount)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
