'''import pyodbc
con = pyodbc.connect (
                      'Server = .\SQLEXpress;'
                       'Database = Python;'
                       'Trusted_Connection=yes;')
cur = con.cursor()
#cur.execute('select')

'''

import pyodbc
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=.\SQLEXPRESS;'
    r'DATABASE=Python;'
    r'Trusted_Connection=yes;'
)
con = pyodbc.connect(conn_str)

cur= con.cursor()
cur.execute('Select * from Python.dbo.Employee')
#result=cur.fetchall()

'''
cur.execute("INSERT INTO  Python.dbo.Employee VALUES(?,?,?)",[109,'fdte',34325434])
cur.commit()



for row in cur:
    print(row[0],row[1],row[2])

    '''

cur.execute("""UPDATE Python.dbo.Employee SET name=%s WHERE Employee ID = %d""",[('raja',3)])
cur.commit()




