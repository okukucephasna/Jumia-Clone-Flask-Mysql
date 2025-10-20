from flask import*
import pymysql

app = Flask(__name__)

app.secret_key = "AW_r%@jN*HU4AW_r%@jN*HU4AW_r%@jN*HU4"
print(__name__)


@app.route('/')
def home():
    # Establish a database connection
    connection = pymysql.connect(host='localhost', user='root', password='',
                                 database='testdb')
   # SQL 1  - Select Products by Smartphone Category**
    sqlSmartphone = "SELECT * FROM products where product_category = 'Smartphone'"
    sqlClothes = "SELECT * FROM products where product_category = 'Clothes'"
    
    
    # Cursor - Used to run/execute above SQL**
    cursorSmartphone = connection.cursor()
    cursorClothes = connection.cursor()
    
   # Execute SQL**
    cursorSmartphone.execute(sqlSmartphone)
    cursorClothes.execute(sqlClothes)
    
    # Fetch Rows**
    smartphones = cursorSmartphone.fetchall()
    clothes = cursorClothes.fetchall()


    # TODO SQL 2  - Smartphones**
    
    # Return smartphones to **home.html**
    return render_template('home.html')
# Get Single Item, Note this route has an product_id, It displays a product based on product_id
@app.route('/single/<product_id>')
def single(product_id):
    # Establish a dbase connection
    connection = pymysql.connect(host='localhost', user='root', password='',
                                database='testdb')
				 
    # Create SQL  - %s is a placeholder, which will take the actual ID during Query Execution.
    sql1 = "SELECT * FROM products WHERE product_id = %s"

    # Cursor - Used to run/execute above SQL
    cursor1 = connection.cursor()

    # Execute SQL providing product_id - NB: Sql had a placeholder in the Where clause thats why we provide the product_id
    cursor1.execute(sql1, (product_id))

    # Get the product retrieved 
    product = cursor1.fetchone()
    
    # Return the product to single.html
    category = product[4]  # Category is at colm 4

    # We now query to Find Others Product in this category, We LImit to only 4
    # ADD THIS
    sql2 = "SELECT * FROM products where product_category = %s LIMIT 4"
    cursor2 = connection.cursor()
    cursor2.execute(sql2, (category))
    similar = cursor2.fetchall()
    # Now we have similar products

    # We now return the Product and similar Products 
    return render_template('single.html', product=product, similar = similar)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            phone = request.form['phone']
            password1 = request.form['password1']
            password2 = request.form['password2']

            if len(password1) < 8:
                return render_template('signup.html', error='Password must more than 8 xters')
            elif password1 != password2:
                return render_template('signup.html', error='Password Do Not Match')
            else:
                connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='testdb')
                sql = ''' 
                     insert into users(username, password, phone, email) 
                     values(%s, %s, %s, %s)
                 '''
                cursor = connection.cursor()
                cursor.execute(sql, (username, password1, phone, email))
                connection.commit()
                # import sms
                # sms.send_sms(phone, "Thank you for Registering")
                return render_template('signup.html', success='Registered Successfully')

    else:
        return render_template('signup.html')
                


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='testdb')

        sql = '''
           select * from users where username = %s and password = %s
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error='Invalid Credentials')
        else:
            session['key'] = username  # link the session key with username
            return redirect('/')  # redirect to product Default route
    else:
        return render_template('signin.html')




    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signin')

import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/mpesa', methods=['POST', 'GET'])
def mpesa_payment():
    if request.method == 'POST':
        phone = str(request.form['phone'])
        amount = str(request.form['amount'])
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
               '<a href="/" class="btn btn-dark btn-sm">Back to Products</a>'



if __name__ == '__main__':
    app.run(debug=True)