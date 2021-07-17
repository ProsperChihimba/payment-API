from flask import make_response, jsonify

#defining all of the responses to be returned in API calls
INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "Status": "invalidField",
    "message": "Invalid fields found"
}

INVALID_INPUT_422 = {
    "http_code": 422,
    "Status": "Invalid Input",
    "message": "Please try to cheack well your parameters"
}

METHOD_NOT_ALLOWED_405 = {
    "http_code": 405,
    "Status": "Method Not Allowed",
    "message": "The method is not allowed for the requested URL."
}

MISSING_PARAMETERS_422 ={
    "http_code": 422,
    "Status": "Missing Parameter",
    "message": "Missing Parameters"
}

BAD_REQUEST_400 = {
    "http_code": 400,
    "Status": "badRequest",
    "message": "Bad Request"
}

SERVER_ERROR_500 = {
    "http_code": 500,
    "Status": "Server Error",
    "message": "There is an internal error, please contact customer service"
}

SERVER_ERROR_404 = {
    "http_code": 404,
    "Status": "Resource Not Found",
    "message": "Please try to cheack well the resourse your requesting"
}

UNAUTHORIZED_401 = {
    "http_code": 401,
    "Status": "Not Authorized",
    "message": "You are not authorized to execute this."
}

FORBIDDEN_403 = {
    "http_code": 403,
    "Status": "Forbidden",
    "message": "You don't have permission to access this resource"
}

SUCCESS_200 = {
    "http_code": 200,
    "Status": "success"
}

SUCCESS_201 = {
    "http_code": 201,
    "Status": "success"
}

SUCCESS_204 = {
    "http_code": 204,
    "Status": "success"
}

TOO_MANY_REQUESTS_429 = {
    "http_code": 429,
    "Status": "Too Many Requests",
    "message": "You have made too many requests"
}

#initialize the responses
def response_with(response, value=None, message=None, error=None, headers={}, pagination=None):
    result={}
    if value is not None:
        result.update(value)
    
    if response.get('message', None) is not None:
        result.update({'message': response['message']})
    
    result.update({'Status': response['Status']})
    
    if error is not None:
        result.update({'errors': error})
    
    if pagination is not None:
        result.update({'pagination': pagination})
    
    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Payment API'})

    return make_response(jsonify(result), response['http_code'], headers)