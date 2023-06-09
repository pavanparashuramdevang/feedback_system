from db_connect import Connector
import time
import datetime


def convertSQLDateTimeToTimestamp(value):
    return time.mktime(time.strptime(value, '%Y-%m-%d %H:%M:%S'))


class Otp_table():

    def __init__(self):
        self.connector=Connector()
        self.cursor=self.connector.get_cursor()
        self.create_otp_table()

    def create_otp_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS otp(
            usn VARCHAR(12) NOT NULL,
            otp VARCHAR(6),
            updated_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY(usn)
            );
            """)
            self.commit()
            print("SUCCESS :) otp table is avilable")

        except:
            print("ERROR :( otp table may already exists")

    def add_otp(self,usn,otp):
        sql="""
        INSERT INTO otp(usn,otp) 
        VALUES (%s,%s)
        ON DUPLICATE KEY UPDATE
        otp=%s;
        """
        usn=usn.upper()
        otp=str(otp)
        val=(usn,otp,otp)
        try:
            self.cursor.execute(sql,val)
            self.connector.commit()
            print("otp added or updated")

        except:
            print("otp update add unable")


    def get_otp(self,usn):
        try:
            sql="""
            SELECT otp,updated_time FROM otp
            WHERE usn=%s;
            """
            val=(usn,)
            self.cursor.execute(sql,val)
            data=self.cursor.fetchone()
            otp=data[0]
            updated_time=data[1]
            print(otp,updated_time)
            if (datetime.datetime.now()-updated_time).total_seconds() >=120:
                return None
            else:
                return otp

        except:
            return None



if __name__=="__main__":
    otp_table=Otp_table()
    otp_table.add_otp('4hg19cs001',123456)
    otp_table.add_otp('4HG19CS002','123455')
    otp_table.get_otp('4HG19CS001')
    otp_table.get_otp('4HG19CS002')


