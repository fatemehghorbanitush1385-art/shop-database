import sqlite3

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()

print("\n" + "="*70)
print("۱. تمام محصولات با دسته‌بندی:")
print("="*70)

cursor.execute('''
    SELECT products.name, categories.name as category, products.price, products.stock
    FROM products
    JOIN categories ON products.category_id = categories.id
''')

results = cursor.fetchall()
for row in results:
    print(f"محصول: {row[0]} | دسته: {row[1]} | قیمت: {row[2]} | موجودی: {row[3]}")

print("\n" + "="*70)
print("۲. تعداد سفارش‌ها برای هر محصول:")
print("="*70)

cursor.execute('''
    SELECT products.name, COUNT(orders.id) as order_count, SUM(orders.quantity) as total_quantity
    FROM products
    LEFT JOIN orders ON products.id = orders.product_id
    GROUP BY products.name
''')

results = cursor.fetchall()
for row in results:
    order_count = row[1] if row[1] else 0
    total_qty = row[2] if row[2] else 0
    print(f"محصول: {row[0]} | تعداد سفارش: {order_count} | کل تعداد: {total_qty}")

print("\n" + "="*70)
print("۳. کل درآمد از هر دسته‌بندی:")
print("="*70)

cursor.execute('''
    SELECT categories.name, SUM(orders.total_price) as total_revenue
    FROM categories
    LEFT JOIN products ON categories.id = products.category_id
    LEFT JOIN orders ON products.id = orders.product_id
    GROUP BY categories.name
''')

results = cursor.fetchall()
for row in results:
    revenue = row[1] if row[1] else 0
    print(f"دسته: {row[0]} | درآمد: {revenue} تومان")

print("\n" + "="*70)
print("۴. بیشترین فروش (ترتیب از بیشتر):")
print("="*70)

cursor.execute('''
    SELECT products.name, SUM(orders.total_price) as total_revenue
    FROM products
    LEFT JOIN orders ON products.id = orders.product_id
    GROUP BY products.name
    ORDER BY total_revenue DESC
''')

results = cursor.fetchall()
for row in results:
    revenue = row[1] if row[1] else 0
    print(f"محصول: {row[0]} | درآمد: {revenue} تومان")

print("\n" + "="*70)
print("۵. تعداد کل سفارش‌ها:")
print("="*70)

cursor.execute('SELECT COUNT(*) as total_orders FROM orders')
result = cursor.fetchone()
print(f"کل سفارش‌ها: {result[0]}")

print("\n" + "="*70)
print("۶. کل درآمد فروشگاه:")
print("="*70)

cursor.execute('SELECT SUM(total_price) as total_revenue FROM orders')
result = cursor.fetchone()
total = result[0] if result[0] else 0
print(f"کل درآمد: {total} تومان")

connection.close()