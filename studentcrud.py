import psycopg2


def db_connection():
    DB_NAME = "postgres"
    DB_USER = "postgres.rfzedwblbbhnapxqobgn"
    DB_PASSWORD = "KittyCatMeowMeow@123"
    DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
    DB_PORT = "5432"

    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print(conn)
        return conn
    except Exception as e:
        print("Error connection to database")
        return None
    
def create_table_teacher():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher(
            id SERIAL PRIMARY KEY,
            name VARCHAR(90) NOT NULL,
            age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table teacher created")


def create_table_courses():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            teacher_id INT REFERENCES teacher (id) ON DELETE CASCADE,
            credits INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table courses created")


def create_table_student():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            course_id INT REFERENCES courses (course_id) ON DELETE CASCADE,
            age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table students created")
    
    
def create_table_enrollments():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
            grade VARCHAR(2) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table enrollments created")
    
    
def insert_teacher(id, name, age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teacher (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted to teacher table")
    
def insert_courses(course_id, course_name, credits, teacher_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_id, course_name, credits, teacher_id) VALUES (%s, %s, %s, %s)", (course_id, course_name, credits, teacher_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted table courses")
    
def insert_student(name, course_id, age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (name, course_id, age) VALUES (%s, %s, %s)", (name,course_id, age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted to table student")
    
def insert_enrollments(enrollment_id, grade, student_id, course_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments (enrollment_id, grade, student_id, course_id) VALUES (%s, %s, %s, %s)", (enrollment_id, grade, student_id, course_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted to enrollments")
    
def update_teacher(name, id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE teacher SET name = %s WHERE id = %s RETURNING id", (name, id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Updated")
    
def delete_teacher(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Deleted")

if __name__ == "__main__":
    insert_enrollments(543, '12', 3, 1002)
