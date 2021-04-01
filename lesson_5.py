'''
****************************************************************************
*  Program  lessson_5.py                                                   *
*  Author   Baba                                                           *
*  Date     March 16, 2021                                                 *
*  Source   Realpython https://realpython.com/python-sql-libraries/#sqlite *
*  Description:                                                            *
*  This program is used to introduce Geniuses to using a                   *
*  database Structured Query Language (SQL).  The program                  *
*  imports the sqlite3 module which allows you to create                   *
*  and interact with an SQL Database                                       *
*                                                                          *
*  - The create_connection function is passed the                          *
*    path of the SQLite database file then it connects                     *
*    the app to an exixting SQLite3 database named hgp_pods                *
*    or if it;s not present it creates the database file                   *
*                                                                          *
*  - The execute_query function is passed the path and the                 *
*    query to implement; create_staff_member_table query and               *
*    add_staff_member query                                                *
*                                                                          *
*  - The execute_read function is passed the path and                      *
*    the display_staff_member query                                        *
****************************************************************************

'''

import sqlite3
from sqlite3 import Error

############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


###################  Connect/Create to the Sqlite3 Database File *********************
connection = create_connection("oak8_pods.sqlite5")


##########################  Create staff table variable query ################
create_staff_members_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_staff_members_table_query) 

add_staff_members_query = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeeem','(415) 684-0505','Programs Director');
"""
execute_query(connection, add_staff_members_query)
#################### Executive query to create staff table #################


################# Create insert query to add staff members to staff table #######

####################  Pod leader tables ##################


create_pod_leaders_table_query = """
CREATE TABLE IF NOT EXISTS leader (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_pod_leaders_table_query)


add_pod_leaders_query = """
INSERT INTO
  leader (name,cell,position)
VALUES
    ('Richard','(510) 228-5623','Pod Leader'),
    ('Jacore','(845) 200-6250','Pod Leader'),
    ('Gabriel','(510) 326-5834','Pod Leader'),
    ('Aris','(510) 229-6359','Pod Leader'),
    ('Andrew','(510) 326-5834','Pod Leader');

"""
execute_query(connection, add_pod_leaders_query)

########################### Pod members table ################################
 

create_pod_member_table_query = """
CREATE TABLE IF NOT EXISTS member (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
execute_query(connection, create_pod_member_table_query)


add_pod_member_query = """
INSERT INTO
  member (name,cell,position)
VALUES
    ('Gabriel','(510) 326-5834','Pod Member'),
    ('Akari','(000) 000-0000','Pod Member'),
    ('Emmanuel','(000) 000-0000','Pod Member'),
    ('David','(510) 631-6288','Pod Member');
"""


execute_query(connection, add_pod_member_query) 

#################################### staff ##########################
display_staff_query = "SELECT * from staff"


staff = execute_read_query(connection, display_staff_query)

for user in staff:
  print(user)

##################################### leader #########################
display_leader_query = "SELECT * from leader"

leader = execute_read_query(connection, display_leader_query)

for user in leader:
  print(user)

#################################### member ###########################
display_member_query = "SELECT * from member"

member = execute_read_query(connection, display_member_query)

for user in member:
  print(user)






execute_query(connection,'drop table staff')
execute_query(connection,'drop table leader')
execute_query(connection,'drop table member')

