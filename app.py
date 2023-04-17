
from cryptographyFramework import *
from valida_login import *



def login():
 while True:
    global user
    user = input("Digite seu nome de usuário (a primeira letra deve ser maiúscula e sem caracteres especiais ou espaços): ")
    if validar_usuario(user):
        break
    else:
        print("O usuário não é válido! Tente novamente.")


 while True:
    global password
    password = input("Digite sua senha (deve ter no mínimo 10 caracteres, uma letra maiúscula, uma letra minúscula, um caractere especial e um número): ")
    if validar_senha(password):
        break
    else:
        print("A senha não é válida! Tente novamente.")

def msg():
 global mensagem
 mensagem = input("Digite a mensagem que deseja criptografar (máximo de 70 caracteres): ")
 if len(mensagem) > 70:
    mensagem = mensagem[:70]
    


login()
msg()


initializeWrite()
encryptedText = encryptMessage(user, password, mensagem)
saveNewLine(encryptedText)
print(mensagem)


