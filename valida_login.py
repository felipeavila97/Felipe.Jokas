from cryptographyFramework import *
import re

initializeWrite()

def validar_usuario(user):
    if re.match("^[A-Z][A-Za-z0-9]{0,29}$", user):
        return True
    else:
        return False


def validar_senha(password):
    if re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$!%*#?&])[A-Za-z\d_@$!%*#?&]{10,}$', password):
        return True
    else:
        return False


     