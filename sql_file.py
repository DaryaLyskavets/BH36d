import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (24) UNIQUE NOT NULL,
    is_published BOOLEAN DEFAULT(true)
    );
''')
conn.commit()

# cur.executemany('''
#     INSERT INTO categories(name)
#     VALUES(?);
# ''', (('Drinks', ) ,('Food', ) ,('Toys', ) ,('Clothing', )))
# conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (36), 
    description VARCHAR (140),
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
    );
''')
conn.commit()
#
# cur.executemany('''
#     INSERT INTO products(title, description, category_id)
#     VALUES(?,?,?);
# ''', (('water', 'sparling', 1),('tea', 'green', 1),('pasta', 'spagetti', 2),('dolls', 'barbie', 3),
#       ('puzzle', 'wood', 3), ('meat', 'beaf', 2)))
# conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (10)
    );
''')
conn.commit()

# cur.executemany('''
#     INSERT INTO statuses (name)
#     VALUES(?);
# ''', (('in_stock', ),('ordered', ),('delivery_expected', )))
# conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (24),
    email VARCHAR (24) UNIQUE
    );
''')
conn.commit()

# cur.executemany('''
#     INSERT INTO users (name, email)
#     VALUES (?,?);
# ''', (('almi', 'almi@info.com'), ('green', 'green@info.com'), ('sosedi', 'sosedi@info.com'),
#       ('martinn', 'martin@info.com')))
# conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(id)
    );
''')
conn.commit()

# cur.executemany('''
#     INSERT INTO orders (user_id, status_id)
#     VALUES (?,?);
#     ''', ((1, 1), (1, 2),(2, 3), (2, 2), (3, 1), (4, 2)))
# conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
    FOREIGN KEY (product_id) REFERENCES products(id)
    );
''')

# cur.executemany('''
#     INSERT INTO order_items(order_id, product_id)
#     VALUES (?,?);
# ''', ((5, 6),(4, 3),(1, 2), (6, 4), (6, 3), (2, 1), (4, 4), (5, 5)))
# conn.commit()

cur.execute('''
    SELECT categories.name, products.title, users.name
    FROM categories, orders
    JOIN products ON categories.id = products.category_id
    JOIN users ON users.id = orders.user_id
    JOIN statuses ON statuses.id = orders.status_id 
    WHERE statuses.name = 'in_stock' and users.name = 'almi'
     
''')
print(cur.fetchall())
