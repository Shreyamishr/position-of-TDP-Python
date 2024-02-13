import mysql.connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shreya@01",
            database="shreya"
        )
        print("Connected to MySQL database successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Create database, table, and columns if they don't exist
def create_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                age INT,
                grade FLOAT
            )
        """)
        print("Table 'students' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

# Insert a new student record
def insert_student(cursor):
    try:
        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES ('Alice', 'Smith', 18, 95.5)
        """)
        print("New student record inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error inserting student record: {err}")

# Update the grade of the student named Alice
def update_student_grade(cursor):
    try:
        cursor.execute("""
            UPDATE students
            SET grade = 97.0
            WHERE first_name = 'Alice'
        """)
        print("Grade updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error updating grade: {err}")

# Delete the student with last name "Smith"
def delete_student(cursor):
    try:
        cursor.execute("""
            DELETE FROM students
            WHERE last_name = 'Smith'
        """)
        print("Student record deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error deleting student record: {err}")

# Fetch and display all student records
def fetch_students(cursor):
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if students:
            print("Student Records:")
            for student in students:
                print(student)
        else:
            print("No student records found.")
    except mysql.connector.Error as err:
        print(f"Error fetching student records: {err}")

def main():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        create_table(cursor)
        insert_student(cursor)
        update_student_grade(cursor)
        delete_student(cursor)
        fetch_students(cursor)
        connection.commit()
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
