from database import DatabaseContextManager

def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    companies_id INTEGER,
    FOREIGN KEY (companies_id) REFERENCES Companies(companies_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_customer(first_name: str, last_name: str, age: int):
    query = """INSERT INTO Customer(first_name, last_name, age) VALUES(?,?,?)"""
    parameters = [first_name, last_name, age]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customer():
    query = """SELECT * FROM Customer"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_customer_name(old_first_name: str, new_first_name: str):
    query = """UPDATE Customer
                SET first_name = ?
                WHERE first_name = ?"""
    parameters = [new_first_name, old_first_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_csutomer(last_name: str):
    query = """DELETE FROM Customer
                WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


#-------------------------------------------------------------------------

def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    companies_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER,
    average_salary INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_companies(company_name: str, employee_count: int, average_salary: int):
    query = """INSERT INTO Companies(company_name, employee_count, average_salary) VALUES(?,?,?)"""
    parameters = [company_name, employee_count, average_salary]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_companies_customer():
    query = """SELECT * FROM Customer
                JOIN Companies
                    ON Customer.id = Companies.companies_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def drop_table():
    query = """DROP TABLE Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


