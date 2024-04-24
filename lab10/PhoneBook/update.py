import psycopg2
from config import load_config


def update_phonebook(id, name):

    updated_row_count = 0

    sql = """ UPDATE PhoneBook
                SET name = %s
                WHERE id = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                cur.execute(sql, (name, id))
                updated_row_count = cur.rowcount

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

def update_id():
    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM PhoneBook ORDER BY id")
                existing_ids = [row[0] for row in cur.fetchall()]

                for index, id in enumerate(existing_ids, start=1):
                    cur.execute("UPDATE PhoneBook SET id = %s WHERE id = %s", (index, id))             
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    while True:
        print("Do you want to update a phonebook? (yes/no): ")
        choice = input().lower()
        if choice != 'yes':
            break
        
        id = input("Enter the ID: ")
        name = input("Enter the new name: ")
        update_phonebook(id, name)
    update_id()