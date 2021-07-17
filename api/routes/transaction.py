from flask import Blueprint, request, g, jsonify
from flask_httpauth import HTTPTokenAuth
from datetime import datetime
from api.utils.responses import response_with
from api.utils import responses as resp
from api.utils.database import db
from api.models.merchant import Merchant, MerchantSchema
from api.models.channel import Channel, ChannelSchema
from api.models.transaction import Transaction, TransactionSchema
from api.utils.randoms import random_string, random_number
from api.routes.providers.mpesa.main import main_mpesa
from api.routes.providers.beemsms import send_sms

#registering transaction route to the blueprint, which is used to create 
#transaction/charge/ endpoint in main.py
transaction_routes = Blueprint("transaction_routes", __name__)
#using HTTPAUTH libraly
auth = HTTPTokenAuth(scheme='Bearer')


#this function is used to get the Bearer token from the API call and verify
#the token, if token is valid it returns the token
@auth.verify_token
def merchants(merchant):
    merchant_fetch = Merchant.query.all()
    merchant_schema = MerchantSchema(many=True)
    merchants = merchant_schema.dump(merchant_fetch)
    for s in range(len(merchants)):
        if merchants[s]['private_key'] == merchant:
            return merchants[s]['private_key']


#the function for charge endpoint it requires authorization to be accessed
@transaction_routes.route('/', methods=['POST'])
@auth.login_required
def create_transaction():
    try:
        data = request.get_json()
        #making sure the required fields in the API call are not empty
        if data['currency'] == "":
            return response_with(resp.INVALID_INPUT_422)
        elif data['amount'] == "":
            return response_with(resp.INVALID_INPUT_422)
        elif data['email'] == "":
            return response_with(resp.INVALID_INPUT_422)
        elif data['number_used'] == "":
            return response_with(resp.INVALID_INPUT_422)
        elif data['channel'] == "":
            return response_with(resp.INVALID_INPUT_422)
        #if the fields are not empty
        else:
            merchant_key = auth.current_user() #get the token from the API call which is returned in verify token function
            channel_name = data['channel']
            #get merchant id
            filter_merchant_id = Merchant.query.filter_by(private_key=merchant_key).first()
            merchant_id = filter_merchant_id.id
            #get channel id
            filter_channel_id = Channel.query.filter_by(provider_name=channel_name).first()
            channel_id = filter_channel_id.id
            #get transaction reference from randoms model in utils directory
            transaction_reference = random_string(14, 7)
            transaction_date = str(datetime.now().strftime("%Y-%m-%d, %H:%M"))
            customer_id = random_number(5)
            customer_code = random_string(8, 4)


            #send payment request to mobile-money operators for the mean time is Vodacom
            mpesa_pay = main_mpesa(data['amount'], transaction_reference, customer_code)
            if mpesa_pay.body['output_ResponseCode'] == 'INS-0':
                transaction_status = "Success"
                transaction_message = "Transaction was completed successfully"

                #send SMS to the customer when the payment was succesfully
                send_txt = send_sms(data['number_used'], f'You have successfully made {data["amount"]} transaction to Payment API.')
            else:
                transaction_status = "Pedding"
                transaction_message = "Transaction is in progress"

                #send SMS to the customer when the payment was not succesfully
                send_txt = send_sms(data['number_used'], f'Your {data["amount"]} transaction had an error please try again.')


            #update the data from the request
            data.update(
                {
                    "transaction_reference": transaction_reference,
                    "merchant_id": merchant_id,
                    "channel_id": channel_id,
                    "transaction_date": transaction_date,
                    "status": transaction_status,
                    "message": transaction_message,
                    "customer_id": customer_id,
                    "customer_code": customer_code
                })
            #post data to the database
            transaction_schema = TransactionSchema()
            transaction = transaction_schema.load(data)
            result = transaction_schema.dump(transaction.create())
            #get the return values after sucessful request
            filter_transaction = Transaction.query.filter_by(transaction_reference=transaction_reference).first()
            return response_with(resp.SUCCESS_201, value=
            {
                "status": filter_transaction.status,
                "message": filter_transaction.message,
                "reference": filter_transaction.transaction_reference,
                "amount": filter_transaction.amount
            })
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)