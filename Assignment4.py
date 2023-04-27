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
Please enter a selection: """

Books = {}
data = open("books.txt", "r")

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
        Languages = []
        Dict = {}
        for value in Books.values():
            Languages.append(value["lang"])
        for language in sorted(Languages):
            if language in Dict:
                Dict[language] += 1
            else:
                Dict[language] = 1
        return Dict
    
    def Sold_Dict():
        Dict = {}
        for value in Books.values():
            if value["type"] in Dict:
                Dict[value["type"]] += value["sold"]
            else:
                Dict[value["type"]] = value["sold"]
        return Dict

    def Type_Dict():
        Types = []
        Dict = {}
        for value in Books.values():
            Types.append(value["type"])
        for type in sorted(Types):
            if type in Dict:
                Dict[type] += 1
            else:
                Dict[type] = 1
        return Dict

    # TODO Formatted printing 
    def Auth_Dict():
        Auth = []
        Dict = {}
        for value in Books.values():
            Auth.append(value["auth"])
        for auth in sorted(Auth):
            if auth in Dict:
                Dict[auth] += 1
            else:
                Dict[auth] = 1
        return Dict
    

    # TODO Numbered List?
    if selection == "1":
        language_list = []
        for key in Language_Dict():
            language_list.append(key)
        print(language_list)
        print("\n")

    if selection == "2":
        print("This is language has the most sold books: " +
              max(Language_Dict(), key=Language_Dict().get) + "\n")

    # TODO Format Printing
    if selection == "3":
        selected_language = input(
            "Please enter a language to see all the books: ")
        for key, value in Books.items():
            if selected_language in str(Books):
                if selected_language in str(value):
                    print(str(key) + str(value))
            else:
                print("There is no such book in that language \n")
                break

    if selection == "4":
        print("There are " + str(len(Type_Dict())) + " different types of books")
        type_list = []
        for key in Type_Dict():
            type_list.append(key)
        print("These are all the different types " + str(type_list))
        print("This type has the most sold books: " +
              max(Type_Dict(), key=Type_Dict().get) + "\n")

    if selection == "5":
        auth_dict = {}
        for key, value in Auth_Dict().items():
            if value > 1:
                auth_dict[key] = value
        print(auth_dict)

    # TODO only got 7 authors with more than 1 {'C. S. Lewis': 2, 'Charles Dickens': 2, 'Dan Brown': 3, 'George Orwell': 2, 'J. K. Rowling': 7, 'J. R. R. Tolkien': 2, 'Suzanne Collins': 2}
    if selection == "6":
        top_authors = {}
        for key,value in sorted(Books.items()):
            top_authors[key] = value["sold"]
        for i in range(1, 11):
            for key,value in sorted(top_authors, key=top_authors.get):
                print(i + ". " + key + " with " + value + " copies sold.") 


    if selection == "7":
        total = 0
        selected_author = input(
            "Please enter an author to see the number of books sold: ")
        if selected_author in str(Books):
            for key,value in Books.items():
                if selected_author in str(value):
                    total += value["sold"]
            print(str(selected_author) + " has sold " + str(total) + " number of copies. \n")
        else:
            print(str(selected_author) + " does not exist in this database. Please be sure to spell the name correctly. \n")


    if selection == "8":
        type_list = []
        for key in Type_Dict():
            type_list.append(key)
        print("These are all the different types of books: " + str(type_list) + "\n")
        type_selection = input("Enter the type of books you would like to see: ")
        if type_selection in str(type_list):
            for key,value in Books.items():
                if type_selection in str(value):
                    print(str(key), str(value))
        else:
            print("This is not a valid type. \n")

    # TODO I need to redo this
    if selection == "9":
        Temp = []
        for key,value in sorted(Sold_Dict()):
            for i in range(1,8):
                print(i, ". " + str(key) + " with " + str(value) + " number of copies sold.")


    if selection == "10":
        break

    if selection == "11":
        break

    else:
        print("Please enter a valid selection.")
