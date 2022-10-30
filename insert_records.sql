-- DML
-- CRUD - create, read, update, delete
USE cocoashop;
INSERT INTO customers(forename, surname, phone, address, email, dob) VALUES 
("John", "Smith", "0123456789", "123 Fake St.", "jsmith@example.com", "2000-10-25"),
("Jane", "Roberts", "0143258679", "456 Not Real Ave.", "janer@mail.com", "2005-7-15"),
("Alice", "Jones", "1043258769", "789 Imaginary Ln.", "alicejones@e.mail", "1998-07-03"),
("Kelsie", "Hayter", "2413685790", "135 Made-up Blvd.", "khayter95@mail.org", "1995-02-26"),
("Darell", "Woods", "9831245670", "246 False Rd.", "darellwoods@email.co.uk", "2001-11-16");

INSERT INTO truffles(category_id, title, truffle_description, unit_price, in_stock) VALUES
(3, "Truffle with zero added sugar 30g", "Delicious milk chocolate truffle with zero added sugar. With surprising flavor, ideal for those who have dietary restrictions!", 2.20, 20),
(3, "White truffle with zero added sugar 30g", "Delicious white chocolate truffle with zero added sugar. With surprising flavor, you will fall in love!", 2.20, 16),
(1, "Strawberry yoghurt truffle 30g", "Delicious milk chocolate truffle with strawberry yogurt filling. For each truffle sold, a part of the value is donated to a cancer hospital. Prevention is the best way!", 2.20, 30),
(1, "Black forest artisan truffle 30g", "Milk chocolate truffle with black forest flavor filling. There's nothing better than grandma's recipe, in the shape of a truffle, so...", 2.20, 30),
(1, "Artisanal truffle petit gateau 30g", "To bring this dessert to our truffle, we created a product made with a 34% cocoa shell and a white chocolate shell with a creamy filling. A combination of amazing flavors!", 2.20, 30),
(1, "Artisanal marula truffle 30g", "Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, milk chocolate and marula form a delicious combination.", 2.20, 30),
(1, "Lanut truffle 30g", "Milk chocolate truffle with creamy hazelnut filling, a delight that only CocoaCris knows how to make!", 2.20, 30),
(1, "Artisanal truffle grancherie 30g", "Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, milk chocolate and cherry form a delicious combination.", 2.20, 30),
(1, "Artisanal truffle condensed milk 30g", "Irresistible handmade milk chocolate truffle with condensed milk flavor filling. Try it!", 2.00, 30),
(1, "30g banoffee artisanal truffle", "Milk and white chocolate truffle with banoffee flavor. A delight that only CocoaCris knows how to make!!", 2.20, 30),
(1, "Artisanal truffle chocolate cake 30g", "Milk chocolate truffle filled with chocolate cake flavor, a delight that only Cacau Show knows how to make!", 2.20, 30),
(1, "Coconut truffle 30g", "Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, milk chocolate and coconut form a delicious combination.", 2.00, 30),
(1, "White truffle 30g", "Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, the shell and the filling, both made of white chocolate, form a delicious combination.", 2.00, 30),
(1, "Truffle milk pudding 30g", "Milk chocolate truffle with pudding flavor filling. There's nothing better than grandma's recipe, in the shape of a truffle, so...", 2.00, 30),
(1, "Mezzo truffle 30g", "Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, milk and white chocolate form a delicious combination.", 2.00, 30),
(1, "Coconut manjar truffle 30g", "White chocolate truffle with coconut manjar flavor filling. For you to remember the taste of sweets that only bring good memories!", 2.00, 30),
(1, "Traditional truffle 30g", "Slightly firm on the outside, with a soft filling and a delicious flavor on the inside. Here, the milk chocolate cone and the traditional truffle filling form a delicious combination.", 2.00, 30),
(2, "Blessed truffle cacao 55% cocoa 30g", "Slightly firm on the outside, with a soft filling and a very characteristic flavor on the inside. Here, the cone and the filling, both made of intense chocolate with 55% cocoa, form a delicious combination.", 2.00, 30),
(1, "Passion fruit truffle 30g", "Slightly firm on the outside, with a soft filling and a delicious flavor on the inside. Here, milk chocolate and passion fruit form a delicious combination.", 2.00, 30),
(1, "Passion fruit truffle 30g", "Slightly firm on the outside, with a soft filling and a delicious flavor on the inside. Here, milk chocolate and passion fruit form a delicious combination.", 2.00, 30),
(1, "Trio napolitano truffle 30g", "Milk chocolate truffle with Neapolitan mousse filling. For you to remember the taste of sweets that only bring good memories!", 2.00, 30),
(2, "Blessed truffle cacao 85% cocoa 13.5g", "Delicious 85% cocoa chocolate truffle with intense chocolate truffle filling. More cocoa, perfect for you!", 1.00, 30),
(2, "Blessed truffle cacao 70% cocoa 13.5g", "Delicious 70% cocoa chocolate truffle filled with 55% cocoa gourmet chocolate. Ideal for those who like the most intense flavors!", 1.00, 30),
(1, "Strawberry truffle 30g", "Slightly firm on the outside, with a soft filling and a very characteristic and delicious flavor on the inside. Here, milk chocolate and strawberry form a delicious combination.", 2.00, 30),
(1, "Love apple truffle 30g", "Milk chocolate truffle with apple flavor filling. A delight that only Cacau Show knows how to make!", 2.00, 30),
(1, "Mint truffle 30g", "Slightly firm on the outside, with a very characteristic flavor on the inside. Here, milk chocolate and mint refreshment form a delicious combination.", 2.00, 30),
(1, "Paçoca truffle 30g", "Milk chocolate truffle with peanut cream filling. It's too good, sir!", 2.00, 30),
(1, "13.5g peanut lanut truffle", "Milk chocolate truffle with peanut cream filling. A small portion with high doses of happiness!", 1.00, 30);

INSERT INTO categories(title) VALUES
("dairy"),
("dairy-free"),
("non-suggar");

INSERT INTO orders(customer_id, order_date) VALUES
(1, "2022-10-24"),
(2, "2022-10-01"),
(3, "2022-09-18"),
(1, "2022-07-03"),
(5, "2022-06-14");

INSERT INTO orders_truffles(order_id, truffle_id, quantity) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 1, 1),
(3, 2, 5),
(3, 1, 7),
(3, 5, 2),
(4, 2, 4),
(4, 3, 1),
(5, 5, 5);
