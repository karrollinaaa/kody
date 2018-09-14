DROP TABLE IF EXISTS tbCustomers;
CREATE TABLE tbCustomers (
	customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer imie TEXT NOT NULL,
    adress TEXT DEFAULT
);

DROP TABLE IF EXISTS tbOrders;
CREATE TABLE tbOrders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    subscription_id INTEGER, 
    purchase_date DATE,
    FOREGIN KEY (customer_id) REFERENCES tbCustomers(customer_id)
    FOREGIN KEY (subscription_id) REFERENCES tbSubcriptions(subscription_id)
);

DROP TABLE IF EXISTS tbSubcriptions;
CREATE TABLE tbSubcriptions (
    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    price_per_month DECIMAL,
    subscription_length TEXT
);
