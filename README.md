________________________________________
🛍️ Jumia-Like E-commerce App (Flask + MySQL + M-Pesa STK Push)
A simple yet functional Jumia-like online shop built using Flask, MySQL, and Safaricom Daraja STK Push API for seamless mobile payments.
This project demonstrates core e-commerce functionality, database connectivity, and real-world payment integration using Python.
________________________________________
🚀 Features
•	🧍 User Registration & Login (Session-based authentication)
•	🛒 Browse Products by Category (e.g., Smartphones, Clothes)
•	📦 View Single Product Details & Similar Products
•	💳 M-Pesa STK Push Payment Integration (Daraja API)
•	🗃️ MySQL Database (Users, Products, Orders)
•	🔐 Logout & Session Management
•	🧰 Flask Backend with Jinja2 Templates and Bootstrap Styling
________________________________________
🧰 Tech Stack
Component	Technology
Backend	Flask (Python)
Database	MySQL (via PyMySQL)
Frontend	HTML, CSS, Bootstrap (Jinja2 templates)
Payments	M-Pesa Daraja STK Push API
Environment	Python 3.x
Hosting (optional)	PythonAnywhere / Render
________________________________________
⚙️ Project Structure
jumia-flask/
│
├── static/                # CSS, JS, and image files
├── templates/             # HTML templates (home, single, signup, signin)
├── app.py                 # Main Flask application file
├── derrick.sql            # SQL script to create database and tables
└── README.md              # Project documentation
________________________________________
🗄️ Database Setup
1.	Open MySQL and create a new database:
2.	CREATE DATABASE testdb;
3.	USE testdb;
4.	SOURCE derrick.sql;
5.	The database includes tables such as:
o	products – stores all items with category, name, price, and image.
o	users – stores registered user information.
o	orders – for tracking purchases (optional extension).
________________________________________
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/okukucephasna/jumia-flask.git
cd jumia-flask
2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # (Windows)
source venv/bin/activate  # (Linux/Mac)
3️⃣ Install Dependencies
pip install flask pymysql requests
4️⃣ Run the Application
python app.py
Visit the app at http://127.0.0.1:5000/
________________________________________
💳 M-Pesa STK Push Integration
The app integrates with Safaricom Daraja API to trigger an STK Push for mobile payments.
STK Push Flow:
1.	User enters their phone number and amount.
2.	Flask app requests an access token using the consumer key and secret.
3.	Generates password with passkey and timestamp.
4.	Sends POST request to https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest.
5.	The user receives a push prompt on their phone to authorize the payment.
Sandbox Credentials:
•	Obtain them from Safaricom Daraja Portal.
•	Use a test phone number starting with 2547XXXXXXXX.
________________________________________
📸 Key Routes
Route	Method	Description
/	GET	Homepage with categories and products
/single/<product_id>	GET	View single product details
/signup	GET/POST	User registration
/signin	GET/POST	User login
/logout	GET	Logout user
/mpesa	POST	STK push payment route
________________________________________
🧠 Skills Demonstrated
•	Flask Routing & Template Rendering
•	MySQL Database Design (using PyMySQL)
•	Secure User Authentication & Session Handling
•	Integration with External REST APIs (Daraja)
•	Basic Frontend Design with Bootstrap
•	Handling JSON responses and error management
________________________________________
🧪 Testing
To test payments:
1.	Use your Safaricom Daraja Sandbox credentials.
2.	Enter phone number 2547XXXXXXXX and amount (e.g., 1).
3.	Check your simulator or test M-Pesa app for STK prompt confirmation.
________________________________________
👨‍💻 Author
Cephas N. Okuku
Email: okungusefa@gmail.com
GitHub: okukucephasna
LinkedIn: cephas-okuku
________________________________________
🧾 License
This project is licensed under the MIT License — feel free to use or modify it for your own learning or development.
________________________________________
