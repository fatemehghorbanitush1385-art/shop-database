# 🏪 Shop Database Project

سیستم مدیریت فروشگاه با **Python** و **SQLite**.

---

## ✨ ویژگی‌ها

- ✅ مدیریت دسته‌بندی‌ها
- ✅ مدیریت محصولات
- ✅ ثبت سفارش‌ها
- ✅ JOIN جداول
- ✅ GROUP BY و Aggregate Functions
- ✅ تحلیل فروش و درآمد

---

## 📊 جداول

### Categories
- id, name

### Products
- id, name, category_id, price, stock

### Orders
- id, product_id, quantity, total_price, date

---

## 📂 فایل‌ها

- `database.py` - کلاس Database
- `insert_shop_data.py` - اضافه کردن داده‌ها
- `shop_queries.py` - Queries و تحلیل

---

## 🚀 اجرا

```bash
python insert_shop_data.py
python shop_queries.py
```

---

## 📈 Queries شامل

- JOIN: محصولات با دسته‌بندی
- GROUP BY: سفارش‌ها برای هر محصول
- SUM: درآمد هر دسته‌بندی
- ORDER BY: بیشترین فروش
- COUNT: تعداد سفارش‌ها

---

**نویسنده:** Fatemeh Ghorbanitush