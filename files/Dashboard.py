import generate
from Database import *
from PySide2.QtWidgets import QTableWidgetItem

class DashContent(Record):
    def display_goal(self, rows):

        """Display record from database to TableWidget"""

        print(rows)
        try:
            for row in rows:
                row_position = self.goal_table.rowCount()
                print(type(row[0]))
                print(row)
                print(type(row_position))
                item_count = 0

                self.goal_table.setRowCount(row_position + 1)
                table_widget = QTableWidgetItem()
                self.goal_table.setVerticalHeaderItem(row_position, table_widget)

                for item in row:
                    self.table_widget = QTableWidgetItem()
                    self.goal_table.setItem(row_position, item_count, self.table_widget)
                    self.table_widget = self.goal_table.item(row_position,item_count)
                    self.table_widget.setText(str(item))

                    item_count = item_count + 1
                row_position = row_position + 1
        except Exception as e:
            print(e)
    
    def fetch_data(self,database):

        """Fetch total income and expense record from database"""

        conn =  sqlite3.connect(database)
        self.cursor = conn.cursor()

        try:
            self.cursor.execute("SELECT SUM(amount) FROM expense_record")
            total_expense = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT SUM(amount) FROM income_record")
            total_income = self.cursor.fetchone()[0]
            # Computes for the current balance
            balance = total_income - total_expense     

        except:
            balance = 0
            total_income = 0  
            total_expense = 0   
            
        return balance, total_expense, total_income

    def current_balance(self, database):
        """Displays current balance"""
        conn =  sqlite3.connect(database)
        self.cursor = conn.cursor()
        current_balance = DashContent.fetch_data(self,database)[0]
        warning_text = ''
        if current_balance <= 1000:
            if current_balance >= 500:
                warning_text = "Low Balance"
            elif current_balance == 0:
                warning_text = "No Balance"
            elif current_balance < 0:
                warning_text = "Insufficient Balance"

        return current_balance, warning_text


    def wallet_status(self,database):
        """Controls the wallet meter status 
           that is based on income and expense"""
           
        conn =  sqlite3.connect(database)
        self.cursor = conn.cursor()
        try: 
            total_expense = DashContent.fetch_data(self,database)[1]
            total_income = DashContent.fetch_data(self,database)[2]

            percent = abs((total_expense / total_income)*100) 
            return percent
            
        except Exception as e:
            print(Exception)