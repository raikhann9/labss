import csv
import psycopg2
from config import load_config

def insert_data():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            while True:
                with conn.cursor() as cur:
                    print("\n1) Insert data from console")
                    print("2) Insert data from CSV file")
                    answer = input("Choose an option (1/2): ")
                    if answer == "1":
                        name = input("Enter name: ")
                        surname = input("Enter surname: ")
                        number = input("Enter number: ")
                        cur.execute("INSERT INTO PhoneBook (name, surname, number) VALUES (%s, %s, %s)", (name, surname, number))
                        conn.commit()
                    elif answer == '2':
                        csv_file = "phonebook.csv"
                        with open(csv_file, 'r') as file:
                            reader = csv.reader(file)
                            next(reader)  
                            for row in reader:
                                cur.execute("INSERT INTO PhoneBook (name, surname, number) VALUES (%s, %s, %s)", row)
                            conn.commit()
                    else:
                        print("Invalid option. Please choose either 1 or 2.")

                continue_input = input("Do you want to enter more data? (yes/no): ").lower()
                if continue_input != 'yes':
                    break  
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

if __name__ == '__main__':
    insert_data()


