from db_connect_ebook import *

# q_1 = cursor.execute("SELECT * FROM ebook_list").fetchall()
# print(q_1)

def retrieve_book_data():
    table = (cursor.execute("SELECT * FROM ebook_list"))

    for column in table:

        print((f"{column[0]} title: {column[1]} - Author: {column[2]}: - Date: {column[3]} "))

# print(retrieve_book_data())


# def retrieve_book_data():
#     query_entry = (cursor.execute("SELECT * FROM ebook_list"))
#     while True:
#         record = query_entry.fetchone()
#         if record is not None:
#             return (f"1) title: {record[1]} - Author: {record[2]}: - Date: {record[3]} ")
#         elif record is None:
#             break



def title_search(input_title):
    title = cursor.execute(f"SELECT * FROM ebook_list WHERE [Book Title] = '{input_title}'").fetchone()
    return title


def add_book_to_db(title, author, date):
    cursor.execute(f"INSERT INTO ebook_list VALUES ('{title}', '{author}', '{date}')")
    conn_ebdb.commit()