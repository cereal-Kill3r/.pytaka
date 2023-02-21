from Database import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QTableWidgetItem
import resources_rc

class StatsContent(Record):
    """ Fetch all record from the database """
    def __init__(self, arg):
        super(StatsContent, self).__init__()
        self.arg = arg
        
    def display_expense(self, database):
        try:
            for row in database:
                row_position = self.expense_table.rowCount()
                print(type(row[0]))
                print(row)
                print(type(row_position))
                item_count = 0

                self.expense_table.setRowCount(row_position + 1)
                table_widget = QTableWidgetItem()
                self.expense_table.setVerticalHeaderItem(row_position, table_widget)

                for item in row:
                    self.table_widget = QTableWidgetItem()
                    self.expense_table.setItem(row_position, item_count, self.table_widget)
                    self.table_widget = self.expense_table.item(row_position,item_count)
                    self.table_widget.setText(str(item))

                    item_count = item_count + 1
                
                row_position = row_position + 1

        except Exception as e:
            print(e)

    def display_income(self, database):
        """ Fetch all record from the database """
        try:
            for row in database:
                row_position = self.income_table.rowCount()
                item_count = 0

                self.income_table.setRowCount(row_position + 1)
                table_widget = QTableWidgetItem()
                self.income_table.setVerticalHeaderItem(row_position, table_widget)

                for item in row:
                    self.table_widget = QTableWidgetItem()
                    self.income_table.setItem(row_position, item_count, self.table_widget)
                    self.table_widget = self.income_table.item(row_position,item_count)
                    self.table_widget.setText(str(item))

                    item_count = item_count + 1
                
                row_position = row_position + 1

        except Exception as e:
            print(e)

    def highest(self, database):

        """Selects highest amount and its data"""
        conn =  sqlite3.connect(database)
        self.cursor = conn.cursor()
        try:
            self.cursor.execute("""SELECT name, amount, date FROM expense_record 
                  WHERE amount = (SELECT MAX(amount) 
                  FROM expense_record )""")
            highest_exp = self.cursor.fetchall()[0]

        except:
            highest_exp = '    '
            
        try:
            self.cursor.execute("""SELECT name, amount, date FROM income_record 
                  WHERE amount = (SELECT MAX(amount) 
                  FROM income_record )""")
            highest_inc = self.cursor.fetchall()[0]
        except:
            highest_inc = '    '
        
        return highest_inc, highest_exp