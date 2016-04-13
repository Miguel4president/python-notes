# Test stuff
from flask import request, Response
from functools import wraps


# This is the validation on the pair
def check_auth(username, password):
    return username == 'admin' and password == 'secret'


# Now validate between the token and something related to the public key of the site
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


def cookie_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        tenant_id = request.view_args.get('tenant_id')
        token = request.cookies.get('cookieToken')
        if not token or not verify_token(token, tenant_id):
            return token_authenticate()
        return func(*args, **kwargs)
    return decorated


def token_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        tenant_id = request.view_args.get('tenant_id')
        token = request.headers.get('myToken')
        if not token or not verify_token(token, tenant_id):
            return token_authenticate()
        return func(*args, **kwargs)
    return decorated
