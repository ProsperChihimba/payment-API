# Payment API using Beem SMS
This is an all-in-one payment API that help’s businesses, developers seeking to accept digital payments from customers willing to pay via card, mobile-money-operators. This help’s merchants save time from having to multi-register and undergo legal processes for every mobile money operator. It's Stripe for East Africa.
Here is our Pitch https://www.youtube.com/watch?v=G2XSjy0yw5g

This API uses Beem SMS API to send text messages to customers who have made a transaction through the API. It sends a successfully transaction message or declined transaction message.
This API uses Vodacom OpenAPI to make a demo transaction to Vodacom users only.
In the future the API will imprement service to make payment in the web by using Beem payment checkout API

Here is the documentation of the API<br><br>

# OVERVIEW <br>
Charge your customer direct from your sever side by making a request to Payment API with required paramenters.<br><br>


# AUTHENTICATION<br>
Authenticate your API calls by including your secret key in the Authorization header of every request you make.<br><br>


# PASS CUSTOMER INFORMATIONS<br>
To make a transaction you will need to pass customer information such as (phone_number, amount, provider_name, Email, amount, first_name, last_name and etc). Customer names are optional. The request must be made with private key. Here are full list of paramenters and their meaning.<br>

Amount - This is an amount in Tanzania shiling(Required).<br>
Customer Number	- This is a Vodacom customer phone number which will be used to charge a custoomer(Required).<br>
Email - This is a customer Email(Required).<br>
Channel - Mobile-provider name which is used by the customer phone number(which is Vodacom) (Required).<br>
First name - This is a first name of customer(Optional).<br>
Last name - This is a last name of customer(Optional).<br><br>


# MAKE A REQUEST<br>
Here is an example of a POST request to charge a customer.<br>

<span style="color:rgb(250, 120, 45)">curl</span> --location --request <span style="color:rgb(194, 247, 237)">POST</span> <span style="color:rgb(173, 219, 103)">'http://127.0.0.1:5000/transaction/charge/'</span> \ <br>
--header <span style="color:rgb(173, 219, 103)">'Authorization: Bearer sk_test_shdjkhdj827391nV4Lid'</span> \ <br>
--header <span style="color:rgb(173, 219, 103)">'Content-Type: application/json'</span> \ <br>
--data-raw <span style="color:rgb(173, 219, 103)">'{ <br>
    &nbsp;&nbsp;&nbsp; "amount": 5000, <br>
    &nbsp;&nbsp;&nbsp; "currency": "TSH", <br>
    &nbsp;&nbsp;&nbsp; "first_name": "user", <br>
    &nbsp;&nbsp;&nbsp; "last_name": "user", <br>
    &nbsp;&nbsp;&nbsp; "email": "user@user.com", <br>
    &nbsp;&nbsp;&nbsp; "number_used": "0763803078", <br>
    &nbsp;&nbsp;&nbsp; "channel": "Vodacom" <br>
&nbsp;&nbsp;&nbsp;}'</span>
   
After making a POST request API will return a JSON data with transaction data

# NOTICE: <br>
The returned transaction data does not mean that the transaction was made succesfully, you have to verify that the status of transaction is Success(this identifies that the transaction was completed). Please read down the table of Status and their meaning.

Here is the sample of returned JSON data.<br>
{<br>
    "status": "success",<br>
    "message": "Transaction is completed successfully",<br>
    "reference": adz49dS428b7kbDTdG4MN,<br>
    "amount": 5000<br>
}<br><br>


# RETURNED STATUS
Success - Transaction is completed succesfully
Pending - Transaction is in progress and is not completed yet
Uncomplete - Transaction is not completed yet for customer to pay<br><br>


# HTTP STATUS<br>
200, 201 (Success) - Request was successful and intended action was carried out. Note that we will always send a 200 if a charge or verify request was made. Do check the data object to know how the charge went (i.e. successful or failed).

401 (Not Authorized) - The request sent was not authorized due not invalid Secret Key or more.

422 (Invalid Input) - This may be caused by passing empty some fieldes which are required or by incorrect paramenter.

404 (Resource Not Found) - The resource your requesting is not available.

400	(Bad Request) - An error happened in the client side

500 (Server Error) - Request denied due to error in Shoket Server.

405 (Method Not Allowed) - The method used in the request is not allowed for the requested URL.

403 (Forbidden) - You don't have permission to access the requested resource

429 (Too Many Requests) - You have made too many requests. Please look at our late limiting description <br><br>


# HOW TO INSTALL REQUIREMENTS <br>
You can use PIP to install the requirements<br>
Type # pip install -r requirements.txt in your command line
