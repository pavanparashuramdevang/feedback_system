from db_connect import Connector


class Status_table():

    def __init__(self):
        self.connector=Connector()
        self.cursor=self.connector.get_cursor()
        self.create_status_table()

    def create_status_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback_status(
            usn VARCHAR(12) NOT NULL,
            status INTEGER DEFAULT 0,
            PRIMARY KEY(usn)
            );
            """)
            self.commit()
            print("SUCCESS :) feedback status table is avilable")

        except:
            print("ERROR :( feedback status table may already exists")

    
    def add_status(self,usn,status):
        sql="""
        INSERT INTO feedback_status(usn,status)
        VALUES (%s,%s)
        ON DUPLICATE KEY UPDATE
        status=%s;
        """
        usn=usn.upper()
        status=int(status)
        val=(usn,status,status)

        try:
            self.cursor.execute(sql,val)
            self.connector.commit()
            print("status added or updated")

        except:
            print("status not able to update or add")

    def get_status(self,usn):
        try:
            sql="""
            SELECT status FROM feedback_status
            WHERE usn=%s;
            """
            usn=usn.upper()
            val=(usn,)

            self.cursor.execute(sql,val)
            status=self.cursor.fetchone()
            status=status[0]

            return status
        
        except:
            return None
        





class Feedback_table():
    def __init__(self):
        self.connector=Connector()
        self.cursor=self.connector.get_cursor()
        self.create_feedback_table()

    def create_feedback_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback(
            feedback VARCHAR(1256) NOT NULL
            );
            """)
            self.commit()
            print("SUCCESS :) feedback table is avilable")

        except:
            print("ERROR :( feedback table may already exists")

    def add_feedback(self,feedback_text):
        sql="""
        INSERT INTO feedback(feedback)
        VALUES (%s);
        """ 
        val=(feedback_text,)
        try:
            self.cursor.execute(sql,val)
            self.connector.commit()
            print("feedback added ")
            return True

        except:
            print("feedback cant be added")
            return False

   




if __name__=="__main__":
    status=Status_table()
    status.add_status('4HG19CS001',0)
    print(status.get_status('4HG19CS001'))

    feedback=Feedback_table()
    feedback.add_feedback("this is my first feed back")