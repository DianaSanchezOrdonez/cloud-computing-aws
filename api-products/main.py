from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import schemas
from uuid import UUID

app = FastAPI()

origins = ['*'] # Permite que el Api Rest se consuma desde cualquier origen

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    cursor = mydb.cursor(dictionary=True)
    query = """
        SELECT 
            p.id, p.sku, p.name, p.description, p.price, p.status,
            c.id AS category_id, c.name AS category_name
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"products": result}

@app.get("/products/{id}")
def product(id: UUID):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (str(id),))
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
    category_id = item.category_id if item.category_id else None
    status = item.status
    cursor = mydb.cursor(dictionary=True)
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

@app.put("/products/{id}")
def product(id: UUID, item:schemas.Product):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    sku = item.sku
    name = item.name
    description = item.description
    price = item.price
    category_id = item.category_id if item.category_id else None
    status = item.status
    cursor = mydb.cursor(dictionary=True)
    sql = "UPDATE products SET sku=%s, name=%s, description=%s, price=%s, category_id=%s, status=%s WHERE id=%s"
    val = (sku, name, description, price, category_id, status, str(id))
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Product modified successfully"}

@app.delete("/products/{id}")
def product(id: UUID):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("DELETE FROM products WHERE id = %s", (str(id),))
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Product deleted successfully"}

# Categories 
@app.get("/categories")
def categories():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"categories": result}