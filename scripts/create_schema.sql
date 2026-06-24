CREATE TABLE customers(

 id SERIAL PRIMARY KEY,

 name VARCHAR(100),

 country VARCHAR(50)

);

CREATE TABLE orders(

 id SERIAL PRIMARY KEY,

 customer_id INT,

 amount NUMERIC,

 order_date DATE

);