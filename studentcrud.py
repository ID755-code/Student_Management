import psycopg2



def db_connection():
    DB_NAME="postgres"
    DB_USER="postgres.rfzedwblbbhnapxqobgn"
    DB_PASSWORD="KittyCatMeowMeow@123"
    DB_HOST="aws-0-ap-southeast-1.pooler.supabase.com"
    DB_PORT="5432"

    try:
        
        conn=psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print(conn)
        return conn
    except Exception as e:
        print("Error connection to database")
        return None

def create_table_courses():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
                create table if not exists courses (
                course_id serial primary key,
                course_name varchar(100) not null,
                teacher_id int references teacher (id) on delete cascade,
                credits int not null)
                   """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table students created")


def create_table_students():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
                create table if not exists student (
                student_id serial primary key,
                name varchar(100) not null,
                course_id int references courses (course_id) on delete cascade,
                age int not null)
                   """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created")
    
    
def create_table_enrollments():
    conn=db_connection()
    cursor=conn.cursor()
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
    print("Table enrollemts created")
    
    
def insert_teacher(name, age):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO teacher (name, age) VALUES(%s, %s) RETURNING id", (name, age))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted")
    
def update_teacher(name, id):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE teacher  SET name= %s WHERE id= %s RETURNING id", (name, id) )
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Updated")
    
def delete_teacher(id):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE id = %s", (id,) )
    conn.commit()
    cursor.close()
    conn.close()
    print("Data deleted")

if __name__=="__main__":
    create_table_courses()
    create_table_students()
    create_table_enrollments()