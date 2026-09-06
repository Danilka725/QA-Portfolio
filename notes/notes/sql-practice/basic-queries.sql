-- ============================================
-- БАЗОВЫЕ SQL ЗАПРОСЫ ДЛЯ QA
-- ============================================

-- 1. SELECT: Выборка данных
-- ============================================

-- Выбрать все столбцы
SELECT * FROM users;

-- Выбрать конкретные столбцы
SELECT name, email, age FROM users;

-- Выбрать уникальные значения
SELECT DISTINCT city FROM users;

-- 2. WHERE: Фильтрация
-- ============================================

-- Равенство
SELECT * FROM users WHERE age = 25;

-- Сравнение
SELECT * FROM products WHERE price > 1000;
SELECT * FROM products WHERE price < 500;

-- Диапазон
SELECT * FROM orders WHERE date BETWEEN '2026-01-01' AND '2026-12-31';

-- LIKE: Поиск по шаблону
SELECT * FROM users WHERE name LIKE 'Иван%'; -- начинается с "Иван"
SELECT * FROM users WHERE email LIKE '%@gmail.com'; -- заканчивается на "@gmail.com"

-- IN: Несколько значений
SELECT * FROM products WHERE category IN ('phones', 'laptops');

-- IS NULL: Проверка на NULL
SELECT * FROM users WHERE phone IS NULL;

-- 3. ORDER BY: Сортировка
-- ============================================

-- По возрастанию
SELECT * FROM products ORDER BY price ASC;

-- По убыванию
SELECT * FROM products ORDER BY created_at DESC;

-- По нескольким столбцам
SELECT * FROM users ORDER BY city ASC, name ASC;

-- 4. LIMIT: Ограничение количества
-- ============================================

-- Первые 10 записей
SELECT * FROM users LIMIT 10;

-- Пропустить первые 10, взять следующие 5
SELECT * FROM users LIMIT 5 OFFSET 10;

-- 5. Агрегатные функции
-- ============================================

-- COUNT: количество записей
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM orders WHERE status = 'completed';

-- SUM: сумма
SELECT SUM(price) FROM orders;

-- AVG: среднее
SELECT AVG(price) FROM products;

-- MIN/MAX: минимум/максимум
SELECT MIN(price), MAX(price) FROM products;

-- 6. GROUP BY: Группировка
-- ============================================

-- Количество пользователей по городам
SELECT city, COUNT(*) 
FROM users 
GROUP BY city;

-- Средняя цена по категориям
SELECT category, AVG(price) 
FROM products 
GROUP BY category;

-- 7. JOIN: Соединение таблиц
-- ============================================

-- INNER JOIN: только совпадающие записи
SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN: все из левой таблицы + совпадения из правой
SELECT users.name, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- RIGHT JOIN: все из правой таблицы + совпадения из левой
SELECT users.name, orders.product
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;

-- 8. Подзапросы
-- ============================================

-- Пользователи, которые сделали заказы
SELECT * FROM users
WHERE id IN (SELECT DISTINCT user_id FROM orders);

-- Товары дороже среднего
SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- 9. Практические примеры для QA
-- ============================================

-- Найти всех пользователей, зарегистрированных сегодня
SELECT * FROM users 
WHERE DATE(created_at) = CURDATE();

-- Найти заказы без товаров (битые данные)
SELECT * FROM orders
LEFT JOIN order_items ON orders.id = order_items.order_id
WHERE order_items.id IS NULL;

-- Проверить дубликаты email
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Найти пользователей без заказов
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM orders);
