import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

query = QSqlQuery()
query.exec(
    """
    SELECT *
    FROM users
    limit 5
    """
)

count = query.record().count()
for i in range(count):
    print(query.record().fieldName(i), end='\t')
print()
while query.next():
    for i in range(count):
        print(query.value(i), end='\t')
    print()
