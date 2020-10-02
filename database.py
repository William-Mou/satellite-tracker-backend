# a simple sample
import sqlite3 

connection = sqlite3.connect("backend.db") 

crsr = connection.cursor() 

sql_command = """CREATE TABLE info ( 
satname varchar(10),
satid varchar(50), 
);"""

crsr.execute(sql_command) 
connection.commit() 

sql_command = """CREATE TABLE positions ( 
satlatitude varchar(20),
satlongitude varchar(20), 
sataltitude varchar(20),
azimuth varchar(20),
elevation varchar(20),
ra varchar(20),
dec varchar(20),
timestamp varchar(20),
eclipsed varchar(2), 
);"""
#eclipsed: true = 1, false = 0

crsr.execute(sql_command) 
connection.commit() 
connection.close() 
