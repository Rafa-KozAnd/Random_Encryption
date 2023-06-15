import random
import string

def gerar_chave_aleatoria():
    alfabeto = list(string.ascii_uppercase)
    random.shuffle(alfabeto)
    chave = {letra: chave_letra for letra, chave_letra in zip(string.ascii_uppercase, alfabeto)}
    return chave

def criptografar(texto, chave):
    texto_criptografado = ""
    for letra in texto.upper():
        if letra.isalpha() and letra in chave:
            texto_criptografado += chave[letra]
        else:
            texto_criptografado += letra
    return texto_criptografado

def descriptografar(texto_criptografado, chave):
    texto = ""
    for letra in texto_criptografado.upper():
        if letra.isalpha() and letra in chave.values():
            for letra_original, chave_letra in chave.items():
                if letra == chave_letra:
                    texto += letra_original
                    break
        else:
            texto += letra
    return texto

def exibir_menu():
    print("\n######################")
    print("===> MENU <===\n")
    print("[1] - Criptografar")
    print("[2] - Descriptografar")
    print("[0] - SAIR")
    print("######################\n")

chave = gerar_chave_aleatoria()
print("Chave: ", chave)

while True:
    exibir_menu()
    opc = input("Escolha uma opção: ")

    if opc == "1":
        texto = input("Digite o texto a ser Criptografado: ")
        texto_criptografado = criptografar(texto, chave)
        print("Texto criptografado:", texto_criptografado)
        
    elif opc == "2":
        texto_criptografado = input("Digite o texto Criptografado: ")
        texto = descriptografar(texto_criptografado, chave)
        print("Texto descriptografado:", texto)
        
    elif opc == "0":
        print("Encerrando código...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")


