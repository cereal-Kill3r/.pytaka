from Database import *
from PySide2.QtWidgets import QTableWidgetItem

class DisplayTable(Record):
    def display_record(self, rows):
        try:
            for row in rows:
                row_position = self.transaction_table.rowCount()
                item_count = 0

                table_widget = QTableWidgetItem()
                self.transaction_table.setRowCount(row_position + 1)
                self.transaction_table.setVerticalHeaderItem(row_position, table_widget)

                for item in row:
                    self.table_widget = QTableWidgetItem()
                    self.transaction_table.setItem(row_position, item_count, self.table_widget)
                    self.table_widget = self.transaction_table.item(row_position,item_count)
                    self.table_widget.setText(str(item))

                    item_count = item_count + 1
                
                row_position = row_position + 1

        except Exception as e:
            print(e)