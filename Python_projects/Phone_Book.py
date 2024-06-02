def create_phone_book(n):
    phone_book = {}
    for _ in range(n):
        name, number = input().split()
        phone_book[name] = number
    return phone_book

def query_phone_book(phone_book):
    while True:
        try:
            name = input()
            if name in phone_book:
                print(f"{name}={phone_book[name]}")
            else:
                print("Not found")
        except EOFError:
            break

if __name__ == "__main__":
    n = int(input())
    phone_book = create_phone_book(n)
    query_phone_book(phone_book)