from database import ShopDatabase

# Database رو شروع کن
db = ShopDatabase()

print("\n" + "="*50)
print("اضافه کردن دسته‌بندی‌ها:")
print("="*50)

# دسته‌بندی‌ها رو اضافه کن
db.add_category("لوازم الکترونیکی")
db.add_category("کتاب")
db.add_category("لباس")

print("\n" + "="*50)
print("اضافه کردن محصولات:")
print("="*50)

# محصولات رو اضافه کن
db.add_product("گوشی", 1, 500000, 10)
db.add_product("لپ‌تاپ", 1, 2000000, 5)
db.add_product("کتاب Python", 2, 150000, 20)
db.add_product("تی‌شرت", 3, 80000, 30)

print("\n" + "="*50)
print("ثبت سفارش‌ها:")
print("="*50)

# سفارش‌ها رو ثبت کن
db.add_order(1, 2, "2024-01-20")  # 2 گوشی
db.add_order(2, 1, "2024-01-21")  # 1 لپ‌تاپ
db.add_order(3, 3, "2024-01-22")  # 3 کتاب
db.add_order(4, 5, "2024-01-23")  # 5 تی‌شرت

db.close()
print("\n✅ تمام داده‌ها اضافه شدند")