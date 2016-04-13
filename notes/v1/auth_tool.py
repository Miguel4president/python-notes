# Test stuff
from flask import request, Response
from functools import wraps

from flask.ext.login import LoginManager


login_manager = LoginManager()


# This is the validation on the pair
def check_auth(username, password):
    return username == 'admin' and password == 'secret'


#         Now validate between the token and something related to the public key of the site
def verify_token(token, tenant_id):
    # decrypt token...I think
    return True


# This is just a failure Response Object...doesn't seem to DO anything
def basic_authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def token_authenticate():
    return Response(
        'Could not verify your access level for this URL.\n'
        'This endpoint requires a public key verified token for your site.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def basic_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return basic_authenticate()
        return f(*args, **kwargs)
    return decorated


def token_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        tenant_id = request.view_args['tenant_id']
        token = request.headers['myToken']
        if not token or not verify_token(token, tenant_id):
            return token_authenticate()
        return func(*args, **kwargs)
    return decorated


# login_manager.init_app(app)
@login_manager.request_loader
def load_user_from_request(request):

    # try to login using token match
    tenant_id = request.view_args['tenant_id']
    token = request.headers['myToken']
    if token and verify_token(token, tenant_id):
        return "a good thing"

    # try to login using Basic Auth
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return None

    return "something good, I guess"