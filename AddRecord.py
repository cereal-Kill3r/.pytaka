from Database import *
from Transaction import DisplayTable

class InsertNewRecord():
    def __init__(self, arg):
        super(InsertNewRecord, self).__init__()
        self.arg = arg

    def add_expense(self, database):

        """Insert values from expense input field to database"""

        name = self.expense_name.text()
        date = self.expense_date.text()
        amount = self.expense_amount.text()
        category = self.expense_category.currentText()

        Expense(database).insert_values(name,category,date,amount)

        self.expense_name.setText("")
        self.expense_date.setText("")
        self.expense_amount.setText("")
    
    def add_income(self, database):

        """Insert values from income input field to database"""

        name = self.income_name.text()
        date = self.income_date.text()
        amount = self.income_amount.text()
        category = self.income_category.currentText()

        Income(database).insert_values(name,category,date,amount)
        Transaction(database)

        self.income_name.setText("")
        self.income_date.setText("")
        self.income_amount.setText("")

    def add_goal(self, database):

        """Insert values from goal input field to database"""

        name = self.goal_name.text()
        target_date = self.goal_date.text()
        target_amount = self.goal_amount.text()
        note = self.goal_note.text()

        Goal(database).insert_values(name,target_date,target_amount,note)

        self.goal_name.setText("")
        self.goal_date.setText("")
        self.goal_amount.setText("")
        self.goal_note.setText("")