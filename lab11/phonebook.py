import csv
import psycopg2

conn=psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
    password="raikhan1", port=5432)
cur=conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS phone (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            number VARCHAR(20) NOT NULL
            )
        """ )

print("Hello! What do you want to do? (1-insert, 2-search, 3-insert many users, 4-records with pagination, 5-delete some data)")
answer=input()

def search_patterns(pattern):
    cur.execute("SELECT * FROM search_patterns(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def add_new_phone(name, surname, number):
    cur.execute("CALL add_new_phone(%s,%s,%s)", (name, surname, number))

def delete_data(data):
    cur.execute("CALL delete_data(%s)", (data,))

def insert_some_users(names, surnames, phones):
    cur.execute("CALL insert_some_users(%s,%s,%s)", (names, surnames, phones))

def records_pagination(lim, offs):
    cur.execute("SELECT * FROM records_pagination(%s, %s);", (lim, offs))
    return cur.fetchall()

def update_id():
    cur.execute("SELECT id FROM phone ORDER BY id")
    exs_ids = [row[0] for row in cur.fetchall()]
    for index, id in enumerate(exs_ids, start=1):
        cur.execute("UPDATE phone SET id = %s WHERE id = %s", (index, id))             

while True:
    if answer=="1":
        print("Do you want to insert some data? (yes/no): ")
        choice = input().lower()
        if choice != 'yes':
            break        
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        phone = input("Enter number: ")
        add_new_phone(name, surname, phone)
    elif answer=="2":
        pattern = input("Enter search pattern, or 'break' to stop: ")
        if pattern=="break":
            break
        search_patterns(pattern)
    elif answer=="3":
        print("Do you want to insert some records? (yes/no): ")
        choice = input().lower()
        if choice != 'yes':
            break 
        names = input("Enter list of names with commas: ").split(',')
        surnames = input("Enter list of surnames with commas: ").split(',')
        phones = input("Enter list of numbers with commas: ").split(',')  
        insert_some_users(names, surnames, phones)
    elif answer=="4":
        print("Do you want to query some data? (yes/no): ")
        choice = input().lower()
        if choice != 'yes':
            break  
        lim = int(input("Enter limit: "))
        offs = int(input("Enter offset: "))
        print(records_pagination(lim, offs))
    elif answer=="5":
        data = input("Enter Name or Surname or Number to delete, or 'break' to stop: ")
        if data=="break":
            break
        delete_data(data)

update_id()
conn.commit()
cur.close()
conn.close()

