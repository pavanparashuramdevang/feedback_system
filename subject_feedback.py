from db_connect import Connector


class Subject_feedback_table():

    def __init__(self,subject):
        self.subject=subject
        self.connector=Connector()
        self.cursor=self.connector.get_cursor()
        self.create_subject_feedback_table()

    def create_subject_feedback_table(self):
        try:
            print(
               f"""
            CREATE TABLE IF NOT EXISTS {self.subject} (
                1 INTEGER ,
                2 INTEGER ,
                3 INTEGER ,
                4 INTEGER ,
                5 INTEGER ,
                6 INTEGER ,
                7 INTEGER ,
                8 INTEGER ,
                9 INTEGER 
            );
            """ 
            )
            self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.subject}(
                one INTEGER ,
                two INTEGER ,
                three INTEGER ,
                four INTEGER ,
                five INTEGER ,
                six INTEGER ,
                seven INTEGER ,
                eight INTEGER ,
                nine INTEGER 
            );
            """)
            self.commit()
            print(f"SUCCESS :) {self.subject}  table is avilable")

        except:
            print(f"ERROR :( {self.subject} table may already exists")

    
    # def add_subject_rating(self,subject,rating:dict):

    #     # try:
    #     print(f""" INSERT INTO {subject} VALUES ({str(rating)[1:-1]}); """)

    #     self.cursor.execute(f""" INSERT INTO {subject} VALUES ({str(rating)[1:-1]}); """)

    #     self.connector.commit()
    #     print("status added or updated")

    #     # except:
    #     #     print("status not able to update or add")

    def add_subject_rating(self,subject,rating:dict):
        try:
            columns = ', '.join(rating.keys())
            values = ', '.join(str(value) for value in rating.values())
            sql = "INSERT INTO {} ({}) VALUES ({});".format(subject,columns, values)
            self.cursor.execute(sql)
            self.connector.commit()
            print("commited successfully")
        except:
            print("update not possible some error")






if __name__=="__main__":
    feedback=Subject_feedback_table('18CS61')
    feedback.add_subject_rating('18CS61',rating={'one':2,'three':7})
