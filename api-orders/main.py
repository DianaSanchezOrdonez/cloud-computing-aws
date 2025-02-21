from fastapi import FastAPI
import mysql.connector
import schemas
from uuid import UUID

app = FastAPI()

host_name = "172.31.85.15" # IPv4 privada de "MV BD"
port_number = "8007"
user_name = "root"
password_db = "utec"
database_name = "bd_api_orders"  

# Get echo test for load balancer's health check
@app.get("/")
def echo_test():
    return {"message": "Echo Test OK"}

@app.get("/orders")
def orders():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"orders": result}

@app.get("/orders/{id}")
def order(id: UUID):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders WHERE id = %s", (str(id),))
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    return {"order": result}

@app.post("/orders")
def order(item:schemas.Order):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cliente_id = item.cliente_id
    status = item.status
    cursor = mydb.cursor(dictionary=True)
    sql = """
        INSERT INTO orders (cliente_id, status)
        VALUES (%s, %s)
    """
    val = (cliente_id, status)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Order added successfully"}

@app.put("/orders/{id}")
def order(id: UUID, item:schemas.Order):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cliente_id = item.cliente_id
    status = item.status
    cursor = mydb.cursor(dictionary=True)
    sql = "UPDATE orders SET cliente_id=%s, status=%s WHERE id=%s"
    val = (cliente_id, status, str(id))
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Order modified successfully"}

@app.delete("/orders/{id}")
def order(id: UUID):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("DELETE FROM orders WHERE id = %s", (str(id),))
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Order deleted successfully"}

# CRUD Order Items
@app.get("/order_items")
def order_items():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM order_items")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"order_items": result}

@app.post("/order_items")
def order_item(item:schemas.OrderItem):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    order_id = item.order_id
    product_id = item.product_id
    quantity = item.quantity
    unit_price = item.unit_price
    total_price = item.unit_price * item.quantity
    cursor = mydb.cursor(dictionary=True)
    sql = """
    INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price)
    VALUES (%s, %s, %s, %s, %s)
    """
    val = (order_id, product_id, quantity, unit_price, total_price)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Order item added successfully"}

@app.put("/order_items/{id}")
def order_item(id: UUID, item:schemas.OrderItem):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    order_id = item.order_id
    product_id = item.product_id
    quantity = item.quantity
    unit_price = item.unit_price
    total_price = item.unit_price * item.quantity
    cursor = mydb.cursor(dictionary=True)
    sql = "UPDATE order_items SET order_id=%s, product_id=%s, quantity=%s, unit_price=%s, total_price=%s WHERE id=%s"
    val = (order_id, product_id, quantity, unit_price, total_price, str(id))
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Order item modified successfully"}

@app.delete("/order_items/{id}")
def order_item(id: UUID):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("DELETE FROM order_items WHERE id = %s", (str(id),))
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Order item deleted successfully"}