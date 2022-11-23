import sys

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableView)


class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(540, 400)

        # Set up the model
        self.model = QSqlTableModel(self)
        self.model.setTable("users")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Имя")
        self.model.setHeaderData(2, Qt.Horizontal, "Job_id")
        self.model.setHeaderData(3, Qt.Horizontal, 'Оклад')
        self.model.setHeaderData(3, Qt.Horizontal, "Email")
        self.model.select()

        # Set up the view

        self.view = QTableView()
        self.view.setModel(self.model)
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
