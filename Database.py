from generate import *
import sqlite3
from sqlite3 import Error

class Record:
    def __init__(self, database, table_name, table_structure):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()
        self.table_name = table_name
        self.table_structure = table_structure
        self.create_table()

    def create_table(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} {self.table_structure}")
        self.connect.commit()

    def __del__(self):
        self.connect.close()

class Expense(Record):
    def __init__(self, database):
        table_name = "expense_record"
        table_structure = """(id TEXT PRIMARY KEY UNIQUE,
                             name TEXT,
                             category TEXT, 
                             date TEXT,
                             amount REAL)"""
        super().__init__(database, table_name, table_structure)
        
    def insert_values(self, name, category, date, amount):
        
        """Insert expense values into expense table"""
        query = f"""INSERT INTO {self.table_name} 
                    (id,name,category,date,amount) 
                    VALUES ('{code()}','{name}','{category}','{date}',{amount})"""
        self.cursor.execute(query)
        self.connect.commit()
    
    def fetch_record(self, database):

        """Gets data all data from expense table"""
        connect = sqlite3.connect(database)
        fetch_data = "SELECT * FROM expense_record"
        try:
            connection = connect.cursor()
            connection.execute(fetch_data)
            return connection

        except Error as e:
            print(e)

class Income(Record):
    def __init__(self, database):
        table_name = "income_record"
        table_structure = """(id TEXT PRIMARY KEY UNIQUE, 
                             name TEXT, 
                             category TEXT,
                             date TEXT,
                             amount REAL)"""
        super().__init__(database, table_name, table_structure)

    def insert_values(self, name, category, date, amount):
        """Insert income values into income table"""
        query = f"""INSERT INTO {self.table_name}
                 (id,name,category,date,amount) VALUES 
                 ('{code()}','{name}','{category}','{date}',{amount})"""

        self.cursor.execute(query)
        self.connect.commit()
    
    def fetch_record(self, database):

        """Gets data all data from income table"""
        connect = sqlite3.connect(database)
        fetch_data = "SELECT * FROM income_record"
        try:
            connection = connect.cursor()
            connection.execute(fetch_data)
            return connection

        except Error as e:
            print(e)

class Goal(Record):
    def __init__(self, database):
        table_name = "goal_record"
        table_structure = """(id TEXT PRIMARY KEY UNIQUE,
                            name TEXT,
                            target_date TEXT,
                            target_amount REAL,
                            note TEXT)"""
        super().__init__(database, table_name, table_structure)
    
    def insert_values(self, name, target_date, target_amount, note):

        """Insert goal values into income table"""
        query = f"""INSERT INTO {self.table_name} 
                (id,name,target_date,target_amount,note)
                 VALUES ('{code()}','{name}','{target_date}',{target_amount},'{note}')"""
        self.cursor.execute(query)
        self.connect.commit()
    
    def fetch_record(self, database):
        connect = sqlite3.connect(database)

        fetch_data = "SELECT * FROM goal_record"

        try:
            connection = connect.cursor()
            connection.execute(fetch_data)
            return connection

        except Error as e:
            print(e)

class Transaction(Record):
    def __init__(self, database):
        table_name = "transaction_record"
        table_structure = """(id TEXT UNIQUE,
                            name TEXT,
                            category TEXT,
                            date TEXT,
                            amount REAL,
                            type TEXT)"""
        super().__init__(database, table_name, table_structure)
        
        try:
            self.cursor.execute("SELECT id, name, category, date, amount FROM expense_record")
            expense_list = self.cursor.fetchall()
            
            for expense in expense_list:
                self.cursor.execute("""INSERT OR IGNORE INTO transaction_record 
                (id,name,category,date,amount,type) 
                VALUES (?,?,?,?,?,'Expense')""", expense)

        except Exception as e:
            print(e)

        try:
            self.cursor.execute("SELECT id, name, category, date, amount FROM income_record")
            income_list = self.cursor.fetchall()
            
            for income in income_list:
                self.cursor.execute("""INSERT OR IGNORE INTO transaction_record 
                (id,name,category,date,amount,type) 
                VALUES (?,?,?,?,?,'Income')""", income)

        except Exception as e:
            print(e)

        self.connect.commit()
        self.connect.close()
  
    def fetch_record(self, database):
        connect = sqlite3.connect(database)

        fetch_data = "SELECT * FROM transaction_record"

        try:
            connection = connect.cursor()
            connection.execute(fetch_data)
            return connection

        except Error as e:
            print(e)

# class Budget(Record):
#     def __init__(self, database):
#         table_name = "budget_record"
#         table_structure = """(id TEXT PRIMARY KEY UNIQUE, 
#                              name TEXT, 
#                              category TEXT,
#                              date TEXT,
#                              budget_limit REAL)"""
#         super().__init__(database, table_name, table_structure)

#     def insert_values(self, name, category, date, limit):
#         query = f"INSERT INTO {self.table_name} (id,name,category,date,budget_limit) VALUES ('{code()}','{name}', '{category}', '{date}', {limit})"
#         self.cursor.execute(query)
#         self.connect.commit()

# class BudgetStatus(Record):
#     def __init__(self, database):
#         table_name = "budget_status_record"
#         table_structure = """(name TEXT,
#                               category TEXT,
#                               date TEXT,
#                               budget_limit REAL,
#                               spent REAL,
#                               remaining REAL)"""
#         super().__init__(database, table_name, table_structure)

#         try:
#             self.cursor.execute("""SELECT b.name, b.category, b.date FROM budget_record b
#                                    JOIN expense_record e ON 
#                                    b.category = e.category""")
#             expense_list = self.cursor.fetchall()
#             self.cursor.execute("SELECT amount FROM expense_record")
#             budget_spent = self.cursor.fetchall()
#             self.cursor.execute("SELECT budget_limit FROM budget_record")
#             budget_limit = self.cursor.fetchall()
#             self.cursor.execute("INSERT INTO budget_status_record (remaining) VALUES (2000)")
#             remaining = 2000
#             # print(expense_list)
#             # print(budget_spent)
#             # print(budget_limit)
            
#             for expense in expense_list:
#                 query = """INSERT OR IGNORE INTO budget_status_record 
#                                     (name,category,date,budget_limit,spent,remaining) 
#                                     VALUES (?,?,?,?,?,?)"""
#                 values = (expense[0],expense[1],expense[2],
#                         budget_limit,budget_spent,remaining)

#                 self.cursor.execute(query,values)
                
#         except Exception as e:
#             print(e)