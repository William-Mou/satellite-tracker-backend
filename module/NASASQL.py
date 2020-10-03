# coding=utf-8

import pymysql
import time


class NASASQL:
    def __init__(self, sateid, user="dbuser", password="nasaspace", db_name="williamdb"):
        flag = True
        while flag:
            try:
                self.db = pymysql.connect(  host='10.121.190.24',
                                            port=3306,
                                            user=user,
                                            password=password,
                                            db=db_name,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
                flag = False
            except:
                print("等待 SQL Server 啟動")
                time.sleep(1)
        self.tableName = "id"+str(sateid)
        self.cursor = self.db.cursor()
        print("Connected db")

    def connect_SQL(self):
        """
        azimuth : Satellite azimuth with respect to observer's location (degrees)
        elevation : Satellite elevation with respect to observer's location (degrees)
        ra : Satellite right ascension (degrees)
        dec : Satellite declination (degrees)
        """
        sql = """CREATE TABLE %s( \
TIMESTAMP INT NOT NULL, \
SATNAME VARCHAR(30) NOT NULL, \
SATLATITUDE FLOAT NOT NULL, \
SATLONGITUDE FLOAT NOT NULL, \
SATALTITUDE FLOAT NOT NULL, \
AZIMUTH FLOAT, \
ELEVATION FLOAT, \
RA FLOAT,  \
DECC FLOAT)""" % self.tableName
        try:
            self.cursor.execute(sql)
            
        except:
            self.db.rollback()
            print("Table Exists:%s" % self.tableName)
    
    def select_SQL(self, TIMESTAMP):
        sql = "SELECT * FROM `%s` WHERE `TIMESTAMP` = '%s'" % (self.tableName, TIMESTAMP)
        self.cursor.execute(sql.lstrip())
        result = self.cursor.fetchone()
        return result

    def insert_SQL(self, TIMESTAMP, SATNAME, SATLATITUDE, SATLONGITUDE, SATALTITUDE):
        sql = "INSERT INTO %s(TIMESTAMP, SATNAME, SATLATITUDE, SATLONGITUDE, SATALTITUDE) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
            self.tableName, TIMESTAMP, SATNAME, SATLATITUDE, SATLONGITUDE, SATALTITUDE)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("db.commit")
        except:
            self.db.rollback()

    def close_SQL(self):
        self.db.close()