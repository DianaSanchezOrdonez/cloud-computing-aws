from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "172.31.85.15" # IPv4 privada de "MV BD"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_customers"  

# Get echo test for load balancer's health check
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Get all customers
@app.get("/customers")
def get_customers():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"customers": result}

# Get an customer by ID
@app.get("/customers/{id}")
def get_customer(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM customers WHERE id = {id}")
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    return {"customer": result}

# Add a new customer
@app.post("/customers")
def add_customer(item:schemas.Customer):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    email = item.email
    first_name = item.first_name
    last_name = item.last_name
    phone = item.phone
    status = item.status
    address = item.address
    cursor = mydb.cursor()
    sql = "INSERT INTO customers (email, first_name, last_name, phone, status, address) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (email, first_name, last_name, phone, status, address)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Customer added successfully"}

# Modify a customer
@app.put("/customers/{id}")
def update_customer(id:int, item:schemas.Customer):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    email = item.email
    first_name = item.first_name
    last_name = item.last_name
    phone = item.phone
    status = item.status
    address = item.address
    cursor = mydb.cursor()
    sql = "UPDATE customers SET email=%s, first_name=%s, last_name=%s, phone=%s, status=%s, address=%s WHERE id=%s"
    val = (email, first_name, last_name, phone, status, address, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Customer modified successfully"}

# Delete a customer by ID
@app.delete("/customers/{id}")
def delete_customer(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM customers WHERE id = {id}")
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Customer deleted successfully"}