__author__ = 'ardi'

import sqlite3
import html
import datetime
import sys

def get_person_chat_on_date(person,date):
    start_datetime = datetime.datetime.strptime(date,"%Y%m%d")
    end_datetime = start_datetime + datetime.timedelta(days=1)
    with sqlite3.connect("main.db") as connection:
        c = connection.cursor()
        chat = c.execute("SELECT body_xml FROM Messages where author=? and timestamp between ? and ?",
                         [person,start_datetime.timestamp(),end_datetime.timestamp()])
        for row in chat:
            if row[0]:
                print (html.unescape(row[0]))

if __name__ == '__main__':
    get_person_chat_on_date(sys.argv[1],sys.argv[2])
