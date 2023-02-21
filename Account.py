import os
import sys
import sqlite3
from Main import *

ui_file_path = os.path.join(os.path.dirname(__file__),"WelcomeWindow.ui")

class AccountOpt():
    def __init__(self, arg):
        super(AccountOpt, self).__init__()
        self.arg = arg

    def login(self, database):

        """ LOGIN FORM: Assess user input infomration with the database"""

        while True:
            email = self.log_email.text()
            password = self.log_pass.text()
            fetch_e = cursor.execute("SELECT email from login WHERE email='"+email+"'").fetchone()
            fetch_e = str(fetch_e).strip("('',)'")
            if fetch_e == email:
                fetch_p = cursor.execute("SELECT password from login WHERE password='" + password + "'").fetchone()
                fetch_p = str(fetch_p).strip("('',)'")
                if fetch_p == password:
                    print('You are now logged in.')
                    Main()
            else:
                print('Wrong password.')
                break

            email = self.log_email.setText("")
            password = self.log_pass.setText("")

    def signup(self, database):

        """ SIGNUP FORM: Get the user information for creating new account"""

        while True:
            fname = self.first_name.text()
            lname = self.last_name.text()
            birthdate = self.date_of_birth.text()
            email = self.email_add.text()
            fetch_p =cursor.execute('SELECT email FROM login').fetchone()
            fetch_p=str(fetch_p).strip("('',)'")
            
            if fetch_p == email:
                widget.prompt.setPlainText("Account already exists")
                break
            else:
                while True:
                    password = self.password.text()
                    cursor.execute('INSERT INTO login VALUES(?,?,?,?,?,?)',
                                    (None, fname, lname, birthdate, email, password))
                    connection.commit()
                    widget.prompt.setPlainText("You are now registered")
                    break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_file = QFile(ui_file_path)

    loader = QUiLoader()
    widget = loader.load(ui_file)
    ui_file.close()

    acc_DB = "Record.db"
    connection = sqlite3.connect(acc_DB)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,fname TEXT NOT NULL,
                    lname TEXT NOT NULL, birthdate TEXT NOT NULL, 
                    email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)""")
    connection.commit()
    
    widget.login_button_3.clicked.connect(lambda: widget.welcome_stacked.setCurrentWidget(widget.login))
    widget.login_butt.clicked.connect(lambda: AccountOpt.login(widget,acc_DB))
    widget.login_butt.clicked.connect(lambda: AccountOpt.open_main)
    widget.return_butt.clicked.connect(lambda: widget.welcome_stacked.setCurrentWidget(widget.welcome_page))

    widget.signup_button_3.clicked.connect(lambda: widget.welcome_stacked.setCurrentWidget(widget.sign_up))
    widget.signup_butt.clicked.connect(lambda: AccountOpt.signup(widget,acc_DB))
    widget.signup_butt.clicked.connect(lambda: widget.welcome_stacked.setCurrentWidget(widget.welcome_page))
    
    widget.show()

    sys.exit(app.exec_())
