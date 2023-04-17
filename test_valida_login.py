from valida_login import *

assert validar_usuario("jokas") == False
assert validar_usuario("Jokas") == True
assert validar_senha("123") == False
assert validar_senha("Senh@do0201") == True
