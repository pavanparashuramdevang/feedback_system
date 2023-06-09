from db_connect import Connector


class Student_table():

    def __init__(self):
        self.connector=Connector()
        self.cursor=self.connector.get_cursor()
        self.create_student_table()

    def create_student_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS student(
            usn VARCHAR(12) NOT NULL,
            email VARCHAR(256),
            PRIMARY KEY(usn)
            );
            """)
            self.commit()
            print("SUCCESS :) student table is avilable")

        except:
            print("ERROR :( student table may already exists")

    
    def add_student(self,usn,email):
        sql="""
        INSERT INTO student(usn,email)
        VALUES (%s,%s)
        ON DUPLICATE KEY UPDATE
        email=%s;
        """
        usn=usn.upper()
        email=email
        val=(usn,email,email)
        try:
            self.cursor.execute(sql,val)
            self.connector.commit()
            print("student added or updated")

        except:
            print("student not ableto update/add ")

    def get_email(self,usn):
        try:
            sql="""
            SELECT email FROM student
            WHERE usn=%s;
            """
            usn=usn.upper()
            val=(usn,)
            self.cursor.execute(sql,val)
            email=self.cursor.fetchone()

            if email=="" or email==None:
                return None
            else:
                return email
        except:
            return None
        
if __name__=="__main__":
    student=Student_table()
    student.add_student('4HG19CS001','abc@gmail.com')
    student.add_student('4HG19CS028','pavanparashuramdevang@gmail.com')
    print(student.get_email('4hg19cs022'))