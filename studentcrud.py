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

def create_tables():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS enrollments(
                    enrollment_id SERIAL PRIMARY KEY,
                    teacher_id INT REFERENCES teacher (id) ON DELETE CASCADE,
                    grade VARCHAR(2))
                   """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created")
    
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
    create_tables()