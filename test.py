from urllib.request import urlopen
from config import DEBUG
from controllers import EmpresaController

"""
    Funcionar en debug mode
"""
from functools import wraps
from flask import current_app, abort, request

def debug_only(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not DEBUG:
            abort(403, description="Not in debug.")

        return f(*args, **kwargs)

    return wrap

@debug_only
def test_connection(module):
    if DEBUG:
        try:
            if(urlopen("http://{}/test/{}".format(request.host,module)).read() != b'OK'):
                print("Error: {} has issues!".format(module))
        except:
            print("Error: {} unreachable!".format(module))
            raise Exception("Error: {} unreachable!".format(module))
    else:
        pass

@debug_only
def test_connection_mainpage():
    if DEBUG:
        try:
            if(urlopen("http://{}/test".format(request.host)).read() != b'OK'):
                print("Error: main has issues!")
        except:
            print("Error: main unreachable!")
            raise Exception("Error: main unreachable!")
    else:
        pass

@debug_only
def testBBDD():
    try:
        empresas = EmpresaController.all_query()
    except:
        raise Exception("Error: BBDD!")
    return "OK"

@debug_only
def tests():
    try:
        test_connection("moduleRegistro")
        test_connection("moduleLogin")
        test_connection("testBBDD")
    except:
        return "TEST FAIL, GO TO CONSOLE!"

    return "TEST OK"
