import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# создание связи с базой на основе драйвера SQLITE
con = QSqlDatabase.addDatabase("QSQLITE")
# привязка файла базы к связи
con.setDatabaseName("contacts.sqlite")
# попытка открытия базы указанной при создании связи
if not con.open():
    # при получении ошибки выводится текст ошибки
    print("Database Error: %s" % con.lastError().databaseText())  # Устаревший способ форматирования строк
    # альтернатива
    #  print(f'Database Error: {con.lastError().databaseText()}')
    sys.exit(1)

# создание запроса
query = QSqlQuery()
query.exec(
    """
    SELECT *
    FROM users
    limit 5
    """
)  # выполнение запроса

# получение количество столбцев и имен столбцов
count = query.record().count()  # количество столбцов
for i in range(count):
    print(query.record().fieldName(i), end='\t')  # получение имен столбцов
print()

# получение ответа на запрос
while query.next():  # пока существует следующая запись
    for i in range(count):  # перебираем столбцы по индексам
        print(query.value(i), end='\t')  # и выводим значение в них
    print()
