import sys
import os
import resources_rc
from Database import *
from AddRecord import *
from Transaction import *
from Dashboard import *
from Statistics import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader

ui_file_path = os.path.join(os.path.dirname(__file__),"MainWindow.ui")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ui_file = QFile(ui_file_path)

        loader = QUiLoader()
        widget = loader.load(ui_file, None)

        DB = "Record.db"

        # CONTROLS DASHBOARD TAB

        widget.dashboard_button.clicked.connect(lambda: widget.stacked_widget.setCurrentWidget(widget.dashboard))
        widget.tip_of_the_day_content.setPlainText(generate.tip)
        widget.balance_text.setPlainText(str(DashContent.current_balance(widget,DB)[0]))
        widget.warning.setText(DashContent.current_balance(widget,DB)[1])
        DashContent.display_goal(widget, Goal.fetch_record(widget,DB))
        percent = DashContent.wallet_status(widget,DB)
        print(f"percent: {percent}")
        try:
            if percent >= 100:
                widget.wallet_meter.setCurrentWidget(widget.hundred)
            elif percent >= 90 < 99:
                widget.wallet_meter.setCurrentWidget(widget.ninety)
            elif percent >= 75 < 89:
                widget.wallet_meter.setCurrentWidget(widget.seventyfive)
            elif percent >= 60 < 74:
                widget.wallet_meter.setCurrentWidget(widget.sixty)
            elif percent >= 45 < 59:
                widget.wallet_meter.setCurrentWidget(widget.fortyfive)
            elif percent >= 30 < 44:
                widget.wallet_meter.setCurrentWidget(widget.thirty)
            elif percent >= 15 < 29:
                widget.wallet_meter.setCurrentWidget(widget.fifteen)
            elif percent >= 0 < 15:
                widget.wallet_meter.setCurrentWidget(widget.zero)

        except Exception as e:
            print(e)

        # CONTROLS FOR STATISTICS TAB

        widget.statistics_button.clicked.connect(lambda: widget.stacked_widget.setCurrentWidget(widget.statistics))
        StatsContent.display_expense(widget, Expense.fetch_record(widget,DB))
        StatsContent.display_income(widget, Income.fetch_record(widget,DB))
        widget.highest_income_2.setPlainText(StatsContent.highest(widget,DB)[0][0])
        widget.income_amt.setPlainText(str(StatsContent.highest(widget,DB)[0][1]))
        widget.income_date_2.setPlainText(StatsContent.highest(widget,DB)[0][2])
        widget.highest_expense.setPlainText(StatsContent.highest(widget,DB)[1][0])
        widget.expense_amt.setPlainText(str(StatsContent.highest(widget,DB)[1][1]))
        widget.expense_date_2.setPlainText(StatsContent.highest(widget,DB)[1][2])
        
        # CONTROLS ADD RECORD TAB

        widget.add_record_button.clicked.connect(lambda: widget.stacked_widget.setCurrentWidget(widget.add_record))
        
        widget.expense_button.clicked.connect(lambda: widget.form.setCurrentWidget(widget.expense_form))
        widget.expense_submit.clicked.connect(lambda: InsertNewRecord.add_expense(widget,DB))

        widget.income_button.clicked.connect(lambda: widget.form.setCurrentWidget(widget.income_form))
        widget.income_submit.clicked.connect(lambda: InsertNewRecord.add_income(widget,DB))


        widget.set_goal_button.clicked.connect(lambda: widget.form.setCurrentWidget(widget.goal_form))
        widget.goal_submit.clicked.connect(lambda: InsertNewRecord.add_goal(widget,DB))

        # CONTROLS TRANSACTION TAB

        widget.transaction_button.clicked.connect(lambda: widget.stacked_widget.setCurrentWidget(widget.transaction))
        DisplayTable.display_record(widget, Transaction.fetch_record(widget,DB))

        # CONTROLS ABOUT TAB
        widget.about_button.clicked.connect(lambda: widget.stacked_widget.setCurrentWidget(widget.about))
        widget.show()

        # CONTROLS EXIT
        widget.logout_button.clicked.connect(sys.exit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())