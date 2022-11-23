import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem)


class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(550, 400)

        self.view = QTableWidget()

        query = QSqlQuery("SELECT * FROM users;")

        count = query.record().count()
        self.view.setColumnCount(count)
        self.view.setHorizontalHeaderLabels([query.record().fieldName(i) for i in range(count)])

        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            for i in range(count):
                self.view.setItem(rows, i, QTableWidgetItem(str(query.value(i))))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            f"Database Error: {con.lastError().databaseText()}"
        )

        return False
    return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    win = Contacts()
    win.show()
    sys.exit(app.exec_())
