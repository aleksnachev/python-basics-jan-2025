searched_book = input()
counter = 0
is_it_found = False
while True:
    book = input()

    if book == "No More Books":
        break

    if book == searched_book:
        print(f"You checked {counter} books and found it.")
        is_it_found = True
        break
    counter += 1
if is_it_found == False:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
