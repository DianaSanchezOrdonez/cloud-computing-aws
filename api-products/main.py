from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "172.31.85.15" # IPv4 privada de "MV BD"
port_number = "8006"
user_name = "root"
password_db = "utec"
database_name = "bd_api_products"  

# Get echo test for load balancer's health check
@app.get("/")
def echo_test():
    return {"message": "Echo Test OK"}

@app.get("/products")
def products():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"products": result}

@app.get("/products/{id}")
def product(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = {id}")
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    return {"product": result}

@app.post("/products")
def product(item:schemas.Product):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    sku = item.sku
    name = item.name
    description = item.description
    price = item.price
    category_id = item.category_id
    status = item.status
    cursor = mydb.cursor()
    sql = """
        INSERT INTO products (sku, name, description, price, category_id, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    val = (sku, name, description, price, category_id, status)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Product added successfully"}

# Modify a customer
@app.put("/products/{id}")
def product(id:int, item:schemas.Product):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    sku = item.sku
    name = item.name
    description = item.description
    price = item.price
    category_id = item.category_id
    status = item.status
    cursor = mydb.cursor()
    sql = "UPDATE products SET sku=%s, name=%s, description=%s, price=%s, category_id=%s, status=%s WHERE id=%s"
    val = (sku, name, description, price, category_id, status, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Product modified successfully"}

# Delete a customer by ID
@app.delete("/products/{id}")
def product(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM products WHERE id = {id}")
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Product deleted successfully"}