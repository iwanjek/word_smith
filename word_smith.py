import datetime
import os
import sys
import json


def write_card_to_file(book_card,file):
    json.dump(book_card, file, indent = 2)


def create_book_card(book_card, initial_card,file):
    """
    Book Title
    Author
    Passage
    Page Number
    Date It was Saved to File
    """
    time = datetime.datetime.now()
    time = time.strftime('%m/%d/%Y %H:%M:%S')

    if initial_card:
        book_card["type"] = 'b'
        book_card["book_title"] = input("Enter book title: ")
        book_card["author"] = input("Enter author: ")
        book_card["passage"] = input("Enter passage: ")
        book_card["pg_num"] = input("Enter page number: ")
        book_card["system_date"] = time

    else:
        book_card["passage"] = input("Enter passage: ")
        book_card["pg_num"] = input("Enter page number: ")
        book_card["system_date"] = time

    write_card_to_file(book_card,file)
    add_more =input("Enter '1' to add cards from the same book\nEnter '2' to add cards from a different book\nEnter '3' to add another type of card\nEnter any other key to quit\n")

    if(add_more == '1'):
        create_book_card(book_card,False,file)
    elif(add_more == '2'):
        create_book_card(book_card,True,file)
    elif(add_more == '3'):
        create_index_card(file)
    else:
        exit()


def create_index_card(file):
    card_type = input("Enter 'b' for book: ")

    if card_type == 'b':
        book_card = {}
        create_book_card(book_card,True,file)
    else:
        print("Sorry but only books quotes are supported as of now.")


def create_path_and_file():
    catalog_path = sys.argv[1]
    catalog_file_name = sys.argv[2]
    filepath = os.path.join(catalog_path, catalog_file_name)

    if not os.path.exists(catalog_path):
        os.makedirs(catalog_path)
    f = open(catalog_file_name, "w+")

    return f

def main():

    f = create_path_and_file()
    create_index_card(f)


main()
