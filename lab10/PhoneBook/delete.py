import psycopg2
from config import load_config


def delete_phonebook(id):

    rows_deleted  = 0
    sql = 'DELETE FROM phonebook WHERE id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

if __name__ == '__main__':
    while True:
        print("Do you want to delete some data? (yes/no): ")
        choice = input().lower()
        if choice != 'yes':
            break
        
        id=input("Enter the ID: ")
        delete_phonebook(id)
