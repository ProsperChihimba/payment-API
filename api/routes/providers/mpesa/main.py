from .portalsdk import APIContext, APIMethodType, APIRequest
from time import sleep
from flask import jsonify


def main_mpesa(amount, transaction_reference, customer_code):
    # Public key on the API listener used to encrypt keys
    public_key = '' #public key
    # Create Context with API to request a Session ID
    api_context = APIContext()
    # Api key
    api_context.api_key = '' #private key
    # Public key
    api_context.public_key = public_key
    # Use ssl/https
    api_context.ssl = True
    # Method type (can be GET/POST/PUT)
    api_context.method_type = APIMethodType.GET
    # API address
    api_context.address = 'openapi.m-pesa.com'
    # API Port
    api_context.port = 443
    # API Path
    api_context.path = '/sandbox/ipg/v2/vodacomTZN/getSession/'

    # Add/update headers
    api_context.add_header('Origin', '*')

    # Parameters can be added to the call as well that on POST will be in JSON format and on GET will be URL parameters
    # api_context.add_parameter('key', 'value')

    #Do the API call and put result in a response packet
    api_request = APIRequest(api_context)

    # Do the API call and put result in a response packet
    result = None
    try:
        result = api_request.execute()
    except Exception as e:
        return jsonify({"Status": "Server Error", "message": "There is an internal error, please contact customer service"}), 500
        #print('Call Failed: ' + e)

    if result is None:
        return jsonify({"Status": "Server Error", "message": "There is an internal error, please contact customer service"}), 500
        #raise Exception('SessionKey call failed to get result. Please check.')

    # Display results
    # print(result.status_code)
    # print(result.headers)
    # print(result.body)

    # The above call issued a sessionID which will be used as the API key in calls that needs the sessionID
    api_context = APIContext()
    api_context.api_key = result.body['output_SessionID']
    api_context.public_key = public_key
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    api_context.address = 'openapi.m-pesa.com'
    api_context.port = 443
    api_context.path = '/sandbox/ipg/v2/vodacomTZN/c2bPayment/singleStage/'

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_Amount', int(amount))
    api_context.add_parameter('input_Country', 'TZN')
    api_context.add_parameter('input_Currency', 'TZS')
    api_context.add_parameter('input_CustomerMSISDN', '255769432516')
    api_context.add_parameter('input_ServiceProviderCode', '000000')
    api_context.add_parameter('input_ThirdPartyConversationID', transaction_reference)
    api_context.add_parameter('input_TransactionReference', customer_code)
    api_context.add_parameter('input_PurchasedItemsDesc', 'Data')
    
    api_request = APIRequest(api_context)

    # SessionID can take up to 30 seconds to become 'live' in the system and will be invalid until it is
    sleep(30)

    result = None
    try:
        result = api_request.execute()
    except Exception as e:
        return jsonify({"Status": "Server Error", "message": "There is an internal error, please contact customer service"}), 500
        #print('Call Failed: ' + e)

    if result is None:
        return jsonify({"Status": "Server Error", "message": "There is an internal error, please contact customer service"}), 500
        #raise Exception('API call failed to get result. Please check.')

    #print(result.status_code)
    #print(result.headers)
    #print(result.body)
    return result #.body    

# if __name__ == '__main__':
#     main()