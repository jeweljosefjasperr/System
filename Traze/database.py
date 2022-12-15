import sqlite3
import bcrypt
import logging

#conn = sqlite3.connect('test.db')
    
class Datab:

    def __init__(self):
        self.conn = sqlite3.connect(database = "test.db")
        self.cursor = self.conn.cursor()
        self.create_users_table()

    def show_databases(self):
        databases = self.cursor.execute("SHOW DATABASES")
        for x in self.cursor:
            print(x)

    def create_users_table(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(255),
        username VARCHAR(255), email varchar(255),phone VARCHAR(50), address VARCHAR(255), password varchar(255),
        role varchar(50))""")
        

    def create_user(self, fullname, username, email, phone, address, password, role):
        '''user_q= "INSERT INTO users (fullname, username, email,phone, address, password, role),VALUES(?, ?, ?, ?, ?, ?, ?);"
        self.cursor.execute(user_q)'''
        password_bytes = bytes(password, 'utf-8')
        password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        sql = "INSERT INTO users (fullname, username, email, phone, address, password, role) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (fullname, username, email, phone, address, password_hash, role)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return True

    def login(self, username, password):
        query = "SELECT * FROM users WHERE username = ?"
        self.cursor.execute(query,(username,))
        users = self.cursor.fetchall()
        password_hash = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
        for user in users:
            if bcrypt.checkpw(password.encode('utf-8'), password_hash):
                return True
            else:
                return False
            
    '''def getInfo(self, fullname, username, email, phone, address, password, role):
        query = "SELECT * FROM users WHERE username = ?"
        self.cursor.execute(query,(username,))
        users = self.cursor.fetchall()
        print(users)'''

    def delete_user(self, id):
        sql = "DELETE FROM users WHERE id = ?"
        self.cursor.execute(sql,(id))
        self.conn.commit()

class SellerDB:
    def __init__(self):
        self.conn = sqlite3.connect(database = "test.db")
        self.cursor = self.conn.cursor()
        #self.create_seller_table()

    def show_databases(self):
        databases = self.cursor.execute("SHOW DATABASES")
        for x in self.cursor:
            print(x)
        
    def create_seller_table(self):
        #tracking_id = "SELECT seller (CAST(RAND()*1000000 AS INT),6) as tracking_id"
        self.conn.execute("""CREATE TABLE IF NOT EXISTS seller (tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                          cust_name VARCHAR(255), cust_phone VARCHAR(11), item_name VARCHAR(255), cust_addr VARCHAR(25),
                          pu_addr VARCHAR(255), date_order DATE, category VARCHAR(255) )""")
        
        #default (LPAD(rand() * 1000000, 6, '0'))

    def add_customer(self, cust_name, cust_phone, item_name, cust_addr,  pu_addr, date_order, category):
        #tracking_id = "SELECT LEFT (CAST(RAND()*1000000 AS INT),6) as tracking_id"
        seller_q = """INSERT INTO seller (cust_name, cust_phone, item_name, cust_addr, pu_addr, date_order, category) VALUES (?, ?, ?, ?, ?, ?, ?);"""
        seller_values = (cust_name, cust_phone, item_name, cust_addr, pu_addr, date_order, category)
        self.cursor.execute(seller_q, seller_values)
        self.conn.commit()
        return True
    
    def get_custname(self):
        list_customers = self.cursor.execute("SELECT cust_name FROM seller").fetchall()
        return list_customers
        
        
    def Show_customers(self):
        c = self.cursor.execute("SELECT * FROM sellers")
    
    '''def track(self, tracking_id, cust_name, cust_phone, item_name, cust_addr,  pu_addr, date_order, category):
        query = "SELECT * FROM seller WHERE tracking_id = ?"
        self.cursor.execute(query,(tracking_id,))
        track_info = self.cursor.fetchall()
        
        print(track_info)'''
        
    def list_customers(self):
        c = self.cursor.execute("SELECT cust_name FROM seller ORDER BY tracking_id ASC").fetchall()
        c.close()
        
def get_data(sql):
    conn = sqlite3.connect('test.db')
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        cursor.close()
        return response
    except Exception as e:
        logging.warning('Exception:%s' % e)
    finally:
        conn.close()
        
        