'''
Julian Patterson 2131249
420-LCU Computer Programming
Friday February 17, 2023
S. Hilal, instructor
Assignment 4
'''

MENU = """Welcome to My Top Books Club:
1- How many different languages are there? Print a number list of all languages.
2- What language has the most books?
3- Display all the books in a given language.
4- How many different types of books are there? Print a numbered list of all the types. Which type has most copies sold?
5- List all authors who have more than one book on the list.
6- List the top 10 authors based on the number of books they have authored.
7- For a given author, what is the total number of books sold?
8- List all books of a given type. 
9- What are the top 7 types of books based on total sold?
10- Display a pie chart plot to show the distribution of books among the top 7 types of books.
11- Exit
Please enter a selection: 
"""

Books = {}
data = open("books.txt" , "r")

for entry in data.readlines():
    entry.split("\n")
    book_record = entry.split(",")
    keys = ["auth", "lang", "type", "sold"]
    book_record[-1] = int(book_record[-1])
    book_dict = dict(zip(keys, book_record[1:]))
    Books[book_record[0]] = book_dict

while True:
    selection = input(MENU)
    def Language_Dict():
        Languages = {}
        for value in Books.values():
            Languages[value["lang"]] += 1
        return Languages



    if selection == "1":
        Languages = dict()


    if selection == "2":
        break

    if selection == "3":
        break 

    if selection == "4":
        break 

    if selection == "5":
        break 

    if selection == "6":
        break 

    if selection == "7":
        break 

    if selection == "8":
        break 

    if selection == "9":
        break 

    if selection == "10":
        break 

    if selection == "11":
        break 

    else:
        print("Please enter a valid selection.")

