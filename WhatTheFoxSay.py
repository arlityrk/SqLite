import sqlite3
import datetime

conn = sqlite3.connect('main.db')
c = conn.cursor()

person = input('Person(username/display name):')
begin_date = input('Begin date(YYYY-MM-DD):')
end_date = input('End date(YYYY-MM-DD):')  + " 23:59"
c.execute('SELECT body_xml, timestamp from messages t where (author=? or from_dispname=?) and datetime(timestamp, "unixepoch", "localtime") between ? and ?', (person, person, begin_date, end_date,))
result = c.fetchall()
for x in range(0,len(result)):
    print("Time : %s" % datetime.datetime.fromtimestamp(result[x][1]))
    print(result[x][0])
    print("-------------------------------------------------------------------")
conn.close()