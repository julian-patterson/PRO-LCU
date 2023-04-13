'''
Julian Patterson 2131249
420-LCU Computer Programming
S. Hilal, instructor
Lab 12
'''

Books = {}
data = open("books.txt" , "r")

for entry in data.readlines():
    entry.split("\n")
    book_record = entry.split(",")
    keys = ["auth", "lang", "type", "sold"]
    book_record[-1] = int(book_record[-1])
    book_dict = dict(zip(keys, book_record[1:]))
    Books[book_record[0]] = book_dict

x = "{:50s} {:20s}"
for entry in sorted(Books):
    print(x.format(str(entry), str(Books[entry])))
