import sqlite3

class ShopDatabase:
    def __init__(self, db_name='shop.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
    
    def create_tables(self):
        """جداول را بساز"""
        
        # جدول دسته‌بندی
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        ''')
        
        # جدول محصولات
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category_id INTEGER NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        ''')
        
        # جدول سفارش‌ها
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total_price REAL NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        ''')
        
        self.connection.commit()
        print("✅ جداول ساخته شدند")
    
    def add_category(self, name):
        """دسته‌بندی اضافه کن"""
        try:
            self.cursor.execute('''
                INSERT INTO categories (name)
                VALUES (?)
            ''', (name,))
            self.connection.commit()
            print(f"✅ دسته‌بندی '{name}' اضافه شد")
            return True
        except sqlite3.IntegrityError:
            print(f"❌ دسته‌بندی '{name}' قبل‌تر وجود داره")
            return False
    
    def add_product(self, name, category_id, price, stock):
        """محصول اضافه کن"""
        self.cursor.execute('''
            INSERT INTO products (name, category_id, price, stock)
            VALUES (?, ?, ?, ?)
        ''', (name, category_id, price, stock))
        self.connection.commit()
        print(f"✅ محصول '{name}' اضافه شد")
    
    def add_order(self, product_id, quantity, date):
        """سفارش اضافه کن"""
        # قیمت محصول رو بگیر
        self.cursor.execute('SELECT price FROM products WHERE id = ?', (product_id,))
        result = self.cursor.fetchone()
        
        if result is None:
            print("❌ محصول پیدا نشد")
            return False
        
        price = result[0]
        total_price = price * quantity
        
        self.cursor.execute('''
            INSERT INTO orders (product_id, quantity, total_price, date)
            VALUES (?, ?, ?, ?)
        ''', (product_id, quantity, total_price, date))
        
        self.connection.commit()
        print(f"✅ سفارش ثبت شد (کل: {total_price} تومان)")
        return True
    
    def close(self):
        """اتصال رو ببند"""
        self.connection.close()