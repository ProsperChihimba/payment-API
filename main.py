import logging
from flask import Flask, jsonify
from api.config.config import ProductionConfig, TestingConfig, DevelopmentConfig
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp
from api.routes.transaction import transaction_routes
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

#cheaking the enviroment the application is running
if app.config["ENV"] == "production":
    app_config = ProductionConfig
elif app.config["ENV"] == "testing":
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

#defining flask-limiter
limiter = Limiter(
    app,
    key_func=get_remote_address
)

#limit all endpoints
limiter.limit("20 per minute")(transaction_routes)

#registering api endpoints routes in blueprint from routes directory
app.register_blueprint(transaction_routes, url_prefix='/charge')

#start global http configurations, handling errors
@app.after_request
def add_header(response):
    return response

@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)

@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)

@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)

@app.errorhandler(401)
def not_authorized(e):
    logging.error(e)
    return response_with(resp.UNAUTHORIZED_401)

@app.errorhandler(405)
def method_not_allowed(e):
    logging.error(e)
    return response_with(resp.METHOD_NOT_ALLOWED_405)

@app.errorhandler(429)
def too_many_requests(e):
    logging.error(e)
    return response_with(resp.TOO_MANY_REQUESTS_429)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main.py__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)