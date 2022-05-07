from urllib.request import urlopen

def test_connection(module):
    production = False
    if (production == False):
        try:
            if(urlopen("http://localhost:3001/test/{}/test".format(module)).read() != b'OK'):
                print("Error: {} has issues!".format(module))
        except:
            print("Error: {} unreachable!".format(module))
    else:
        pass

def test_connection_mainpage():
    production = False
    if (production == False):
        try:
            if(urlopen("http://localhost:3001/test".read() != b'OK'):
                print("Error: main has issues!".format(module))
        except:
            print("Error: main unreachable!".format(module))
    else:
        pass

test_connection("moduleRegistro")
test_connection("moduleLogin")
test_connection_mainpage()
