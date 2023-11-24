import sqlite3

from model.product import Product


def create_connection():
    try:
        connection = sqlite3.connect('itecs_database.db')
        return connection
    except sqlite3.Error as e:
        print(e)
    return None


def create_table():
    query = '''
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            price INTEGER,
            author TEXT,
            date TEXT,
            category TEXT,
            description TEXT
      );
    '''
    table_connection = create_connection()
    if table_connection:
        cursor = table_connection.cursor()
        cursor.execute(query)
        table_connection.commit()
        table_connection.close()


def write_product_to_db(product):
    query = '''
        INSERT INTO products (name, price, author, date, category, description)
        VALUES (?, ?, ?, ?, ?, ?)
    '''

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, (
                product.name,
                product.price,
                product.author,
                product.date,
                product.category,
                product.description
            ))
            connection.commit()
            print("Product inserted successfully!")
        except sqlite3.Error as e:
            print("Error inserting product:", e)

        connection.close()


def read_products_from_db():
    query = '''
        SELECT name, price, author, date, category, description
        FROM products
    '''

    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            rows = cursor.fetchall()

            products = []
            for row in rows:
                product = Product()
                product.name = row[0]
                product.price = row[1]
                product.author = row[2]
                product.date = row[3]
                product.category = row[4]
                product.description = row[5]
                products.append(product)

            return products
        except sqlite3.Error as e:
            print("Error reading books:", e)

        connection.close()
        return None
